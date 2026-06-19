"""
Generate diagram figures for the Entrega 6 IEEE paper and the Entrega 5 slides:
    reports/fig_pipeline.png      end-to-end system architecture
    reports/fig_mlp.png           MLP layer diagram
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

Path("reports").mkdir(exist_ok=True)


def box(ax, x, y, w, h, text, fc):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=fc, ec="#1e293b", lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=9, weight="bold", color="#0f172a")


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=14, lw=1.4, color="#334155"))


# --------------------------------------------------------------------------- #
# Fig 1: pipeline
# --------------------------------------------------------------------------- #
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")

ax.text(6, 7.6, "Phishing Detection System Architecture", ha="center",
        fontsize=12, weight="bold")

# Offline (training) lane
ax.text(0.2, 6.7, "A. Offline training", fontsize=9, weight="bold", color="#1d4ed8")
box(ax, 0.3, 5.2, 2.0, 1.1, "UCI Dataset\n11,055 × 30", "#dbeafe")
box(ax, 2.7, 5.2, 2.0, 1.1, "Preprocess\nencode + scale", "#dbeafe")
box(ax, 5.1, 5.2, 2.0, 1.1, "Train MLP\n+ RF / SVM", "#dbeafe")
box(ax, 7.5, 5.2, 2.1, 1.1, "Evaluate\nAcc/F1/AUC", "#dbeafe")
box(ax, 9.9, 5.2, 1.9, 1.1, "Persist\n.keras +\nscaler", "#bfdbfe")
for x in (2.3, 4.7, 7.1, 9.5):
    arrow(ax, x, 5.75, x + 0.4, 5.75)

# Real-time lane
ax.text(0.2, 3.9, "B. Real-time detection (synchronous)", fontsize=9,
        weight="bold", color="#b91c1c")
box(ax, 0.3, 2.3, 2.0, 1.1, "Raw URL\n(user/API)", "#fee2e2")
box(ax, 2.7, 2.3, 2.2, 1.1, "Feature\nExtractor\nURL+HTML+DNS+WHOIS", "#fee2e2")
box(ax, 5.3, 2.3, 1.9, 1.1, "Scaler\n(loaded)", "#fed7aa")
box(ax, 7.6, 2.3, 1.9, 1.1, "MLP\ninference", "#fed7aa")
box(ax, 9.9, 2.3, 1.9, 1.1, "Verdict +\nconfidence", "#fecaca")
for x in (2.3, 4.9, 7.2, 9.5):
    arrow(ax, x, 2.85, x + 0.4, 2.85)

# link persisted model to real-time
arrow(ax, 10.85, 5.2, 8.55, 3.4)
ax.text(10.2, 4.4, "load", fontsize=8, style="italic", color="#475569")

box(ax, 4.4, 0.4, 3.2, 0.95, "FastAPI service  +  Web demo", "#e0e7ff")
arrow(ax, 6.0, 2.3, 6.0, 1.35)

plt.tight_layout()
plt.savefig("reports/fig_pipeline.png", dpi=160, bbox_inches="tight")
plt.close()
print("✓ reports/fig_pipeline.png")


# --------------------------------------------------------------------------- #
# Fig 2: MLP architecture
# --------------------------------------------------------------------------- #
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
ax.text(5, 5.6, "MLP Architecture", ha="center", fontsize=12, weight="bold")

layers = [
    ("Input\n30", "#cbd5e1", "30 features"),
    ("Dense 128\nBN+ReLU\nDrop 0.3", "#93c5fd", ""),
    ("Dense 64\nBN+ReLU\nDrop 0.2", "#60a5fa", ""),
    ("Dense 32\nReLU\nDrop 0.1", "#3b82f6", ""),
    ("Sigmoid\n1", "#22c55e", "P(legit)"),
]
x = 0.35
w = 1.5
gap = 0.38
for i, (txt, fc, sub) in enumerate(layers):
    box(ax, x, 2.0, w, 1.8, txt, fc)
    if sub:
        ax.text(x + w / 2, 1.6, sub, ha="center", fontsize=8, color="#475569")
    if i < len(layers) - 1:
        arrow(ax, x + w, 2.9, x + w + gap, 2.9)
    x += w + gap

ax.text(5, 0.7, "L2 regularization · Adam (lr=1e-3) · Binary cross-entropy · "
        "Early stopping (patience=10)  ·  15,105 params",
        ha="center", fontsize=8, color="#334155")

plt.tight_layout()
plt.savefig("reports/fig_mlp.png", dpi=160, bbox_inches="tight")
plt.close()
print("✓ reports/fig_mlp.png")
