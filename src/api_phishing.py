"""
Real-time phishing detection REST API (FastAPI).

This is the synchronous / real-time detection component required by Entregas 5
and 6. It loads the trained MLP and the fitted StandardScaler and exposes:

    GET  /                 Interactive web demo (HTML form)
    GET  /health           Liveness + model metadata
    POST /predict/features Score a pre-extracted 30-feature vector
    POST /predict/url      Score a raw URL (features extracted on the fly)

Run:
    uvicorn src.api_phishing:app --reload
    # then open http://localhost:8000
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import List, Optional

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

warnings.filterwarnings("ignore")
try:  # silence requests' self-signed warnings used by the extractor
    import requests
    requests.packages.urllib3.disable_warnings()  # type: ignore
except Exception:
    pass

import tensorflow as tf  # noqa: E402

from .feature_extractor import extract_features, FEATURE_ORDER  # noqa: E402

# --------------------------------------------------------------------------- #
# Model loading
# --------------------------------------------------------------------------- #
ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "best_model.keras"
SCALER_PATH = ROOT / "models" / "scaler.joblib"

_model = None
_scaler = None


def _load():
    global _model, _scaler
    if _model is None:
        _model = tf.keras.models.load_model(str(MODEL_PATH))
    if _scaler is None:
        _scaler = joblib.load(str(SCALER_PATH))
    return _model, _scaler


def _predict_vector(vector: List[float]) -> dict:
    model, scaler = _load()
    if len(vector) != 30:
        raise HTTPException(status_code=422,
                            detail=f"Expected 30 features, got {len(vector)}.")
    x = scaler.transform(np.array(vector, dtype=float).reshape(1, -1))
    p_legit = float(model.predict(x, verbose=0).flatten()[0])  # P(legitimate)
    is_legit = p_legit >= 0.5
    return {
        "prediction": "Legitimate" if is_legit else "Phishing",
        "label": "Legítimo" if is_legit else "Phishing",
        "is_phishing": (not is_legit),
        "p_legitimate": round(p_legit, 4),
        "p_phishing": round(1 - p_legit, 4),
        "confidence": round(p_legit if is_legit else 1 - p_legit, 4),
    }


# --------------------------------------------------------------------------- #
# Schemas
# --------------------------------------------------------------------------- #
class FeaturesRequest(BaseModel):
    features: List[float] = Field(..., description="30 feature values in {-1,0,1}")


class URLRequest(BaseModel):
    url: str = Field(..., description="Raw URL to analyze")
    timeout: Optional[int] = Field(6, description="Fetch timeout in seconds")


# --------------------------------------------------------------------------- #
# App
# --------------------------------------------------------------------------- #
app = FastAPI(
    title="Phishing Website Detection API",
    description="Real-time phishing detection using an MLP neural network "
                "trained on the UCI Phishing Websites dataset (PF3325).",
    version="1.0.0",
)


@app.get("/health")
def health():
    model, _ = _load()
    return {
        "status": "ok",
        "model": MODEL_PATH.name,
        "n_features": len(FEATURE_ORDER),
        "params": int(model.count_params()),
    }


@app.post("/predict/features")
def predict_features(req: FeaturesRequest):
    """Classify a pre-extracted 30-feature vector."""
    result = _predict_vector(req.features)
    return result


@app.post("/predict/url")
def predict_url(req: URLRequest):
    """Extract features from a raw URL and classify it in real time."""
    try:
        vector, provenance, info = extract_features(req.url, timeout=req.timeout or 6)
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=400, detail=f"Extraction failed: {exc}")
    result = _predict_vector(vector)
    result["info"] = info
    result["features"] = {
        name: {"value": val, "source": provenance[name]}
        for name, val in zip(FEATURE_ORDER, vector)
    }
    return result


# --------------------------------------------------------------------------- #
# Web demo
# --------------------------------------------------------------------------- #
DEMO_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Phishing Detector — PF3325</title>
<style>
  :root { --bg:#0f172a; --card:#1e293b; --accent:#38bdf8; --ok:#22c55e; --bad:#ef4444; }
  * { box-sizing:border-box; }
  body { font-family:system-ui,Segoe UI,Roboto,sans-serif; background:var(--bg);
         color:#e2e8f0; margin:0; min-height:100vh; display:flex; align-items:center;
         justify-content:center; padding:24px; }
  .card { background:var(--card); border-radius:16px; padding:32px; width:100%;
          max-width:760px; box-shadow:0 20px 60px rgba(0,0,0,.4); }
  h1 { margin:0 0 4px; font-size:1.6rem; }
  .sub { color:#94a3b8; margin:0 0 24px; font-size:.92rem; }
  .row { display:flex; gap:10px; }
  input[type=text] { flex:1; padding:14px 16px; border-radius:10px; border:1px solid #334155;
         background:#0b1220; color:#e2e8f0; font-size:1rem; }
  button { padding:14px 22px; border:0; border-radius:10px; background:var(--accent);
           color:#06283d; font-weight:700; font-size:1rem; cursor:pointer; }
  button:disabled { opacity:.5; cursor:wait; }
  #result { margin-top:24px; display:none; }
  .verdict { font-size:1.5rem; font-weight:800; padding:18px; border-radius:12px;
             text-align:center; }
  .verdict.ok  { background:rgba(34,197,94,.15);  color:var(--ok);  border:1px solid var(--ok); }
  .verdict.bad { background:rgba(239,68,68,.15);  color:var(--bad); border:1px solid var(--bad); }
  .bar { height:10px; background:#0b1220; border-radius:6px; overflow:hidden; margin:14px 0; }
  .bar > span { display:block; height:100%; background:var(--accent); }
  .meta { font-size:.85rem; color:#94a3b8; }
  table { width:100%; border-collapse:collapse; margin-top:16px; font-size:.82rem; }
  td,th { padding:6px 8px; border-bottom:1px solid #334155; text-align:left; }
  .tag { font-size:.7rem; padding:2px 6px; border-radius:4px; }
  .measured { background:#164e63; color:#67e8f9; }
  .default  { background:#3f3f46; color:#d4d4d8; }
  .pill.p1 { color:var(--ok); } .pill.m1 { color:var(--bad); } .pill.z { color:#facc15; }
  .examples { margin-top:14px; font-size:.82rem; color:#94a3b8; }
  .examples a { color:var(--accent); cursor:pointer; text-decoration:underline; }
</style>
</head>
<body>
  <div class="card">
    <h1>🛡️ Phishing Website Detector</h1>
    <p class="sub">Real-time detection &middot; MLP neural network &middot; UCI Phishing Websites &middot; PF3325</p>
    <div class="row">
      <input id="url" type="text" placeholder="https://example.com" autofocus>
      <button id="go" onclick="analyze()">Analizar</button>
    </div>
    <div class="examples">Ejemplos:
      <a onclick="setUrl('https://www.github.com')">github.com</a> &middot;
      <a onclick="setUrl('https://www.wikipedia.org')">wikipedia.org</a> &middot;
      <a onclick="setUrl('https://secure-paypal-verify.com')">URL sospechosa</a>
    </div>
    <div id="result">
      <div id="verdict" class="verdict"></div>
      <div class="bar"><span id="bar"></span></div>
      <div class="meta" id="meta"></div>
      <table id="ftable"></table>
    </div>
  </div>
<script>
function setUrl(u){ document.getElementById('url').value=u; }
async function analyze(){
  const url = document.getElementById('url').value.trim();
  if(!url) return;
  const btn = document.getElementById('go');
  btn.disabled = true; btn.textContent = 'Analizando...';
  try {
    const r = await fetch('/predict/url', {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({url})
    });
    if(!r.ok){ throw new Error((await r.json()).detail || r.statusText); }
    const d = await r.json();
    render(d);
  } catch(e){ alert('Error: ' + e.message); }
  finally { btn.disabled=false; btn.textContent='Analizar'; }
}
function render(d){
  document.getElementById('result').style.display='block';
  const v = document.getElementById('verdict');
  const phish = d.is_phishing;
  v.className = 'verdict ' + (phish ? 'bad' : 'ok');
  v.textContent = (phish ? '⚠️ PHISHING' : '✅ LEGÍTIMO') +
                  '  ·  ' + (d.confidence*100).toFixed(1) + '% confianza';
  document.getElementById('bar').style.width = (d.confidence*100).toFixed(0)+'%';
  const i = d.info;
  document.getElementById('meta').textContent =
    `Dominio: ${i.registered_domain} · ${i.n_measured}/30 features medidas en vivo · ` +
    `redirects: ${i.redirects} · WHOIS: ${i.whois_available?'sí':'no'} · ` +
    `P(phishing)=${d.p_phishing}`;
  const cls = v=> v>0?'pill p1':(v<0?'pill m1':'pill z');
  let rows = '<tr><th>Feature</th><th>Valor</th><th>Fuente</th></tr>';
  for(const [k,o] of Object.entries(d.features)){
    rows += `<tr><td>${k}</td><td class="${cls(o.value)}">${o.value>0?'+1':o.value}</td>`+
            `<td><span class="tag ${o.source}">${o.source}</span></td></tr>`;
  }
  document.getElementById('ftable').innerHTML = rows;
}
document.getElementById('url').addEventListener('keydown', e=>{ if(e.key==='Enter') analyze(); });
</script>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def demo():
    return DEMO_HTML
