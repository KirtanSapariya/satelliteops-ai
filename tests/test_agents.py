"""
Unit Tests for SatelliteOps AI Agents
"""

import pytest
import asyncio
from agents.telemetry_monitor import TelemetryMonitorAgent
from agents.anomaly_detector import AnomalyDetectorAgent
from agents.orbit_predictor import OrbitPredictorAgent
from agents.collision_avoidance import CollisionAvoidanceAgent


@pytest.mark.asyncio
async def test_telemetry_monitor_agent():
    """Test telemetry monitor agent"""
    agent = TelemetryMonitorAgent()
    result = await agent.run({})

    assert "LEO-SAT-001" in result
    assert "TELEMETRY STATUS" in result
    assert agent.name == "telemetry_monitor"


@pytest.mark.asyncio
async def test_anomaly_detector_agent():
    """Test anomaly detector agent"""
    agent = AnomalyDetectorAgent()
    result = await agent.run({'telemetry': {}})

    assert "ANOMALY" in result or "NOMINAL" in result
    assert agent.name == "anomaly_detector"


@pytest.mark.asyncio
async def test_orbit_predictor_agent():
    """Test orbit predictor agent"""
    agent = OrbitPredictorAgent()
    result = await agent.run({})

    assert "ORBITAL TRAJECTORY" in result
    assert "Position" in result
    assert agent.name == "orbit_predictor"


@pytest.mark.asyncio
async def test_collision_avoidance_agent():
    """Test collision avoidance agent"""
    agent = CollisionAvoidanceAgent()
    result = await agent.run({})

    assert "COLLISION RISK" in result
    assert agent.name == "collision_avoidance"


@pytest.mark.asyncio
async def test_agent_error_handling():
    """Test agent error handling"""
    agent = TelemetryMonitorAgent()
    # Should not raise exception
    result = await agent.run({})
    assert result is not None
