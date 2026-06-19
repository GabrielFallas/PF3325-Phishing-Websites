"""
Real-time feature extraction for phishing detection.

Given a raw URL, this module computes the 30 features of the UCI Phishing
Websites dataset (Mohammad et al., 2012/2014) so the trained model can score
an arbitrary, previously-unseen URL.

Each feature is encoded with the dataset's ternary convention:
    1  -> legitimate pattern
    0  -> suspicious pattern
   -1  -> phishing pattern

IMPORTANT — honesty about real-time extraction
----------------------------------------------
The original dataset was built (2012-2014) using third-party services that are
now defunct or paid-only:
  * web_traffic  -> Alexa rank      (Alexa was retired in May 2022)
  * Page_Rank    -> Google PageRank (the public Toolbar PageRank was retired in 2016)
  * Links_pointing_to_page -> external backlink index (no free API)
  * Google_Index / Statistical_report -> require search-engine / threat-intel APIs

For those features we fall back to a *neutral / conservative default* and record
that the value was NOT measured from live data. The `extract_features` function
returns both the 30-value vector (in the exact training order) and a per-feature
provenance map so the API and the demo can be transparent about what was actually
observed versus defaulted.

Features grounded in the URL string, the fetched HTML/JS, DNS and WHOIS are
computed for real.
"""

from __future__ import annotations

import re
import socket
import ssl
from datetime import datetime
from urllib.parse import urlparse, urljoin

import requests

try:
    import tldextract
    _HAS_TLDEXTRACT = True
except Exception:  # pragma: no cover
    _HAS_TLDEXTRACT = False

try:
    from bs4 import BeautifulSoup
    _HAS_BS4 = True
except Exception:  # pragma: no cover
    _HAS_BS4 = False

try:
    import whois as _whois
    _HAS_WHOIS = True
except Exception:  # pragma: no cover
    _HAS_WHOIS = False

try:
    import dns.resolver as _dnsresolver
    _HAS_DNS = True
except Exception:  # pragma: no cover
    _HAS_DNS = False


# Exact feature order expected by the scaler / model (models/feature_names.joblib)
FEATURE_ORDER = [
    "having_IP_Address", "URL_Length", "Shortining_Service", "having_At_Symbol",
    "double_slash_redirecting", "Prefix_Suffix", "having_Sub_Domain",
    "SSLfinal_State", "Domain_registeration_length", "Favicon", "port",
    "HTTPS_token", "Request_URL", "URL_of_Anchor", "Links_in_tags", "SFH",
    "Submitting_to_email", "Abnormal_URL", "Redirect", "on_mouseover",
    "RightClick", "popUpWidnow", "Iframe", "age_of_domain", "DNSRecord",
    "web_traffic", "Page_Rank", "Google_Index", "Links_pointing_to_page",
    "Statistical_report",
]

SHORTENERS = {
    "bit.ly", "goo.gl", "tinyurl.com", "ow.ly", "t.co", "is.gd", "buff.ly",
    "adf.ly", "bit.do", "cutt.ly", "shorte.st", "rebrand.ly", "tiny.cc",
    "rb.gy", "shorturl.at", "soo.gd", "s2r.co", "clck.ru", "tr.im",
}

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _registered_domain(netloc: str) -> str:
    host = netloc.split(":")[0]
    if _HAS_TLDEXTRACT:
        ext = tldextract.extract(host)
        if ext.domain and ext.suffix:
            return f"{ext.domain}.{ext.suffix}"
    return host


def _is_ip(host: str) -> bool:
    host = host.split(":")[0]
    # IPv4 dotted or hex/octal, or bracketed IPv6
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host):
        return True
    if re.match(r"^0x[0-9a-fA-F]+", host):
        return True
    if ":" in host:
        return True
    return False


