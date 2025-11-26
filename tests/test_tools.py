"""
Unit Tests for SatelliteOps AI Tools
"""

import pytest
import numpy as np
from tools.telemetry_tools import parse_telemetry, validate_telemetry
from tools.orbital_mechanics import calculate_orbital_period, calculate_miss_distance
from tools.ml_tools import extract_features


def test_parse_telemetry():
    """Test telemetry parsing"""
    raw_data = b"test_data"
    telemetry = parse_telemetry(raw_data)

    assert 'timestamp' in telemetry
    assert 'position' in telemetry
    assert 'velocity' in telemetry


def test_validate_telemetry():
    """Test telemetry validation"""
    valid_telemetry = {
        'timestamp': '2025-11-18T00:00:00',
        'position': np.array([0, 0, 0]),
        'velocity': np.array([0, 0, 0]),
        'temperature': 25.0
    }

    is_valid, errors = validate_telemetry(valid_telemetry)
    assert is_valid == True
    assert len(errors) == 0


def test_calculate_orbital_period():
    """Test orbital period calculation"""
    # LEO satellite at 550 km altitude
    semi_major_axis = 6371 + 550  # Earth radius + altitude
    period = calculate_orbital_period(semi_major_axis)

    assert 90 < period < 100  # ~95 minutes for LEO


def test_calculate_miss_distance():
    """Test miss distance calculation"""
    pos1 = np.array([7000, 0, 0])
    pos2 = np.array([7001, 0, 0])
    vel1 = np.array([0, 7.5, 0])
    vel2 = np.array([0, 7.5, 0])

    miss_distance = calculate_miss_distance(pos1, pos2, vel1, vel2, 1.0)
    assert miss_distance >= 0


def test_extract_features():
    """Test feature extraction"""
    telemetry = {
        'temperature': 25.0,
        'power': 450,
        'altitude_km': 550,
        'velocity_km_s': 7.58,
        'attitude_deg': 0.02
    }

    features = extract_features(telemetry)
    assert len(features) == 5
    assert features[0] == 25.0
