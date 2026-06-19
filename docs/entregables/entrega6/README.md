# Entrega 6 — Documento Final (Artículo Científico IEEE)

> **Curso:** PF3325 – Redes
> **Autores:** Gabriel Fallas & Valeria Chinchilla
> **Fecha de entrega:** Domingo 5 de julio de 2026
> **Formato:** IEEE conference, doble columna, 6 páginas (incluye referencias)

## Contenido

| Archivo | Descripción |
|---------|-------------|
| `main.tex` | Artículo completo en formato `IEEEtran` (conference, doble columna) |
| `references.bib` | 10 referencias en formato BibTeX |
| `figures/` | Figuras del artículo (generadas desde `src/`) |

## Estructura del artículo

1. **Abstract** + keywords
2. **I. Introduction** — motivación, problema, contribuciones
3. **II. Related Work** — Tabla I comparativa + brecha que cerramos (detección en tiempo real)
4. **III. Theoretical Background** — vectores de phishing, dataset UCI, MLP, regularización
5. **IV. Methodology** — preprocesamiento, clasificadores, arquitectura MLP (Fig. 1 y 2)
6. **V. Real-Time Detection Implementation** — extractor de features, límites honestos, API REST + demo
7. **VI. Results and Analysis** — Tabla II (resultados reales), matriz de confusión, ROC, training history
8. **VII. Discussion and Limitations**
9. **VIII. Conclusion**
10. **References** (10)

## Resultados reales incluidos (test set, 1 659 muestras)

| Modelo | Acc | Prec | Recall | F1 | AUC |
|--------|-----|------|--------|----|----|
| Random Forest | 0.972 | 0.969 | 0.981 | 0.975 | 0.996 |
| SVM (RBF) | 0.946 | 0.935 | 0.971 | 0.953 | 0.987 |
| **MLP (propuesto)** | 0.965 | 0.951 | **0.988** | 0.969 | 0.994 |

El MLP logra el **recall más alto (98.8%)**, la métrica decisiva en seguridad
(solo 11 falsos negativos de 924 sitios phishing).

## Cómo compilar el PDF

### Opción A — Overleaf (recomendado, sin instalar nada)

1. Crear un proyecto nuevo en [overleaf.com](https://www.overleaf.com).
2. Subir `main.tex`, `references.bib` y la carpeta `figures/`.
3. Menú **Compiler → pdfLaTeX**. Overleaf corre BibTeX automáticamente.
4. Descargar el PDF (≈ 6 páginas).

### Opción B — Local (TeX Live / MiKTeX)

```bash
cd docs/entregables/entrega6
pdflatex main
bibtex   main
pdflatex main
pdflatex main
```

## Regenerar las figuras

Las figuras se producen desde el código fuente:

```bash
python src/compare_models.py   # roc_comparison.png, confusion_mlp.png, metrics.json
python src/evaluate.py         # training_history.png
python src/make_figures.py     # fig_pipeline.png, fig_mlp.png
# luego copiar reports/*.png -> docs/entregables/entrega6/figures/
```

---
*Entrega 6 – PF3325 Redes | Gabriel Fallas & Valeria Chinchilla | Julio 2026*
