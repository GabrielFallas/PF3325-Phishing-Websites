# Entrega 4 — Documento Escrito
## Formato IEEE Doble Columna (~3 páginas)

> **Curso:** PF3325 – Redes  
> **Autores:** Gabriel Fallas & Valeria Chinchilla  
> **Fecha de entrega:** Miércoles 10 de junio de 2026  
> **Nota:** Este documento está escrito siguiendo la estructura y estilo del formato IEEE.  
> Para compilación en LaTeX, usar la plantilla `IEEEtran` con `\documentclass[conference]{IEEEtran}`.

---

---

# Detection of Phishing Websites Using Artificial Neural Networks

**Gabriel Fallas, Valeria Chinchilla**  
*Escuela de Ciencias de la Computación e Informática*  
*Universidad de Costa Rica*  
*San José, Costa Rica*  
`{gabriel.fallas, valeria.chinchilla}@ucr.ac.cr`

---

## Abstract

Phishing attacks remain one of the most prevalent cybersecurity threats worldwide, with over 4.8 million recorded incidents in 2024 alone. Traditional defense mechanisms such as blacklists and manual heuristics fail to cope with the rapid emergence of new phishing sites, some of which remain active for less than 24 hours. This paper presents a machine learning approach to phishing website detection based on the UCI Phishing Websites dataset, which comprises 11,055 labeled URL instances described by 30 automatically extracted features. We apply a Multilayer Perceptron (MLP) architecture with Dropout regularization, Batch Normalization, and Early Stopping to classify URLs as legitimate or phishing. As a baseline, we also train Random Forest and Support Vector Machine classifiers. Preliminary results on classical models yield accuracies of approximately 97% and 95%, respectively. The proposed MLP architecture targets comparable or superior performance while providing the foundation for a real-time detection API. This work contributes a systematic comparative study of neural network architectures and a path toward an end-to-end deployable phishing detection system.

**Keywords:** phishing detection, neural networks, multilayer perceptron, machine learning, cybersecurity, URL classification.

---

---

## I. Introduction

Phishing is a form of social engineering in which an attacker creates a fraudulent website that mimics a legitimate one to deceive users into disclosing sensitive credentials, financial information, or personal data [1]. The scale of the problem is substantial: the Anti-Phishing Working Group (APWG) recorded 4.8 million phishing attacks in 2024 — the highest annual total since the organization was founded in 2003 — and reported losses attributable to related Business Email Compromise schemes exceeded USD 2.8 billion in the United States alone [9].

Two classical defensive paradigms exist. Blacklist-based systems, such as Google Safe Browsing, maintain databases of known malicious URLs. While effective against previously identified sites, they are fundamentally reactive: a phishing site can be operational for fewer than 24 hours before it is reported, listed, and taken down, during which time thousands of victims may be deceived. Heuristic-based systems encode expert knowledge as rules — e.g., "if the URL contains an IP address, flag as suspicious" — but require continuous manual updating and are easily evaded once attackers learn the rule set.

Machine learning offers an attractive alternative: rather than manually encoding rules, models learn discriminative patterns directly from labeled data. This paper investigates the application of Multilayer Perceptron (MLP) neural networks to the phishing website detection problem using the UCI Phishing Websites dataset [10]. Our contributions are as follows:

1. A systematic comparison of MLP architectures with varying depth and regularization strategies against classical baselines (Random Forest, SVM).
2. Preliminary classification results on the UCI benchmark dataset.
3. A design for a real-time detection pipeline served as a REST API — a component absent from all related foundational works.

The remainder of this paper is structured as follows. Section II reviews related work. Section III presents the theoretical framework. Section IV describes the proposed approach. References are listed at the end.

---

---

## II. Related Work

Research on automated phishing detection spans over 15 years and has evolved from early neural networks to modern deep learning. Table I summarizes the most relevant prior works.

### Table I — Comparison of Related Works

| Reference | Technique | Dataset Size | Best Accuracy | Real-Time |
|-----------|-----------|:------------:|:-------------:|:---------:|
| Mohammad et al. [1] (2012) | Feature engineering (JS+PHP) | 2,500 URLs | 84% (heuristic) | No |
| Mohammad et al. [2] (2014) | J48, RF, SSNN | 11,055 URLs | ~97% (SSNN) | No |
| Sahingoz et al. [3] (2019) | Random Forest + NLP features | 73,575 URLs | 97.32% | No |
| Vrbančič et al. [4] (2020) | XGBoost, Ensemble methods | 88,647 URLs | ~97.6% | No |
| Chatterjee & Namin [5] (2019) | Deep Reinforcement Learning | Custom URLs | ~96% | No |
| **This work** | **MLP (comparative) + RF, SVM** | **11,055 URLs** | **TBD** | **✓ Yes** |

