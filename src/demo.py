"""
Demonstration script for phishing detection system (Entrega 2).
Shows dataset overview, classifier design, and sample predictions.
"""

import sys
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    confusion_matrix, classification_report, roc_curve, roc_auc_score
)

from preprocess import preprocess_data, load_dataset, encode_target, load_preprocessing


def show_dataset_overview():
    """Display dataset information and exploratory analysis."""
    print("\n" + "=" * 70)
    print("📊 DATASET OVERVIEW")
    print("=" * 70)
    
    X, y, features = load_dataset()
    y = encode_target(y)
    
    print(f"\n✓ Dataset: UCI Phishing Websites (ID: 327)")
    print(f"✓ Source: https://archive.ics.uci.edu/dataset/327/phishing+websites")
    print(f"\nDataset Statistics:")
    print(f"  Total samples:     {len(X):,}")
    print(f"  Total features:    {len(features)}")
    print(f"  Phishing sites:    {int((y==0).sum()):,} ({100*((y==0).sum())/len(y):.1f}%)")
    print(f"  Legitimate sites:  {int((y==1).sum()):,} ({100*((y==1).sum())/len(y):.1f}%)")
    
    print(f"\nFeature Categories (4 categories, 30 features):")
    print(f"  • Address Bar based:       12 features (URL, domain characteristics)")
    print(f"  • Abnormal based:           6 features (behavior indicators)")
    print(f"  • HTML & JavaScript based:  5 features (client-side code)")
    print(f"  • Domain based:             7 features (reputation metrics)")
    
    print(f"\nFirst 12 Features (Address Bar based):")
    for i in range(12):
        print(f"  {i+1:2d}. {features[i]}")
    
    print(f"\nFeature Values:")
    print(f"  Ternary Encoding: -1 (Phishing), 0 (Suspicious), 1 (Legitimate)")
    print(f"  Example sample:")
    print(X.iloc[0].to_string())


def show_classifier_design():
    """Display classifier design."""
    print("\n" + "=" * 70)
    print("🧠 CLASSIFIER DESIGN")
    print("=" * 70)
    
    print("\nApproach: Ensemble Methods & Support Vector Machines")
    print("\nClassifier 1: Random Forest")
    print("  • 100 decision trees in ensemble")
    print("  • Bagging approach for robustness")
    print("  • Handles non-linearity and feature interactions")
    print("  • Fast inference")
    
    print("\nClassifier 2: Support Vector Machine (SVM)")
    print("  • RBF (Radial Basis Function) kernel")
    print("  • Finds optimal hyperplane for separation")
    print("  • Handles high-dimensional feature space")
    print("  • Effective for binary classification")
    
    print("\nPreprocessing Pipeline:")
    print("  1. Load ARFF dataset (11,055 samples)")
    print("  2. Encode target: {-1, 1} → {0, 1}")
    print("  3. Standardize features (mean=0, std=1)")
    print("  4. Split: 70% train / 15% validation / 15% test")
    
    print("\nEvaluation Metrics:")
    print("  • Accuracy: Overall correctness")
    print("  • Precision: (TP / (TP + FP)) - Avoid false positives")
    print("  • Recall: (TP / (TP + FN)) - Catch real phishing")
    print("  • F1-Score: Harmonic mean of precision & recall")
    print("  • AUC-ROC: Area under ROC curve (0-1, 1=perfect)")


def show_sample_predictions():
    """Show predictions on test samples."""
    print("\n" + "=" * 70)
    print("🔍 SAMPLE PREDICTIONS")
    print("=" * 70)
    
    # Load data
    _, _, X_test, _, _, y_test, _, _ = preprocess_data()
    
    # Load models
    try:
        rf_model = pickle.load(open('models/random_forest_model.pkl', 'rb'))
        svm_model = pickle.load(open('models/svm_model.pkl', 'rb'))
    except FileNotFoundError:
        print("\n⚠️  Models not found!")
        print("Run: python src/train_sklearn.py")
        return
    
    # Show first 10 test samples
    print(f"\nShowing 10 predictions from test set:")
    print("-" * 90)
    print(f"{'#':>2s} {'True':>12s} {'RF Pred':>12s} {'SVM Pred':>12s} {'Match':>8s}")
    print("-" * 90)
    
    for i in range(min(10, len(X_test))):
        x_sample = X_test[i:i+1]
        y_true = y_test[i]
        
        # Predictions
        rf_pred = rf_model.predict(x_sample)[0]
        svm_pred = svm_model.predict(x_sample)[0]
        
        # Format
        true_label = "Legitimate" if y_true == 1 else "Phishing"
        rf_label = "Legitimate" if rf_pred == 1 else "Phishing"
        svm_label = "Legitimate" if svm_pred == 1 else "Phishing"
        
        match = "✓" if (rf_pred == y_true and svm_pred == y_true) else "✗"
        
        print(f"{i+1:2d} {true_label:>12s} {rf_label:>12s} {svm_label:>12s} {match:>8s}")


