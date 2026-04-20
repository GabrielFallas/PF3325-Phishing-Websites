"""
check_phishing_dataset.py
=========================
Script de inspección de calidad para el dataset de sitios web de phishing.
Fuente: UCI ML Repository — ID 327 (Phishing Websites)
Uso:   python check_phishing_dataset.py Training_Dataset.arff
"""

import sys
import pandas as pd
import numpy as np
from io import StringIO

# ── Helpers ─────────────────────────────────────────────────────────────────

def separator(title=""):
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)

def load_arff(path):
    """Parsea un archivo .arff y retorna (DataFrame, dict de atributos)."""
    attributes = {}
    data_lines = []
    in_data = False

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("%"):
                continue
            upper = line.upper()
            if upper.startswith("@ATTRIBUTE"):
                parts = line.split()
                attr_name = parts[1]
                attr_type = " ".join(parts[2:])
                attributes[attr_name] = attr_type
            elif upper.startswith("@DATA"):
                in_data = True
            elif in_data:
                data_lines.append(line)

    cols = list(attributes.keys())
    df = pd.read_csv(StringIO("\n".join(data_lines)), header=None, names=cols)
    return df, attributes


# ── Main ─────────────────────────────────────────────────────────────────────

def main(path):
    df, attributes = load_arff(path)
    target_col = "Result"
    feature_cols = [c for c in df.columns if c != target_col]

    # ── 1. Información básica ─────────────────────────────────────────────
    separator("1. INFORMACIÓN BÁSICA")
    print(df.info())
    print(f"\nFilas   : {len(df):,}")
    print(f"Columnas: {len(df.columns)}  (features: {len(feature_cols)}, target: 1)")

    # ── 2. Valores únicos por atributo (según definición ARFF) ───────────
    separator("2. VALORES DECLARADOS EN ARFF vs OBSERVADOS EN DATOS")
    for attr, atype in attributes.items():
        observed = sorted(df[attr].dropna().unique().tolist())
        print(f"  {attr:<35} declarados={atype:<20} observados={observed}")

    # ── 3. Valores faltantes ──────────────────────────────────────────────
    separator("3. VALORES FALTANTES")
    missing = df.isnull().sum()
    print(missing[missing > 0].to_string() if missing.sum() > 0 else "  ✓ Sin valores nulos detectados")
    print(f"\n  Total de celdas nulas: {missing.sum()}")

    # ── 4. Filas duplicadas ───────────────────────────────────────────────
    separator("4. FILAS DUPLICADAS")
    n_dup = df.duplicated().sum()
    print(f"  Filas duplicadas: {n_dup}")
    if n_dup > 0:
        print(df[df.duplicated(keep=False)].head(10))

    # ── 5. Balance de clases ──────────────────────────────────────────────
    separator("5. BALANCE DE CLASES (target: Result)")
    counts = df[target_col].value_counts()
    props  = df[target_col].value_counts(normalize=True)
    summary = pd.DataFrame({"Etiqueta": ["Legítimo (1)", "Phishing (-1)"],
                             "Conteo":   [counts.get(1, 0), counts.get(-1, 0)],
                             "Proporción": [f"{props.get(1,0):.2%}", f"{props.get(-1,0):.2%}"]})
    print(summary.to_string(index=False))
    ratio = counts.max() / counts.min() if counts.min() > 0 else float("inf")
    print(f"\n  Ratio mayoría/minoría: {ratio:.2f}x")

    # ── 6. Valores fuera del rango esperado ──────────────────────────────
    separator("6. VALORES FUERA DEL RANGO DECLARADO {-1, 0, 1}")
    unexpected = {}
    allowed = {-1, 0, 1}
    for col in df.columns:
        vals = set(df[col].dropna().unique().tolist())
        extra = vals - allowed
        if extra:
            unexpected[col] = extra
    if unexpected:
        for col, vals in unexpected.items():
            print(f"  {col}: valores inesperados → {vals}")
    else:
        print("  ✓ Todos los valores están dentro de {-1, 0, 1}")

    # ── 7. Frecuencia de cada valor por feature ───────────────────────────
    separator("7. DISTRIBUCIÓN DE VALORES POR FEATURE")
    for col in df.columns:
        vc = df[col].value_counts().sort_index()
        vc_str = "  ".join([f"{k}:{v}" for k, v in vc.items()])
        print(f"  {col:<35} {vc_str}")

    # ── 8. Varianza cero (features constantes) ────────────────────────────
    separator("8. FEATURES CON VARIANZA CERO O MUY BAJA (posibles constantes)")
    low_var = []
    for col in feature_cols:
        dominant_freq = df[col].value_counts(normalize=True).iloc[0]
        if dominant_freq >= 0.95:
            top_val = df[col].value_counts().index[0]
            low_var.append((col, top_val, f"{dominant_freq:.1%}"))
    if low_var:
        for col, val, freq in low_var:
            print(f"  {col:<35} valor dominante={val}  frecuencia={freq}")
    else:
        print("  ✓ Ninguna feature con valor dominante >= 95%")

    # ── 9. Correlación entre features (altamente correlacionadas) ─────────
    separator("9. PARES DE FEATURES MUY CORRELACIONADAS (|r| >= 0.80)")
    corr = df[feature_cols].corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    high_corr = [(col, row, upper.loc[row, col])
                 for col in upper.columns
                 for row in upper.index
                 if pd.notna(upper.loc[row, col]) and upper.loc[row, col] >= 0.80]
    if high_corr:
        for c1, c2, r in sorted(high_corr, key=lambda x: -x[2]):
            print(f"  {c1} ↔ {c2}  r={r:.3f}")
    else:
        print("  ✓ Ningún par con correlación >= 0.80")

    # ── 10. Correlación de cada feature con el target ─────────────────────
    separator("10. CORRELACIÓN DE FEATURES CON EL TARGET (|r|, ordenado desc)")
    target_corr = df[feature_cols].corrwith(df[target_col]).abs().sort_values(ascending=False)
    for feat, r in target_corr.items():
        bar = "█" * int(r * 20)
        print(f"  {feat:<35} r={r:.3f}  {bar}")

    # ── 11. Columnas con valores 0 declarados vs no declarados ────────────
    separator("11. USO DEL VALOR '0' (valor intermedio / 'sospechoso')")
    for col in df.columns:
        if 0 in df[col].values:
            n0 = (df[col] == 0).sum()
            pct = n0 / len(df) * 100
            declared = "0" in attributes.get(col, "")
            print(f"  {col:<35} n=0:{n0:>5}  ({pct:.1f}%)  declarado={declared}")

    separator("INSPECCIÓN COMPLETA")
    print("  Script finalizado sin errores.\n")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "Training_Dataset.arff"
    main(path)