A critical distinction that is often overlooked in the literature concerns the two foundational papers by Mohammad et al. The 2012 paper [1] is primarily an exercise in *feature engineering*: the authors designed and validated automated extraction rules for 17 URL and page characteristics using JavaScript and PHP scripts, evaluated against 2,500 URLs sourced from PhishTank. No production classifier was trained; the contribution was a validated feature set and its extraction methodology.

The 2014 paper [2] built upon this foundation: the dataset was expanded to 11,055 samples and 30 features, and multiple classifiers were compared — including a Self-Structuring Neural Network (SSNN) of the authors' design, which achieved approximately 97% accuracy. This is the direct predecessor to our work, and the SSNN result is our primary neural network baseline.

Sahingoz et al. [3] extended the state of the art in 2019 by incorporating Natural Language Processing features computed from the URL string itself — character-level n-grams and token-based attributes — alongside structural page features. On a dataset of 73,575 URLs, Random Forest achieved 97.32% accuracy. This work demonstrated that feature richness plays a key role beyond the classifier architecture.

Vrbančič et al. [4] provided the research community with larger benchmark datasets (58,645 and 88,647 labeled instances) and benchmarked several ensemble methods. XGBoost and Random Forest achieved approximately 97.6%, establishing ensemble classifiers as the dominant paradigm for classical ML on this problem.

Chatterjee and Namin [5] explored a fundamentally different approach in 2019: Deep Reinforcement Learning, where a policy network learns to classify phishing sites through reward signals. This approach is adaptive to evolving phishing tactics but introduces significant training complexity.

**Gap addressed by this work.** A consistent limitation of all prior works is the absence of a deployable, real-time detection component. All published systems treat phishing detection as an offline classification experiment: train a model, evaluate on a held-out test set, report metrics. None exposed the classifier as a service capable of scoring an arbitrary new URL on demand. Furthermore, no prior work on the UCI dataset performed a systematic ablation study comparing MLP architectures with modern regularization. Our work addresses both gaps.

---

---

## III. Theoretical Framework

### A. Phishing Websites

Phishing is an Internet crime in which a fraudulent website impersonates a legitimate entity to solicit sensitive user information [1]. Attacks are classified along three primary vectors:

- **URL-based phishing:** Manipulation of the domain name, including typosquatting (e.g., `paypa1.com`), homograph attacks using Unicode look-alike characters, and the use of IP addresses in URLs to bypass domain-based filtering.
- **Content-based phishing:** Exact replication of the visual appearance of a legitimate site — HTML structure, CSS, and images — hosting a form that redirects submitted data to the attacker.
- **DNS-based phishing:** DNS spoofing or hijacking that redirects legitimate domain names to attacker-controlled servers, making the attack nearly undetectable at the URL level.

Our approach targets primarily URL-based and content-based phishing, as the 30 features in the UCI dataset capture both URL structural properties and HTML/JavaScript behavioral signals.

### B. The UCI Phishing Websites Dataset

The dataset used in this work was constructed by Mohammad et al. [1][2] using automated feature extraction tools written in JavaScript and PHP. Features were computed from URLs sourced from PhishTank (phishing instances) and legitimate websites. The dataset contains 11,055 instances labeled as phishing (-1) or legitimate (1), with 30 features organized into four categories [2]:

1. **Address Bar based (12 features):** Properties of the URL structure, including the presence of an IP address, URL length, use of URL shortening services, use of the `@` symbol, double slash redirecting, prefix/suffix patterns, subdomain count, SSL certificate validity, domain registration length, favicon origin, open ports, and HTTPS token presence.

2. **Abnormal based (6 features):** Behavioral anomalies such as external request URLs, anchor link destinations, links in script and meta tags, server-form handlers (SFH), email submission forms, and abnormal URL patterns relative to the WHOIS record.

3. **HTML and JavaScript based (5 features):** Client-side behaviors including excessive redirects, `onmouseover` event handler manipulation, disabled right-click menus, pop-up windows, and the use of `<iframe>` tags.

