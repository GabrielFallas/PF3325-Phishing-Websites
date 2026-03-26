# Source Code Directory

This directory contains the Python source code for the phishing detection system.

## Modules

### `preprocess.py`

Data preprocessing pipeline:

- Load dataset from UCI or local .arff file
- Feature scaling with StandardScaler
- Train/validation/test splitting
- Label encoding
- Data serialization

### `model.py`

Neural network architecture definitions:

- MLP model with configurable layers
- Custom model architectures
- Model building utilities
- Layer configurations

### `train.py`

Training script:

- Command-line interface for training
- Model training loop
- Callbacks configuration (EarlyStopping, ModelCheckpoint)
- Hyperparameter management
- Training history logging

### `evaluate.py`

Model evaluation and metrics:

- Test set evaluation
- Metrics calculation (Accuracy, Precision, Recall, F1, AUC-ROC)
- Confusion matrix generation
- ROC curve plotting
- Classification report
- Visualization utilities

### `feature_extractor.py`

Real-time feature extraction from URLs:

- Extract 30 features from raw URLs
- Implements feature extraction rules from Mohammad et al. (2012, 2014)
- URL parsing and analysis
- HTTPS/SSL checks
- Domain age and reputation queries
- HTML/JavaScript analysis

### `api_phishing.py`

FastAPI REST API for real-time detection:

- POST endpoint for prediction
- Model loading and inference
- Request/response schemas
- API documentation (Swagger/OpenAPI)
- Error handling

## Usage

### Training a Model

```bash
python src/train.py --epochs 100 --batch-size 64
```

### Evaluating a Model

```bash
python src/evaluate.py --model-path models/best_model.keras
```

### Running the API

```bash
uvicorn src.api_phishing:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/docs` for interactive API documentation.

## Development

- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Add docstrings to all functions and classes
- Write unit tests for critical functions (future work)

## Dependencies

All required packages are listed in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

