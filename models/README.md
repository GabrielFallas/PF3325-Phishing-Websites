# Models Directory

This directory stores trained machine learning models and preprocessing artifacts.

## Contents

- `best_model.keras` - Best performing neural network model (saved using Keras format)
- `scaler.joblib` - Fitted StandardScaler for feature normalization
- Other model checkpoints and artifacts generated during training

## Important Notes

⚠️ **This directory is excluded from git** (see `.gitignore`) due to:

- Large file sizes (models can be >100MB)
- Binary format not suitable for version control
- Can be regenerated from source code and data

## Model Persistence

### Saving Models

```python
# Save Keras model
model.save('models/best_model.keras')

# Save scaler
import joblib
joblib.dump(scaler, 'models/scaler.joblib')
```

### Loading Models

```python
import tensorflow as tf
import joblib

# Load Keras model
model = tf.keras.models.load_model('models/best_model.keras')

# Load scaler
scaler = joblib.load('models/scaler.joblib')
```

## Model Versioning

For proper model versioning in production, consider:

- Using MLflow or Weights & Biases for experiment tracking
- Storing models in cloud storage (S3, GCS, Azure Blob)
- Including model metadata (hyperparameters, metrics, training date)
- Semantic versioning for model releases

## Regenerating Models

To train a new model:

```bash
python src/train.py
```

The training script will automatically save the best model to this directory.