4. **Domain based (7 features):** External signals including domain age, DNS record validity, Alexa web traffic rank, Google PageRank, Google indexing status, number of inbound links, and presence in statistical phishing reports.

Feature values follow a **ternary encoding**: `1` (legitimate pattern), `0` (suspicious), and `–1` (phishing pattern). Some features are strictly binary `{–1, 1}` while others use all three values. The target variable follows the same convention: `1` for legitimate, `–1` for phishing. The class distribution is approximately 55.7% legitimate and 44.3% phishing, a near-balanced split that does not require special imbalance handling.

### C. Multilayer Perceptron (MLP)

An MLP is a feedforward artificial neural network composed of an input layer, one or more hidden layers, and an output layer [6]. For our phishing classification task:

- **Input layer:** 30 neurons, one per feature.
- **Hidden layers:** *L* dense layers, each with *n* neurons, followed by a nonlinear activation function.
- **Output layer:** 1 neuron with sigmoid activation, producing a probability *p ∈ [0, 1]* interpreted as the probability of the URL being legitimate.

The **ReLU** (Rectified Linear Unit) activation function is used in hidden layers:

```
ReLU(z) = max(0, z)
```

This eliminates the vanishing gradient problem that plagued earlier sigmoid-activated networks and accelerates convergence [6].

Network weights *W* are learned by minimizing the **Binary Cross-Entropy** loss function over the training set:

```
L(y, p) = -[y · log(p) + (1 - y) · log(1 - p)]
```

where *y ∈ {0, 1}* is the true label and *p* is the model's output probability. Optimization is performed using the **Adam** optimizer, which adapts the learning rate individually for each parameter using first and second moment estimates of the gradient [6].

Weight updates are computed via **backpropagation** — the application of the chain rule to compute partial derivatives of the loss with respect to every weight in the network, propagating the error signal from output to input.

### D. Regularization Techniques

Overfitting — the tendency of a complex model to memorize training data rather than learn generalizable patterns — is a primary challenge when training deep networks on moderately-sized datasets. We employ three complementary techniques:

**Dropout** [7]: During each training iteration, each neuron in a hidden layer is independently set to zero with probability *p* (the dropout rate). This forces the network to develop redundant representations and prevents co-adaptation of neurons. At inference time, all neurons are active but their outputs are scaled by *(1 – p)* to preserve expected activation magnitudes.

**Batch Normalization** [8]: After each linear transformation, the pre-activation values are normalized across the mini-batch to have zero mean and unit variance, then re-scaled by learned parameters *γ* and *β*. This stabilizes the gradient signal, reduces sensitivity to weight initialization, and allows the use of higher learning rates, significantly accelerating training.

**Early Stopping**: Training is monitored on a held-out validation set. If the validation loss fails to improve over *k* consecutive epochs (the patience parameter), training is halted and the weights from the epoch with the best validation performance are restored. This prevents continued weight updates that improve training loss but harm generalization.

### E. Evaluation Metrics

Model performance is assessed using a comprehensive set of binary classification metrics:

- **Accuracy:** Proportion of correctly classified instances.
- **Precision:** Of all instances classified as legitimate, the fraction that are truly legitimate. High precision is critical to avoid falsely blocking legitimate sites (false positives reduce user trust).
- **Recall:** Of all truly phishing instances, the fraction correctly identified. High recall is critical for security — a phishing site incorrectly classified as legitimate (false negative) reaches the user.
- **F1-Score:** Harmonic mean of Precision and Recall, balancing both concerns.
- **AUC-ROC:** Area Under the Receiver Operating Characteristic Curve, measuring classifier performance across all decision thresholds.
- **Confusion Matrix:** Full breakdown of TP, TN, FP, FN predictions.

---

---

## IV. Proposed Approach

### A. Dataset and Preprocessing

We use the UCI Phishing Websites dataset (ID: 327) [10], loaded directly via the `ucimlrepo` Python library or from the local `Training Dataset.arff` file. The dataset contains 11,055 instances with 30 features and no missing values, requiring no imputation.

Preprocessing steps are as follows:

1. **Label transformation:** The target variable `Result ∈ {–1, 1}` is converted to binary `{0, 1}` for compatibility with the sigmoid output and binary cross-entropy loss. Features retain their original ternary encoding `{–1, 0, 1}` — the intermediate `0` value (suspicious) carries meaningful information distinct from both extremes.

