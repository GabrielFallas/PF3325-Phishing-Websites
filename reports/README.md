# Reports Directory

Generated artifacts (figures + metrics) used in the Entrega 5 presentation and
the Entrega 6 IEEE paper. Regenerate with the scripts in `src/`.

## Generated assets

| File | Produced by | Used in |
| ---- | ----------- | ------- |
| `metrics.json` | `src/compare_models.py` | Results tables |
| `roc_comparison.png` | `src/compare_models.py` | Fig. ROC (RF/SVM/MLP) |
| `confusion_mlp.png` | `src/compare_models.py` | Fig. MLP confusion matrix |
| `training_history.png` | `src/evaluate.py` | Fig. training curves |
| `fig_pipeline.png` | `src/make_figures.py` | Fig. system architecture |
| `fig_mlp.png` | `src/make_figures.py` | Fig. MLP architecture |
| `confusion_matrix.png`, `roc_curve.png` | `src/evaluate.py` | Single-model plots |

## Final results (test set, 1,659 samples)

| Model | Acc | Prec | Recall | F1 | AUC |
|-------|-----|------|--------|----|----|
| Random Forest | 0.972 | 0.969 | 0.981 | 0.975 | 0.996 |
| SVM (RBF) | 0.946 | 0.935 | 0.971 | 0.953 | 0.987 |
| MLP (proposed) | 0.965 | 0.951 | **0.988** | 0.969 | 0.994 |

## Paper source

The compilable LaTeX paper lives in `docs/entregables/entrega6/`
(`main.tex` + `references.bib` + `figures/`). See that folder's README for
compile instructions (Overleaf or local `pdflatex`).

### Paper Structure

#### Entrega 4 (~3 pages):

1. **Introduction** - Problem context and motivation
2. **Related Work** - Literature review and comparison table
3. **Theoretical Background** - Phishing detection, neural networks, dataset description
4. **References** - IEEE citation style

#### Entrega 6 (6 pages):

1. **Introduction** - Extended problem context
2. **Related Work** - Comprehensive literature review
3. **Theoretical Background** - Deep learning concepts
4. **System Design and Implementation** - Architecture, preprocessing, API
5. **Results and Analysis** - Metrics, comparisons, error analysis
6. **Conclusions and Future Work** - Summary and next steps
7. **References** - IEEE citation style (≥8 references)

## Key References

1. Mohammad, R. M., Thabtah, F., & McCluskey, L. (2012). _An assessment of features related to phishing websites using an automated technique_. ICITST-2012.

2. Mohammad, R. M., Thabtah, F., & McCluskey, L. (2014). _Predicting phishing websites based on self-structuring neural network_. Neural Computing and Applications.

3. Sahingoz, O. K., et al. (2019). _Machine learning based phishing detection from URLs_. Expert Systems with Applications.

4. UCI Machine Learning Repository: Phishing Websites Dataset. https://archive.ics.uci.edu/dataset/327/phishing+websites

## LaTeX Template

For IEEE format papers, use the official IEEE conference template:

- Download from: https://www.ieee.org/conferences/publishing/templates.html
- Use the LaTeX version for best results
- Follow the double-column format

## Notes

- Keep figures and tables within the page limits
- Use vector graphics (PDF, SVG) for plots when possible
- Cite all external sources properly
- Proofread carefully before submission