def _same_domain(url: str, base_domain: str) -> bool:
    """True if a (possibly relative) resource URL belongs to base_domain."""
    if not url:
        return True
    url = url.strip()
    if url.startswith("#") or url.startswith("javascript:") or url.startswith("mailto:"):
        return True
    if url.startswith("/") or not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        return True  # relative -> same domain
    try:
        return _registered_domain(urlparse(url).netloc) == base_domain
    except Exception:
        return True


def _pct_band(pct: float, low: float, high: float) -> int:
    """Generic three-way band: <low ->1, [low,high] ->0, >high ->-1."""
    if pct < low:
        return 1
    if pct <= high:
        return 0
    return -1


# --------------------------------------------------------------------------- #
# Main extraction
# --------------------------------------------------------------------------- #
def extract_features(url: str, timeout: int = 6):
    """
    Extract the 30 UCI features from a raw URL.

    Returns
    -------
    vector : list[int]                30 values in FEATURE_ORDER
    provenance : dict[str, str]       feature -> "measured" | "default" | "partial"
    info : dict                       extra diagnostics (domain, fetched, etc.)
    """
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        url = "http://" + url

    parsed = urlparse(url)
    netloc = parsed.netloc
    host = netloc.split(":")[0]
    base_domain = _registered_domain(netloc)

    f: dict[str, int] = {}
    prov: dict[str, str] = {}

    def measured(name, value):
        f[name] = int(value)
        prov[name] = "measured"

    def default(name, value, kind="default"):
        f[name] = int(value)
        prov[name] = kind

    # --- Try to fetch the page once (used by several features) -------------- #
    html = None
    resp = None
    redirect_count = 0
    final_url = url
    try:
        resp = requests.get(
            url, timeout=timeout, headers={"User-Agent": USER_AGENT},
            allow_redirects=True, verify=False,
        )
        html = resp.text or ""
        redirect_count = len(resp.history)
        final_url = resp.url
    except Exception:
        html = None

    soup = None
    if html and _HAS_BS4:
        try:
            soup = BeautifulSoup(html, "html.parser")
        except Exception:
            soup = None

    # 1. having_IP_Address -------------------------------------------------- #
    measured("having_IP_Address", -1 if _is_ip(host) else 1)

    # 2. URL_Length --------------------------------------------------------- #
    n = len(url)
    measured("URL_Length", 1 if n < 54 else (0 if n <= 75 else -1))

    # 3. Shortining_Service ------------------------------------------------- #
    measured("Shortining_Service", -1 if base_domain in SHORTENERS else 1)

    # 4. having_At_Symbol --------------------------------------------------- #
    measured("having_At_Symbol", -1 if "@" in url else 1)

    # 5. double_slash_redirecting ------------------------------------------- #
    last = url.rfind("//")
    measured("double_slash_redirecting", -1 if last > 7 else 1)

    # 6. Prefix_Suffix ------------------------------------------------------ #
    measured("Prefix_Suffix", -1 if "-" in host else 1)

    # 7. having_Sub_Domain -------------------------------------------------- #
    h = host
    if h.startswith("www."):
        h = h[4:]
    dots = h.count(".")
    if _HAS_TLDEXTRACT:
        sub = tldextract.extract(host).subdomain
        sub = sub.replace("www", "").strip(".")
        nsub = 0 if not sub else sub.count(".") + 1
        measured("having_Sub_Domain", 1 if nsub == 0 else (0 if nsub == 1 else -1))
    else:
        measured("having_Sub_Domain", 1 if dots <= 1 else (0 if dots == 2 else -1))

    # 8. SSLfinal_State ----------------------------------------------------- #
    ssl_state = -1
    if parsed.scheme == "https" or final_url.startswith("https"):
        ssl_state = _check_ssl(host, parsed.port or 443, timeout)
    measured("SSLfinal_State", ssl_state)

    # WHOIS (shared by features 9, 24, 18) ---------------------------------- #
    w = None
    if _HAS_WHOIS and not _is_ip(host):
        try:
            w = _whois.whois(base_domain)
        except Exception:
            w = None

    # 9. Domain_registeration_length ---------------------------------------- #
    exp = _first_date(getattr(w, "expiration_date", None)) if w else None
    if exp:
        months = (exp - datetime.now()).days / 30.0
        measured("Domain_registeration_length", 1 if months > 12 else -1)
    else:
        default("Domain_registeration_length", -1)

    # 10. Favicon ----------------------------------------------------------- #
    if soup is not None:
        ico = None
        for link in soup.find_all("link"):
            rel = " ".join(link.get("rel", [])).lower()
            if "icon" in rel:
                ico = link.get("href")
                break
        if ico is None:
            measured("Favicon", 1)
        else:
            measured("Favicon", 1 if _same_domain(ico, base_domain) else -1)
    else:
        default("Favicon", 1)

    # 11. port -------------------------------------------------------------- #
    if parsed.port and parsed.port not in (80, 443):
        measured("port", -1)
    else:
        default("port", 1)  # full port scan not performed in real time

    # 12. HTTPS_token ------------------------------------------------------- #
    measured("HTTPS_token", -1 if "https" in host.lower() else 1)

    # 13-17, 19-23: HTML/JS based ------------------------------------------- #
    if soup is not None:
        _html_features(soup, html, base_domain, final_url, measured)
    else:
        for name in ("Request_URL", "URL_of_Anchor", "Links_in_tags", "SFH",
                     "Submitting_to_email", "on_mouseover", "RightClick",
                     "popUpWidnow", "Iframe"):
            default(name, 0 if name in ("Request_URL", "URL_of_Anchor",
                                        "Links_in_tags") else 1)

    # 18. Abnormal_URL ------------------------------------------------------ #
    if w is not None:
        has_record = bool(getattr(w, "domain_name", None))
        measured("Abnormal_URL", 1 if has_record else -1)
    else:
        default("Abnormal_URL", -1 if not _HAS_WHOIS else 1)

    # 19. Redirect ---------------------------------------------------------- #
    if resp is not None:
        measured("Redirect", 1 if redirect_count <= 1 else (0 if redirect_count <= 3 else -1))
    else:
        default("Redirect", 1)

    # 24. age_of_domain ----------------------------------------------------- #
    cre = _first_date(getattr(w, "creation_date", None)) if w else None
    if cre:
        age_months = (datetime.now() - cre).days / 30.0
        measured("age_of_domain", 1 if age_months >= 6 else -1)
    else:
        default("age_of_domain", -1)

    # 25. DNSRecord --------------------------------------------------------- #
    measured("DNSRecord", _dns_record(host))

    # 26. web_traffic  (Alexa retired 2022) --------------------------------- #
    default("web_traffic", 0, kind="default")

    # 27. Page_Rank    (Google PageRank retired 2016) ----------------------- #
    default("Page_Rank", 0, kind="default")

    # 28. Google_Index  (needs search API) ---------------------------------- #
    default("Google_Index", 1, kind="default")

    # 29. Links_pointing_to_page  (needs backlink index) -------------------- #
    default("Links_pointing_to_page", 0, kind="default")

    # 30. Statistical_report  (needs threat-intel feed) --------------------- #
    default("Statistical_report", 1, kind="default")

    vector = [f[name] for name in FEATURE_ORDER]
    info = {
        "url": url,
        "final_url": final_url,
        "registered_domain": base_domain,
        "page_fetched": html is not None,
        "redirects": redirect_count,
        "whois_available": w is not None,
        "n_measured": sum(1 for v in prov.values() if v == "measured"),
        "n_default": sum(1 for v in prov.values() if v != "measured"),
    }
    return vector, prov, info