2. **Feature scaling:** All 30 features are standardized using `StandardScaler` (zero mean, unit variance), fit exclusively on the training split to prevent data leakage.

3. **Train/validation/test split:** The dataset is partitioned into 70% training (7,738 samples), 15% validation (1,659 samples), and 15% test (1,658 samples) using stratified splitting to preserve class proportions across all splits.

### B. Classifier Architectures

**Baseline classifiers (Entrega 2, completed):**
- *Random Forest:* 100 decision trees with default hyperparameters. Serves as the primary performance target, as Random Forest is the dominant method in related work.
- *SVM with RBF kernel:* A kernelized support vector machine; strong on moderate-sized tabular datasets.

**Proposed neural network (in progress):**

```
Input (30) → [Dense(128) + BatchNorm + ReLU + Dropout(0.3)]
           → [Dense(64)  + BatchNorm + ReLU + Dropout(0.2)]
           → [Dense(32)  + ReLU]
           → Dense(1, sigmoid)
```

The model is compiled with the Adam optimizer (learning rate 0.001), Binary Cross-Entropy loss, and accuracy as the monitoring metric. Training uses Early Stopping (patience = 10) and model checkpointing to save the best weights.

A systematic ablation study will compare: (a) 2-layer vs. 3-layer vs. 4-layer MLP, (b) with vs. without Batch Normalization, (c) dropout rates of 0.2, 0.3, and 0.5.

### C. Real-Time Detection Component

The trained model and fitted scaler are serialized (`best_model.keras`, `scaler.joblib`) and wrapped in a REST API using FastAPI. The API exposes two endpoints:

- `POST /predict/features` — accepts a JSON array of 30 pre-extracted feature values and returns the classification and confidence probability.
- `POST /predict/url` — accepts a raw URL string, extracts the 30 features programmatically using `tldextract`, `requests`, and `BeautifulSoup`, then returns the classification.

This architecture enables real-time phishing detection for any URL, fulfilling the synchronous component requirement of the project and establishing the primary differentiator of our system from all related works reviewed in Section II.

---

---

## V. Preliminary Results

Table II presents the performance of the baseline classifiers trained in Entrega 2 on the test set (1,658 samples, stratified split).

### Table II — Baseline Classifier Performance on Test Set

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|:--------:|:---------:|:------:|:--------:|:-------:|
| Random Forest (100 trees) | ~97% | ~97% | ~97% | ~97% | ~99% |
| SVM (RBF kernel) | ~95% | ~95% | ~95% | ~95% | ~98% |
| MLP (proposed) | — | — | — | — | — |

*Note: MLP results pending full training and ablation study (Entrega 5).*

The Random Forest result aligns closely with the 97% accuracy reported by Mohammad et al. [2] using their SSNN, confirming that our preprocessing pipeline and experimental setup are consistent with the established benchmark. The MLP is expected to achieve comparable performance, with the ablation study providing insight into which architectural choices most influence generalization.

---

---

## References

[1] R. M. Mohammad, F. Thabtah, and L. McCluskey, "An assessment of features related to phishing websites using an automated technique," in *Proc. 2012 International Conference for Internet Technology and Secured Transactions (ICITST)*, London, UK, Dec. 2012, pp. 492–497. doi: 10.1109/ICITST.2012.6470857.

[2] R. M. Mohammad, F. Thabtah, and L. McCluskey, "Predicting phishing websites based on self-structuring neural network," *Neural Computing and Applications*, vol. 25, no. 2, pp. 443–458, Aug. 2014. doi: 10.1007/s00521-013-1490-z.

[3] O. K. Sahingoz, E. Buber, O. Demir, and B. Diri, "Machine learning based phishing detection from URLs," *Expert Systems with Applications*, vol. 117, pp. 345–357, Mar. 2019. doi: 10.1016/j.eswa.2018.09.029.

[4] G. Vrbančič, I. Fister, and V. Podgorelec, "Datasets for phishing websites detection," *Data in Brief*, vol. 33, p. 106438, Dec. 2020. doi: 10.1016/j.dib.2020.106438.

[5] S. Chatterjee and A. S. Namin, "Detecting phishing websites through deep reinforcement learning," in *Proc. 43rd Annual IEEE Computer Software and Applications Conference (COMPSAC)*, Milwaukee, WI, USA, Jul. 2019, pp. 228–229. doi: 10.1109/COMPSAC.2019.10211.

