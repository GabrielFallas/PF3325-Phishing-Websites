# Phishing Website Detection using Neural Networks

> **Course:** PF3325 – Redes  
> **Dataset:** [UCI ML Repository – Phishing Websites (ID: 327)](https://archive.ics.uci.edu/dataset/327/phishing+websites)  
> **Status:** 🚧 In Development
> **Students:** Gabriel Fallas - Valeria Chinchilla

## 📋 Overview

This project implements an automated phishing website detection system using Artificial Neural Networks (ANN) and supervised learning techniques on the UCI Phishing Websites dataset. The system includes both offline classification and a real-time detection component via REST API.

### Key Features

- ✅ Complete ML pipeline: data loading → preprocessing → training → evaluation
- ✅ Multi-Layer Perceptron (MLP) architecture with regularization techniques
- ✅ Comprehensive exploratory data analysis (EDA)
- ✅ Real-time phishing detection via FastAPI REST API
- ✅ Comparative analysis with baseline ML models (Random Forest, SVM)

## 📚 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) directory:

- **[Project Plan](docs/PLAN_PROYECTO.md)** - Detailed project plan with deliverables, architecture, and methodology (Spanish)
- **[Setup Guide](docs/SETUP_COMPLETE.md)** - Complete setup checklist and next steps
- **[GitHub Setup](docs/GITHUB_SETUP.md)** - Step-by-step guide to push this project to GitHub
- **[Contributing](docs/CONTRIBUTING.md)** - Code style guidelines, git workflow, and contribution rules

## 🎯 Project Objectives

1. Process and prepare the UCI Phishing Websites dataset (30 features, 11,055 instances)
2. Train a neural network capable of classifying URLs as legitimate or phishing
3. Extend the system to real-time detection (synchronous classification)

## 📊 Dataset

- **Source:** UCI Machine Learning Repository – Phishing Websites (ID: 327)
- **Instances:** 11,055 samples
- **Features:** 30 automatically extracted attributes (ternary encoding: {-1, 0, 1})
- **Target:** `Result` → `-1` (phishing) / `1` (legitimate)

### Feature Categories

The dataset contains 30 features organized in 4 categories (Mohammad et al., 2012, 2014):

| Category                    | Description                    | Features    |
| --------------------------- | ------------------------------ | ----------- |
| **Address Bar based**       | URL and domain characteristics | 12 features |
| **Abnormal based**          | Abnormal behavior indicators   | 6 features  |
| **HTML & JavaScript based** | Client-side code analysis      | 5 features  |
| **Domain based**            | Domain reputation metrics      | 7 features  |

## 🏗️ Project Structure

```
phishing-detection-pf3325/
│
├── data/                              # Dataset files
│   ├── Training Dataset.arff          # Original UCI dataset (11,055 instances, 30 features)
│   ├── README.md                      # Dataset documentation
│   └── processed/                     # Preprocessed data (not tracked)
│
├── src/                               # Source code
│   ├── preprocess.py                  # Preprocessing pipeline
│   ├── model.py                       # Neural network architecture
│   ├── train.py                       # MLP training script
│   ├── train_sklearn.py               # RF / SVM baseline training
│   ├── evaluate.py                    # MLP evaluation + figures
│   ├── compare_models.py              # RF/SVM/MLP comparison + metrics.json + ROC
│   ├── make_figures.py                # Architecture & pipeline diagrams
│   ├── feature_extractor.py           # Real-time feature extraction from URLs
│   ├── api_phishing.py                # FastAPI REST API + web demo
│   ├── demo.py                        # Console demo (Entrega 2)
│   └── README.md                      # Source code documentation
│
├── models/                            # Trained models (not tracked)
│   ├── best_model.keras               # Best trained model
│   ├── scaler.joblib                  # Fitted StandardScaler
│   └── README.md                      # Model persistence documentation
│
├── reports/                           # Academic deliverables
│   ├── entrega4_contexto.pdf          # IEEE 3-page paper (due June 3, 2026)
│   ├── entrega6_final.pdf             # IEEE 6-page final paper (due July 5, 2026)
│   └── README.md                      # Reports documentation
│
├── docs/                              # Documentation directory
│   ├── README.md                      # Docs index & navigation
│   ├── PLAN_PROYECTO.md               # Detailed project plan (Spanish)
│   ├── CONTRIBUTING.md                # Contribution guidelines
│   ├── GITHUB_SETUP.md                # GitHub setup tutorial
│   ├── SETUP_COMPLETE.md              # Setup completion guide
│   │
│   └── entregables/                   # Course deliverables (Entregas 2-6)
│       ├── entrega2/                  # Delivery 2: Video + Baseline Models
│       │   ├── README.md
│       │   └── entrega2_video_script.md
│       │
│       ├── entrega3/                  # Delivery 3: Class Presentation (May 27, 2026)
│       │   ├── README.md
│       │   ├── ENTREGA3_PRESENTACION.md       # Complete presentation guide (script + notes)
│       │   ├── presentacion.html              # Interactive HTML presentation [NEW]
│       │   ├── SCRIPT_PRESENTACION.md         # Detailed presenter script with timing [NEW]
│       │   └── CHECKLIST.md
│       │
│       ├── entrega4/                  # Delivery 4: IEEE Paper (~3 pages, June 3, 2026)
│       │   ├── README.md
│       │   └── ENTREGA4_IEEE_PAPER.md         # Complete IEEE paper draft
│       │
│       ├── entrega5/                  # Delivery 5: Final presentation (July 1, 2026)
│       │   ├── README.md
│       │   ├── presentacion.html              # Interactive 13-slide deck
│       │   ├── SCRIPT_PRESENTACION.md         # Presenter script with timing
│       │   └── figures/
│       │
│       └── entrega6/                  # Delivery 6: Final IEEE paper (6 pages, July 5, 2026)
│           ├── README.md
│           ├── main.tex                       # Compilable IEEEtran paper
│           ├── references.bib
│           └── figures/
│
├── .gitignore                         # Files to ignore in git
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## 🚀 Quick Start

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/phishing-detection-pf3325.git
cd phishing-detection-pf3325
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Dataset Loading

You can load the dataset in two ways:

**Option 1: From UCI Repository (requires internet)**

```python
from ucimlrepo import fetch_ucirepo

phishing_websites = fetch_ucirepo(id=327)
X = phishing_websites.data.features
y = phishing_websites.data.targets
```

**Option 2: From local .arff file**

```python
from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff('data/Training Dataset.arff')
df = pd.DataFrame(data)
```

### Training the Model

```bash
python src/train.py
```

### Running the Real-Time API

```bash
uvicorn src.api_phishing:app --reload
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for interactive API documentation.

## 🧪 Model Architecture

The neural network uses the following architecture:

- **Input Layer:** 30 features
- **Hidden Layer 1:** 128 neurons (ReLU + BatchNorm + Dropout 0.3)
- **Hidden Layer 2:** 64 neurons (ReLU + BatchNorm + Dropout 0.2)
- **Hidden Layer 3:** 32 neurons (ReLU)
- **Output Layer:** 1 neuron (Sigmoid)

**Training Configuration:**

- Optimizer: Adam
- Loss: Binary Crossentropy
- Metrics: Accuracy, Precision, Recall, F1-Score, AUC-ROC
- Callbacks: Early Stopping (patience=10), ModelCheckpoint

## 📈 Results

Test set: 1,659 samples (15%, stratified). Numbers from `reports/metrics.json`.

| Model              | Accuracy | Precision | Recall    | F1-Score | AUC-ROC |
| ------------------ | -------- | --------- | --------- | -------- | ------- |
| Random Forest      | 0.972    | 0.969     | 0.981     | 0.975    | 0.996   |
| SVM (RBF)          | 0.946    | 0.935     | 0.971     | 0.953    | 0.987   |
| **MLP (proposed)** | 0.965    | 0.951     | **0.988** | 0.969    | 0.994   |

The MLP attains the **highest recall (98.8%)** — the decisive metric for a
security filter — missing only 11 phishing sites out of 924 on the test set.

## 🔬 Methodology

### Data Preprocessing

1. **Label Encoding:** Convert target from {-1, 1} to {0, 1} for sigmoid output
2. **Feature Scaling:** StandardScaler on ternary feature values {-1, 0, 1}
3. **Train/Val/Test Split:** 70% / 15% / 15% (stratified)

**Important:** Features are NOT converted to binary. The value `0` (suspicious) contains valid information distinct from `-1` and `1`.

### Evaluation Metrics

- Accuracy, Precision, Recall, F1-Score
- ROC Curve and AUC
- Confusion Matrix
- Classification Report

## 🌐 Real-Time Detection API

The system includes a FastAPI-based REST API (`src/api_phishing.py`) for
real-time phishing detection, plus an interactive web demo at `GET /`.

```bash
uvicorn src.api_phishing:app --reload   # open http://localhost:8000
```

### Endpoints

| Method & path           | Purpose                                            |
| ----------------------- | -------------------------------------------------- |
| `GET  /`                | Interactive web demo (paste a URL, get a verdict)  |
| `GET  /health`          | Liveness + model metadata                          |
| `POST /predict/features`| Score a pre-extracted 30-feature vector            |
| `POST /predict/url`     | Extract features from a raw URL and classify it    |

**`POST /predict/url`**

```json
// Request
{ "url": "https://www.github.com" }

// Response
{
  "prediction": "Legitimate",
  "label": "Legítimo",
  "is_phishing": false,
  "confidence": 0.99,
  "p_phishing": 0.0,
  "info": { "registered_domain": "github.com", "n_measured": 24, "n_default": 6 },
  "features": { "having_IP_Address": { "value": 1, "source": "measured" }, "...": {} }
}
```

> **Note on real-time extraction.** `feature_extractor.py` computes ~24/30
> features live (URL string, TLS handshake, HTML/JS parsing, DNS, WHOIS). Six
> features (`web_traffic`/Alexa, `Page_Rank`, `Links_pointing_to_page`,
> `Google_Index`, `Statistical_report`) rely on services that are now defunct or
> paid-only, so they fall back to a neutral default; each response reports the
> per-feature `source` (`measured` vs `default`).

## 📚 References

1. Mohammad, R. M., Thabtah, F., & McCluskey, L. (2012). _An assessment of features related to phishing websites using an automated technique_. ICITST-2012.
2. Mohammad, R. M., Thabtah, F., & McCluskey, L. (2014). _Predicting phishing websites based on self-structuring neural network_. Neural Computing and Applications.
3. UCI Machine Learning Repository: Phishing Websites Dataset. https://archive.ics.uci.edu/dataset/327/phishing+websites

## 📅 Project Timeline

| Phase | Deliverable                                           | Date          | Status        |
| ----- | ----------------------------------------------------- | ------------- | ------------- |
| 1     | Project proposal meeting                              | April 8, 2026 | ✅ Completed  |
| 2     | Demo video (8-12 min) + Baseline models               | May 6, 2026   | ✅ Completed  |
| 3     | Class presentation (motivation, related work, theory) | May 27, 2026  | ✅ Completed|
| 4     | IEEE paper (~3 pages)                                 | June 3, 2026  | ✅ Completed  |
| 5     | Final presentation (implementation + real-time API)   | July 1, 2026  | ✅ Completed  |
| 6     | Final IEEE paper (6 pages)                            | July 5, 2026  | ✅ Completed  |

## 👥 Contributors

- Gabriel Fallas
- Valeria Chinchilla

---

**Keywords:** phishing detection, neural networks, machine learning, cybersecurity, deep learning, FastAPI
