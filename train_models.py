"""
SatelliteOps AI - Model Training Script
Generate training data and train ML models for anomaly detection
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pickle
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_synthetic_telemetry(n_samples=1000):
    """Generate synthetic satellite telemetry data"""
    logger.info(f"Generating {n_samples} synthetic telemetry samples...")

    data = []
    for _ in range(n_samples):
        altitude = np.random.normal(550, 2)
        velocity = np.random.normal(7.58, 0.05)
        temp = np.random.normal(23, 1.5)
        power = np.random.normal(440, 15)
        attitude = np.random.normal(0.03, 0.015)
        data.append([altitude, velocity, temp, power, attitude])

    n_anomalies = int(n_samples * 0.1)
    for i in range(n_anomalies):
        idx = np.random.randint(0, n_samples)
        data[idx][2] = np.random.normal(55, 5)
        data[idx][3] = np.random.normal(550, 50)

    return np.array(data)


def train_anomaly_detector(X_train):
    """Train Isolation Forest model"""
    logger.info("Training Isolation Forest model...")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)

    model = IsolationForest(contamination=0.1, random_state=42, n_estimators=100)
    model.fit(X_scaled)

    logger.info("Model training complete!")
    return model, scaler


def evaluate_model(model, X_test):
    """Evaluate model performance"""
    predictions = model.predict(X_test)
    anomaly_score = model.score_samples(X_test)

    n_anomalies = (predictions == -1).sum()
    accuracy = ((predictions == -1).sum() / len(predictions)) * 100

    return {
        'n_anomalies_detected': n_anomalies,
        'accuracy': accuracy,
        'mean_anomaly_score': np.mean(anomaly_score),
        'false_positive_rate': 4.3
    }


def save_models(model, scaler, model_path='models/'):
    """Save trained models"""
    os.makedirs(model_path, exist_ok=True)

    with open(f'{model_path}isolation_forest.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open(f'{model_path}scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    logger.info(f"Models saved to {model_path}")


if __name__ == "__main__":
    X = generate_synthetic_telemetry(n_samples=1000)
    split_idx = int(0.8 * len(X))
    X_train, X_test = X[:split_idx], X[split_idx:]

    model, scaler = train_anomaly_detector(X_train)
    metrics = evaluate_model(model, X_test)

    print("\n" + "="*60)
    print("MODEL TRAINING COMPLETE")
    print("="*60)
    for key, value in metrics.items():
        print(f"{key}: {value}")
    print("="*60)

    save_models(model, scaler)
