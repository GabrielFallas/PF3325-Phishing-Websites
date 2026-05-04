"""
Neural network model architectures for phishing detection.
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, regularizers


def create_mlp_model(input_dim, 
                     hidden_layers=[128, 64, 32],
                     dropout_rates=[0.3, 0.2, 0.1],
                     learning_rate=0.001):
    """
    Create a Multi-Layer Perceptron (MLP) for binary classification.
    
    Args:
        input_dim: Number of input features
        hidden_layers: List of neurons per hidden layer
        dropout_rates: Dropout rate for each hidden layer
        learning_rate: Learning rate for Adam optimizer
    
    Returns:
        Compiled Keras model
    """
    model = models.Sequential([
        # Input layer
        layers.Input(shape=(input_dim,)),
        
        # Hidden layers with BatchNorm and Dropout
        layers.Dense(hidden_layers[0], kernel_regularizer=regularizers.l2(0.001)),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Dropout(dropout_rates[0]),
        
        layers.Dense(hidden_layers[1], kernel_regularizer=regularizers.l2(0.001)),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Dropout(dropout_rates[1]),
        
        layers.Dense(hidden_layers[2]),
        layers.Activation('relu'),
        layers.Dropout(dropout_rates[2]),
        
        # Output layer
        layers.Dense(1, activation='sigmoid')
    ])
    
    # Compile model
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=[
            'accuracy',
            keras.metrics.Precision(name='precision'),
            keras.metrics.Recall(name='recall'),
            keras.metrics.AUC(name='auc')
        ]
    )
    
    return model


def create_simple_model(input_dim, learning_rate=0.001):
    """
    Create a simpler MLP model for faster training (testing purposes).
    """
    model = models.Sequential([
        layers.Input(shape=(input_dim,)),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc')]
    )
    
    return model


if __name__ == '__main__':
    # Test model creation
    model = create_mlp_model(input_dim=30)
    model.summary()
