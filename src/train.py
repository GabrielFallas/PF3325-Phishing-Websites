"""
Training script for phishing detection models.
"""

import sys
import argparse
from pathlib import Path
import json
import numpy as np

import tensorflow as tf
from tensorflow import keras

from preprocess import preprocess_data, save_preprocessing
from model import create_mlp_model, create_simple_model


def train_model(X_train, X_val, y_train, y_val,
                model_name='best_model.keras',
                epochs=50,
                batch_size=32,
                simple_model=False,
                model_dir='models',
                verbose=1):
    """
    Train the neural network model.
    
    Args:
        X_train, X_val, y_train, y_val: Training and validation data
        model_name: Name to save the model as
        epochs: Number of training epochs
        batch_size: Batch size
        simple_model: If True, use simpler model for faster training
        model_dir: Directory to save model
        verbose: Verbosity level for training
    
    Returns:
        Trained model and training history
    """
    # Create model
    if simple_model:
        print("Creating SIMPLE model (for quick testing)...")
        model = create_simple_model(input_dim=X_train.shape[1])
    else:
        print("Creating MLP model...")
        model = create_mlp_model(input_dim=X_train.shape[1])
    
    print(f"\nModel architecture:")
    model.summary()
    
    # Callbacks
    model_path = Path(model_dir) / model_name
    Path(model_dir).mkdir(exist_ok=True)
    
    callbacks = [
        keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True,
            verbose=1
        ),
        keras.callbacks.ModelCheckpoint(
            str(model_path),
            monitor='val_auc',
            save_best_only=True,
            verbose=1
        )
    ]
    
    # Train
    print(f"\nTraining for {epochs} epochs...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=verbose
    )
    
    print(f"\n✓ Model saved to {model_path}")
    
    # Save training history
    history_data = {k: [float(v) for v in hist] for k, hist in history.history.items()}
    history_path = Path(model_dir) / 'training_history.json'
    with open(history_path, 'w') as f:
        json.dump(history_data, f)
    print(f"✓ Training history saved to {history_path}")
    
    return model, history


def main():
    parser = argparse.ArgumentParser(description='Train phishing detection model')
    parser.add_argument('--epochs', type=int, default=50, help='Number of epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    parser.add_argument('--simple', action='store_true', help='Use simple model')
    parser.add_argument('--model-dir', default='models', help='Directory to save models')
    args = parser.parse_args()
    
    # Preprocess data
    print("=" * 60)
    print("PREPROCESSING DATA")
    print("=" * 60)
    X_train, X_val, X_test, y_train, y_val, y_test, scaler, features = preprocess_data()
    
    # Save preprocessing artifacts
    save_preprocessing(scaler, features, model_dir=args.model_dir)
    
    # Train model
    print("\n" + "=" * 60)
    print("TRAINING MODEL")
    print("=" * 60)
    model, history = train_model(
        X_train, X_val, y_train, y_val,
        epochs=args.epochs,
        batch_size=args.batch_size,
        simple_model=args.simple,
        model_dir=args.model_dir
    )
    
    print("\n" + "=" * 60)
    print("TRAINING COMPLETE")
    print("=" * 60)
    print(f"Best validation AUC: {max(history.history['val_auc']):.4f}")
    print(f"Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")


if __name__ == '__main__':
    main()