def show_model_evaluation():
    """Show complete model evaluation."""
    print("\n" + "=" * 70)
    print("📈 MODEL EVALUATION (TEST SET)")
    print("=" * 70)
    
    # Load data
    _, _, X_test, _, _, y_test, _, _ = preprocess_data()
    
    # Load models
    try:
        rf_model = pickle.load(open('models/random_forest_model.pkl', 'rb'))
        svm_model = pickle.load(open('models/svm_model.pkl', 'rb'))
    except FileNotFoundError:
        print("\n⚠️  Models not found!")
        return
    
    # Evaluate both models
    for model_name, model in [("Random Forest", rf_model), ("SVM", svm_model)]:
        print(f"\n{model_name}:")
        print("-" * 70)
        
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]
        
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_proba)
        
        print(f"  Accuracy:    {acc:.4f} ({int(acc * len(y_test))}/{len(y_test)} correct)")
        print(f"  Precision:   {prec:.4f} (catch phishing correctly)")
        print(f"  Recall:      {rec:.4f} (find all phishing sites)")
        print(f"  F1-Score:    {f1:.4f}")
        print(f"  AUC-ROC:     {auc:.4f}")
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        tn, fp, fn, tp = cm.ravel()
        print(f"\n  Confusion Matrix:")
        print(f"    True Negatives:  {tn:4d}  |  False Positives: {fp:4d}")
        print(f"    False Negatives: {fn:4d}  |  True Positives:  {tp:4d}")


def generate_visualizations():
    """Generate and save visualization plots."""
    print("\n" + "=" * 70)
    print("📊 GENERATING VISUALIZATIONS")
    print("=" * 70)
    
    # Load data
    _, _, X_test, _, _, y_test, _, _ = preprocess_data()
    
    # Load models
    try:
        rf_model = pickle.load(open('models/random_forest_model.pkl', 'rb'))
    except FileNotFoundError:
        print("⚠️  Model not found!")
        return
    
    Path('reports').mkdir(exist_ok=True)
    
    y_pred = rf_model.predict(X_test)
    y_proba = rf_model.predict_proba(X_test)[:, 1]
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Phishing', 'Legitimate'],
                yticklabels=['Phishing', 'Legitimate'],
                cbar_kws={'label': 'Count'})
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix - Random Forest Classifier')
    plt.tight_layout()
    plt.savefig('reports/confusion_matrix.png', dpi=150, bbox_inches='tight')
    print("✓ Saved: reports/confusion_matrix.png")
    plt.close()
    
    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc = roc_auc_score(y_test, y_proba)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, 'b-', linewidth=2.5, label=f'Random Forest (AUC={auc:.4f})')
    plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
    plt.xlabel('False Positive Rate', fontsize=11)
    plt.ylabel('True Positive Rate', fontsize=11)
    plt.title('ROC Curve - Phishing Detection', fontsize=12)
    plt.legend(loc='lower right', fontsize=10)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('reports/roc_curve.png', dpi=150, bbox_inches='tight')
    print("✓ Saved: reports/roc_curve.png")
    plt.close()


def main():
    """Run complete demonstration."""
    print("\n" + "=" * 70)
    print("🎬 ENTREGA 2 - PHISHING DETECTION SYSTEM DEMONSTRATION")
    print("=" * 70)
    print("\nThis demonstration shows:")
    print("  1. Dataset overview and statistics")
    print("  2. Classifier design and architecture")
    print("  3. Sample predictions")
    print("  4. Model evaluation metrics")
    
    # Run all sections
    show_dataset_overview()
    show_classifier_design()
    show_sample_predictions()
    show_model_evaluation()
    generate_visualizations()
    
    print("\n" + "=" * 70)
    print("✓ DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nGenerated files for presentation:")
    print("  • reports/confusion_matrix.png")
    print("  • reports/roc_curve.png")


if __name__ == '__main__':
    main()
