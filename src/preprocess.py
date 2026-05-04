"""
Data preprocessing pipeline for phishing detection.
Loads, preprocesses, and prepares the UCI Phishing Websites dataset.
"""

import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path


def load_dataset(arff_path='data/Training_Dataset.arff'):
    """
    Load the UCI Phishing Websites dataset from ARFF file.
    
    Args:
        arff_path: Path to the .arff file
    
    Returns:
        X: Feature matrix (pandas DataFrame)
        y: Target vector (pandas Series)
        feature_names: List of feature names
    """
    # Load ARFF file
    data, meta = arff.loadarff(arff_path)
    df = pd.DataFrame(data)
    
    # Convert bytes to strings
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].str.decode('utf-8')
    
    # Separate features and target
    target_col = 'Result'
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Convert to numeric
    X = X.astype(float)
    y = y.astype(float)
    
    return X, y, list(X.columns)


def encode_target(y):
    """
    Convert target from {-1, 1} to {0, 1} for binary classification.
    -1 (phishing) -> 0
    1 (legitimate) -> 1
    
    Args:
        y: Target vector with values {-1, 1}
    
    Returns:
        y_encoded: Target vector with values {0, 1}
    """
    return (y + 1) / 2  # Convert -1,1 to 0,1


def preprocess_data(arff_path='data/Training_Dataset.arff', 
                   test_size=0.15, 
                   val_size=0.15,
                   random_state=42,
                   scale=True):
    """
    Complete preprocessing pipeline:
    1. Load dataset
    2. Encode target
    3. Scale features
    4. Split into train/validation/test
    
    Args:
        arff_path: Path to ARFF file
        test_size: Proportion for test set
        val_size: Proportion for validation set
        random_state: Random seed for reproducibility
        scale: Whether to scale features
    
    Returns:
        Tuple of (X_train, X_val, X_test, y_train, y_val, y_test, scaler, feature_names)
    """
    # Load data
    X, y, feature_names = load_dataset(arff_path)
    
    # Encode target: {-1, 1} -> {0, 1}
    y = encode_target(y)
    
    print(f"Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Target distribution: {(y==0).sum()} phishing, {(y==1).sum()} legitimate")
    
    # Split: 70% train, 15% val, 15% test
    # First split: 85% train+val, 15% test
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Second split: from 85%, take 15/85 ≈ 17.65% for validation
    val_size_adjusted = val_size / (1 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=val_size_adjusted, random_state=random_state, stratify=y_temp
    )
    
    # Fit scaler on training data only
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"\nData splits:")
    print(f"  Train: {X_train_scaled.shape}")
    print(f"  Val:   {X_val_scaled.shape}")
    print(f"  Test:  {X_test_scaled.shape}")
    
    return (X_train_scaled, X_val_scaled, X_test_scaled, 
            y_train.values, y_val.values, y_test.values,
            scaler, feature_names)


def save_preprocessing(scaler, feature_names, model_dir='models'):
    """Save preprocessing artifacts."""
    Path(model_dir).mkdir(exist_ok=True)
    joblib.dump(scaler, f'{model_dir}/scaler.joblib')
    joblib.dump(feature_names, f'{model_dir}/feature_names.joblib')
    print(f"Preprocessing artifacts saved to {model_dir}/")


def load_preprocessing(model_dir='models'):
    """Load preprocessing artifacts."""
    scaler = joblib.load(f'{model_dir}/scaler.joblib')
    feature_names = joblib.load(f'{model_dir}/feature_names.joblib')
    return scaler, feature_names


if __name__ == '__main__':
    # Example usage
    X_train, X_val, X_test, y_train, y_val, y_test, scaler, features = preprocess_data()
    print(f"\nFeatures ({len(features)}):")
    for i, feat in enumerate(features, 1):
        print(f"  {i:2d}. {feat}")
