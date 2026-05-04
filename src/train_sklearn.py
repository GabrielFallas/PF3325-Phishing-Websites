"""
Quick training script with scikit-learn for Entrega 2 demo.
Uses Random Forest and SVM for fast results.
"""

import sys
import pickle
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
)
import numpy as np

from preprocess import preprocess_data, save_preprocessing


def train_sklearn_models(X_train, X_val, y_train, y_val):
    """
    Train sklearn models for quick evaluation.
    """
    print("=" * 60)
    print("TRAINING SCIKIT-LEARN MODELS")
    print("=" * 60)
    
    # Random Forest
    print("\n1. Training Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    
    rf_pred = rf_model.predict(X_val)
    rf_acc = accuracy_score(y_val, rf_pred)
    print(f"   ✓ Random Forest Validation Accuracy: {rf_acc:.4f}")
    
    # SVM
    print("\n2. Training SVM (RBF kernel)...")
    svm_model = SVC(kernel='rbf', probability=True, random_state=42)
    svm_model.fit(X_train, y_train)
    
    svm_pred = svm_model.predict(X_val)
    svm_acc = accuracy_score(y_val, svm_pred)
    print(f"   ✓ SVM Validation Accuracy: {svm_acc:.4f}")
    
    # Save models
    Path('models').mkdir(exist_ok=True)
    pickle.dump(rf_model, open('models/random_forest_model.pkl', 'wb'))
    pickle.dump(svm_model, open('models/svm_model.pkl', 'wb'))
    print("\n✓ Models saved to models/")
    
    return rf_model, svm_model


def main():
    # Load and preprocess data
    print("Loading and preprocessing data...")
    X_train, X_val, X_test, y_train, y_val, y_test, scaler, features = preprocess_data()
    
    # Save preprocessing artifacts
    save_preprocessing(scaler, features)
    
    # Train models
    rf_model, svm_model = train_sklearn_models(X_train, X_val, y_train, y_val)
    
    # Evaluate on test set
    print("\n" + "=" * 60)
    print("EVALUATION ON TEST SET")
    print("=" * 60)
    
    print("\nRandom Forest:")
    rf_pred = rf_model.predict(X_test)
    rf_proba = rf_model.predict_proba(X_test)[:, 1]
    print(f"  Accuracy:  {accuracy_score(y_test, rf_pred):.4f}")
    print(f"  Precision: {precision_score(y_test, rf_pred):.4f}")
    print(f"  Recall:    {recall_score(y_test, rf_pred):.4f}")
    print(f"  F1-Score:  {f1_score(y_test, rf_pred):.4f}")
    print(f"  AUC-ROC:   {roc_auc_score(y_test, rf_proba):.4f}")
    
    print("\nSVM:")
    svm_pred = svm_model.predict(X_test)
    svm_proba = svm_model.predict_proba(X_test)[:, 1]
    print(f"  Accuracy:  {accuracy_score(y_test, svm_pred):.4f}")
    print(f"  Precision: {precision_score(y_test, svm_pred):.4f}")
    print(f"  Recall:    {recall_score(y_test, svm_pred):.4f}")
    print(f"  F1-Score:  {f1_score(y_test, svm_pred):.4f}")
    print(f"  AUC-ROC:   {roc_auc_score(y_test, svm_proba):.4f}")
    
    print("\n" + "=" * 60)
    print("✓ TRAINING COMPLETE")
    print("=" * 60)


if __name__ == '__main__':
    main()