def _check_ssl(host: str, port: int, timeout: int) -> int:
    """1 if a valid trusted cert is presented, 0 if https but problematic, -1 none."""
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                return 1 if cert else 0
    except ssl.SSLError:
        return 0  # certificate present but not trusted / hostname mismatch
    except Exception:
        return 0  # reachable assumption failed; treat as suspicious, not absent


def _html_features(soup, html, base_domain, final_url, measured):
    # 13. Request_URL: external embedded objects (img, audio, video, embed)
    objs = soup.find_all(["img", "audio", "video", "embed", "iframe", "source"])
    ext = tot = 0
    for tag in objs:
        src = tag.get("src") or tag.get("href")
        if not src:
            continue
        tot += 1
        if not _same_domain(src, base_domain):
            ext += 1
    pct = 100 * ext / tot if tot else 0
    measured("Request_URL", _pct_band(pct, 22, 61))

    # 14. URL_of_Anchor
    anchors = soup.find_all("a")
    ext_a = tot_a = 0
    for a in anchors:
        href = (a.get("href") or "").strip()
        tot_a += 1
        if href in ("", "#", "#nothing", "#doesnotexist", "#skip") \
                or href.startswith("javascript:void") or href.lower().startswith("javascript"):
            ext_a += 1
        elif not _same_domain(href, base_domain):
            ext_a += 1
    pct_a = 100 * ext_a / tot_a if tot_a else 0
    measured("URL_of_Anchor", _pct_band(pct_a, 31, 67))

    # 15. Links_in_tags: link/script/meta pointing externally
    tags = soup.find_all(["link", "script"])
    ext_t = tot_t = 0
    for tag in tags:
        src = tag.get("href") or tag.get("src")
        if not src:
            continue
        tot_t += 1
        if not _same_domain(src, base_domain):
            ext_t += 1
    pct_t = 100 * ext_t / tot_t if tot_t else 0
    measured("Links_in_tags", _pct_band(pct_t, 17, 81))

    # 16. SFH: form action handler
    sfh = 1
    forms = soup.find_all("form")
    for form in forms:
        action = (form.get("action") or "").strip()
        if action in ("", "about:blank"):
            sfh = -1
            break
        if not _same_domain(action, base_domain):
            sfh = 0
    measured("SFH", sfh)

    # 17. Submitting_to_email
    mail = ("mailto:" in (html or "").lower()) or ("mail(" in (html or "").lower())
    measured("Submitting_to_email", -1 if mail else 1)

    low = (html or "").lower()
    # 20. on_mouseover (status bar manipulation)
    measured("on_mouseover", -1 if "onmouseover" in low and "window.status" in low else 1)
    # 21. RightClick disabled
    measured("RightClick", -1 if ("event.button==2" in low or "contextmenu" in low) else 1)
    # 22. popUpWidnow
    measured("popUpWidnow", -1 if ("window.open(" in low or "alert(" in low) else 1)
    # 23. Iframe
    measured("Iframe", -1 if soup.find("iframe") is not None else 1)


