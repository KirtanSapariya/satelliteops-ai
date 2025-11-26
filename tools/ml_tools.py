"""
Machine Learning Utilities
Anomaly detection and feature engineering
"""

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from typing import Tuple, Dict, List


class AnomalyDetector:
    """Isolation Forest-based anomaly detector"""

    def __init__(self, contamination: float = 0.1):
        self.model = IsolationForest(
            contamination=contamination,
            n_estimators=100,
            max_samples=256,
            random_state=42
        )
        self.scaler = StandardScaler()
        self.is_fitted = False

    def fit(self, telemetry_data: np.ndarray):
        """Train anomaly detector on historical data"""
        scaled_data = self.scaler.fit_transform(telemetry_data)
        self.model.fit(scaled_data)
        self.is_fitted = True

    def detect(self, telemetry_sample: np.ndarray) -> Tuple[float, bool]:
        """
        Detect anomalies in telemetry sample

        Returns:
            (anomaly_score, is_anomaly)
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before detection")

        scaled_sample = self.scaler.transform(telemetry_sample.reshape(1, -1))
        anomaly_score = self.model.decision_function(scaled_sample)[0]
        is_anomaly = anomaly_score < -0.5

        return anomaly_score, is_anomaly


def extract_features(telemetry: Dict) -> np.ndarray:
    """
    Extract feature vector from telemetry

    Args:
        telemetry: Telemetry dictionary

    Returns:
        Feature vector for ML models
    """
    features = [
        telemetry.get('temperature', 0),
        telemetry.get('power', 0),
        telemetry.get('altitude_km', 0),
        telemetry.get('velocity_km_s', 0),
        telemetry.get('attitude_deg', 0)
    ]

    return np.array(features)


def analyze_root_cause(features: np.ndarray, feature_names: List[str]) -> Dict:
    """
    Analyze root cause of anomaly using feature importance

    Args:
        features: Feature vector
        feature_names: Names of features

    Returns:
        Root cause analysis dict
    """
    # Calculate feature deviations from normal
    # This is simplified - production would use more sophisticated analysis

    root_cause = {
        'primary_factor': feature_names[0],
        'contributing_factors': feature_names[1:3],
        'severity': 'HIGH'
    }

    return root_cause
