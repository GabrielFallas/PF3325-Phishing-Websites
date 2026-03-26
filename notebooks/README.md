# Notebooks Directory

This directory contains Jupyter notebooks for exploratory data analysis, model development, and experimentation.

## Notebooks

1. **`01_eda.ipynb`** - Exploratory Data Analysis
   - Dataset overview and statistics
   - Feature distribution analysis
   - Correlation heatmap
   - Class balance visualization
   - Detection of outliers
2. **`02_preprocessing.ipynb`** - Data Preprocessing
   - Data cleaning (if needed)
   - Feature scaling with StandardScaler
   - Train/validation/test split (70%/15%/15%)
   - Label encoding (convert {-1, 1} to {0, 1})
3. **`03_model_training.ipynb`** - Neural Network Training
   - Model architecture definition
   - Training loop with callbacks
   - Learning curves visualization
   - Model checkpoint saving
4. **`04_experiments.ipynb`** - Architecture Comparison & Ablation Study
   - Comparison of different MLP architectures
   - Hyperparameter tuning experiments
   - Baseline models (Random Forest, SVM)
   - Ablation study (Dropout, BatchNorm effects)
5. **`05_evaluation.ipynb`** - Final Evaluation & Metrics
   - Test set evaluation
   - Confusion matrix
   - ROC curve and AUC
   - Detailed classification report
   - Error analysis

## Usage

To run the notebooks:

1. Ensure all dependencies are installed:

   ```bash
   pip install -r requirements.txt
   ```

2. Start Jupyter:

   ```bash
   jupyter notebook
   ```

   or

   ```bash
   jupyter lab
   ```

3. Open the notebooks in sequential order (01 → 02 → 03 → 04 → 05)

## Notes

- Notebooks are designed to be run in sequence
- Results and figures are saved to `reports/` directory
- Trained models are saved to `models/` directory
- Use GPU acceleration if available for faster training

