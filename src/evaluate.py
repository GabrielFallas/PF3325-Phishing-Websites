"""
Model evaluation and metrics visualization.
"""

import sys
import json
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    confusion_matrix, classification_report, roc_curve, auc, roc_auc_score
)
import tensorflow as tf

from preprocess import preprocess_data


def evaluate_model(model, X_test, y_test, threshold=0.5):
    """
    Evaluate model on test set.
    
    Args:
        model: Trained Keras model
        X_test: Test features
        y_test: Test labels
        threshold: Classification threshold (default 0.5)
    
    Returns:
        Dictionary with metrics
    """
    # Get predictions
    y_pred_proba = model.predict(X_test, verbose=0)
    y_pred = (y_pred_proba >= threshold).astype(int).flatten()
    
    # Calculate metrics
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    metrics = {
        'accuracy': (tp + tn) / (tp + tn + fp + fn),
        'precision': tp / (tp + fp) if (tp + fp) > 0 else 0,
        'recall': tp / (tp + fn) if (tp + fn) > 0 else 0,
        'specificity': tn / (tn + fp) if (tn + fp) > 0 else 0,
        'f1': 2 * tp / (2 * tp + fp + fn) if (2 * tp + fp + fn) > 0 else 0,
        'auc_roc': roc_auc_score(y_test, y_pred_proba),
        'confusion_matrix': cm.tolist(),
        'tp': int(tp),
        'tn': int(tn),
        'fp': int(fp),
        'fn': int(fn)
    }
    
    return metrics, y_pred, y_pred_proba


def print_metrics(metrics):
    """Pretty print metrics."""
    print("\n" + "=" * 50)
    print("EVALUATION METRICS")
    print("=" * 50)
    print(f"Accuracy:    {metrics['accuracy']:.4f}")
    print(f"Precision:   {metrics['precision']:.4f}")
    print(f"Recall:      {metrics['recall']:.4f}")
    print(f"Specificity: {metrics['specificity']:.4f}")
    print(f"F1-Score:    {metrics['f1']:.4f}")
    print(f"AUC-ROC:     {metrics['auc_roc']:.4f}")
    
    print("\nConfusion Matrix:")
    cm = np.array(metrics['confusion_matrix'])
    print(f"  TN={metrics['tn']:4d}  FP={metrics['fp']:4d}")
    print(f"  FN={metrics['fn']:4d}  TP={metrics['tp']:4d}")
    print("=" * 50)


def plot_confusion_matrix(cm, save_path='reports/confusion_matrix.png'):
    """Plot confusion matrix."""
    Path(save_path).parent.mkdir(exist_ok=True)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Phishing', 'Legitimate'],
                yticklabels=['Phishing', 'Legitimate'])
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix - Phishing Detection')
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"✓ Confusion matrix saved to {save_path}")
    plt.close()


def plot_roc_curve(y_test, y_pred_proba, auc_score, save_path='reports/roc_curve.png'):
    """Plot ROC curve."""
    Path(save_path).parent.mkdir(exist_ok=True)
    
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, 'b-', linewidth=2, label=f'ROC (AUC={auc_score:.4f})')
    plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve - Phishing Detection')
    plt.legend(loc='lower right')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"✓ ROC curve saved to {save_path}")
    plt.close()


def plot_training_history(history_path, save_path='reports/training_history.png'):
    """Plot training history from saved JSON."""
    Path(save_path).parent.mkdir(exist_ok=True)
    
    with open(history_path, 'r') as f:
        history = json.load(f)
    
    # Plot loss
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
    
    ax1.plot(history['loss'], label='Train Loss')
    ax1.plot(history['val_loss'], label='Val Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.set_title('Training Loss')
    ax1.legend()
    ax1.grid(alpha=0.3)
    
    # Plot accuracy
    ax2.plot(history['accuracy'], label='Train Accuracy')
    ax2.plot(history['val_accuracy'], label='Val Accuracy')
    ax2.plot(history['auc'], label='Train AUC')
    ax2.plot(history['val_auc'], label='Val AUC')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Score')
    ax2.set_title('Training Accuracy & AUC')
    ax2.legend()
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"✓ Training history plot saved to {save_path}")
    plt.close()


def main():
    # Load data
    print("Loading data...")
    _, _, X_test, _, _, y_test, _, _ = preprocess_data()
    
    # Load model
    model_path = 'models/best_model.keras'
    if not Path(model_path).exists():
        print(f"ERROR: Model not found at {model_path}")
        print("Please train the model first: python src/train.py")
        sys.exit(1)
    
    print(f"Loading model from {model_path}...")
    model = tf.keras.models.load_model(model_path)
    
    # Evaluate
    print("\nEvaluating model on test set...")
    metrics, y_pred, y_pred_proba = evaluate_model(model, X_test, y_test)
    print_metrics(metrics)
    
    # Plot results
    print("\nGenerating visualizations...")
    plot_confusion_matrix(np.array(metrics['confusion_matrix']))
    plot_roc_curve(y_test, y_pred_proba, metrics['auc_roc'])
    
    # Plot training history if available
    history_path = 'models/training_history.json'
    if Path(history_path).exists():
        plot_training_history(history_path)


if __name__ == '__main__':
    main()