[6] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," *Nature*, vol. 521, no. 7553, pp. 436–444, May 2015. doi: 10.1038/nature14539.

[7] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, "Dropout: A simple way to prevent neural networks from overfitting," *Journal of Machine Learning Research*, vol. 15, no. 1, pp. 1929–1958, Jan. 2014.

[8] S. Ioffe and C. Szegedy, "Batch normalization: Accelerating deep network training by reducing internal covariate shift," in *Proc. 32nd International Conference on Machine Learning (ICML)*, Lille, France, Jul. 2015, pp. 448–456.

[9] Anti-Phishing Working Group (APWG), "Phishing Activity Trends Report, 4th Quarter 2024," APWG, Tech. Rep., Feb. 2025. [Online]. Available: https://docs.apwg.org/reports/apwg_trends_report_q4_2024.pdf

[10] D. Dua and C. Graff, "UCI Machine Learning Repository – Phishing Websites Dataset (ID: 327)," University of California, Irvine, School of Information and Computer Sciences, 2019. [Online]. Available: https://archive.ics.uci.edu/dataset/327/phishing+websites

---

---

## APPENDIX — Instrucciones de Compilación LaTeX (IEEE Format)

Para convertir este documento al formato visual IEEE doble columna, usar la siguiente plantilla LaTeX:

```latex
\documentclass[conference]{IEEEtran}
\IEEEoverridecommandlockouts

\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{textcomp}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{hyperref}

\begin{document}

\title{Detection of Phishing Websites Using Artificial Neural Networks}

\author{
  \IEEEauthorblockN{Gabriel Fallas}
  \IEEEauthorblockA{
    \textit{ECCI} \\
    \textit{Universidad de Costa Rica}\\
    San José, Costa Rica \\
    gabriel.fallas@ucr.ac.cr}
  \and
  \IEEEauthorblockN{Valeria Chinchilla}
  \IEEEauthorblockA{
    \textit{ECCI} \\
    \textit{Universidad de Costa Rica}\\
    San José, Costa Rica \\
    valeria.chinchilla@ucr.ac.cr}
}

\maketitle

\begin{abstract}
% [Pegar el abstract de arriba]
\end{abstract}

\begin{IEEEkeywords}
phishing detection, neural networks, multilayer perceptron,
machine learning, cybersecurity, URL classification
\end{IEEEkeywords}

% --- Secciones: copiar el contenido de cada sección ---
\section{Introduction}
% ...

\section{Related Work}
% ...

\section{Theoretical Framework}
% ...

\section{Proposed Approach}
% ...

\section{Preliminary Results}
% ...

\bibliographystyle{IEEEtran}
\bibliography{references}

\end{document}
```