def _dns_record(host: str) -> int:
    if _is_ip(host):
        return 1
    if _HAS_DNS:
        try:
            _dnsresolver.resolve(host, "A", lifetime=4)
            return 1
        except Exception:
            try:
                _dnsresolver.resolve(host, "AAAA", lifetime=4)
                return 1
            except Exception:
                return -1
    # fallback to socket
    try:
        socket.gethostbyname(host)
        return 1
    except Exception:
        return -1


def _first_date(value):
    if value is None:
        return None
    if isinstance(value, list):
        value = next((v for v in value if v is not None), None)
    if isinstance(value, datetime):
        # Normalize to naive local time so arithmetic with datetime.now() works
        if value.tzinfo is not None:
            value = value.replace(tzinfo=None)
        return value
    return None


if __name__ == "__main__":
    import sys
    import warnings
    warnings.filterwarnings("ignore")
    requests.packages.urllib3.disable_warnings()  # type: ignore
    test_url = sys.argv[1] if len(sys.argv) > 1 else "https://www.google.com"
    vec, prov, info = extract_features(test_url)
    print(f"\nURL: {test_url}")
    print(f"Info: {info}\n")
    for name, val in zip(FEATURE_ORDER, vec):
        print(f"  {name:30s} {val:+d}   [{prov[name]}]")