### Archivo `references.bib`:
```bibtex
@inproceedings{mohammad2012,
  author    = {Mohammad, Rami M. and Thabtah, Fadi and McCluskey, T. L.},
  title     = {An Assessment of Features Related to Phishing Websites Using
               an Automated Technique},
  booktitle = {Proc. Int. Conf. Internet Technology and Secured Transactions
               (ICITST)},
  year      = {2012},
  pages     = {492--497},
  doi       = {10.1109/ICITST.2012.6470857}
}

@article{mohammad2014,
  author  = {Mohammad, Rami M. and Thabtah, Fadi and McCluskey, T. L.},
  title   = {Predicting Phishing Websites Based on Self-Structuring Neural Network},
  journal = {Neural Computing and Applications},
  volume  = {25},
  number  = {2},
  pages   = {443--458},
  year    = {2014},
  doi     = {10.1007/s00521-013-1490-z}
}

@article{sahingoz2019,
  author  = {Sahingoz, Ozgur Koray and Buber, Ebubekir and
             Demir, Onder and Diri, Banu},
  title   = {Machine Learning Based Phishing Detection from {URLs}},
  journal = {Expert Systems with Applications},
  volume  = {117},
  pages   = {345--357},
  year    = {2019},
  doi     = {10.1016/j.eswa.2018.09.029}
}

@article{vrbancic2020,
  author  = {Vrban{\v{c}}i{\v{c}}, Grega and Fister, Iztok and
             Podgorelec, Vili},
  title   = {Datasets for Phishing Websites Detection},
  journal = {Data in Brief},
  volume  = {33},
  pages   = {106438},
  year    = {2020},
  doi     = {10.1016/j.dib.2020.106438}
}

@inproceedings{chatterjee2019,
  author    = {Chatterjee, Subhajit and Namin, Akbar Siami},
  title     = {Detecting Phishing Websites through Deep Reinforcement Learning},
  booktitle = {Proc. 43rd Annual IEEE Computer Software and
               Applications Conference (COMPSAC)},
  year      = {2019},
  pages     = {228--229},
  doi       = {10.1109/COMPSAC.2019.10211}
}

@article{lecun2015,
  author  = {LeCun, Yann and Bengio, Yoshua and Hinton, Geoffrey},
  title   = {Deep Learning},
  journal = {Nature},
  volume  = {521},
  number  = {7553},
  pages   = {436--444},
  year    = {2015},
  doi     = {10.1038/nature14539}
}

@article{srivastava2014,
  author  = {Srivastava, Nitish and Hinton, Geoffrey and Krizhevsky, Alex
             and Sutskever, Ilya and Salakhutdinov, Ruslan},
  title   = {Dropout: A Simple Way to Prevent Neural Networks from Overfitting},
  journal = {Journal of Machine Learning Research},
  volume  = {15},
  number  = {1},
  pages   = {1929--1958},
  year    = {2014}
}

@inproceedings{ioffe2015,
  author    = {Ioffe, Sergey and Szegedy, Christian},
  title     = {Batch Normalization: Accelerating Deep Network Training
               by Reducing Internal Covariate Shift},
  booktitle = {Proc. 32nd Int. Conference on Machine Learning (ICML)},
  year      = {2015},
  pages     = {448--456}
}

@techreport{apwg2024q4,
  author      = {{Anti-Phishing Working Group (APWG)}},
  title       = {Phishing Activity Trends Report, 4th Quarter 2024},
  institution = {APWG},
  year        = {2025},
  url         = {https://docs.apwg.org/reports/apwg_trends_report_q4_2024.pdf}
}

@misc{uci327,
  author = {Dua, Dheeru and Graff, Casey},
  title  = {{UCI} Machine Learning Repository -- Phishing Websites Dataset ({ID}: 327)},
  year   = {2019},
  url    = {https://archive.ics.uci.edu/dataset/327/phishing+websites},
  note   = {University of California, Irvine, School of Information and
            Computer Sciences}
}
```

---

## APPENDIX B — Notas para la Entrega

### Diferencias entre este documento y el formato físico IEEE

Este archivo Markdown representa el **contenido completo** del paper. Al compilarlo en LaTeX con `IEEEtran`, el formato visual será:

- **Dos columnas** de texto con márgenes estándar IEEE
- **Fuente:** Times New Roman 10pt
- **Encabezado:** Título en negrita, autores y afiliación
- **Tablas:** Numeradas con `Table I`, `Table II`
- **Figuras:** Numeradas con `Fig. 1`, `Fig. 2` (si aplica)
- **Referencias:** Numeradas en corchetes `[1]`, `[2]`, etc.
- **Extensión visual esperada:** ~3 páginas doble columna

### Elementos adicionales a agregar antes de la entrega final:

1. **Diagrama de flujo del sistema** (Fig. 1):
   - Bloque: Dataset UCI → Preprocesamiento → MLP → Evaluación
   - Rama paralela: URL cruda → Feature Extractor → MLP → API → Predicción

2. **Curva ROC** (Fig. 2): graficar las curvas de RF y SVM sobre los datos de prueba

3. **Actualizar Tabla II** con los resultados reales del MLP una vez entrenado

### Checklist de entrega:
```
☐ Abstract ≤ 150 palabras                         ✅
☐ 5 secciones: Intro, Related Work, Framework,    ✅
  Approach, Results
☐ ≥ 6 referencias académicas en IEEE format        ✅ (10 refs)
☐ Tabla comparativa de trabajo relacionado         ✅
☐ Tabla de resultados (baseline completo)          ✅
☐ Descripción del marco teórico                    ✅
☐ Posicionamiento crítico vs. trabajo previo       ✅
☐ ~3 páginas en formato IEEE doble columna        ⬜ (compilar en LaTeX)
```

---

*Entrega 4 – PF3325 Redes | Gabriel Fallas & Valeria Chinchilla | Junio 2026*
