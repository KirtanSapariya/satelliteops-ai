# agents/mission_coordinator.py
"""
Mission Coordinator Agent - Root orchestrator for SatelliteOps AI
"""

from agents.telemetry_monitor import TelemetryMonitorAgent
from agents.anomaly_detector import AnomalyDetectorAgent
from agents.orbit_predictor import OrbitPredictorAgent
from agents.collision_avoidance import CollisionAvoidanceAgent
from agents.alert_generator import AlertGeneratorAgent
from agents.report_agent import ReportAgent

async def create_mission_coordinator():
    telemetry_monitor = TelemetryMonitorAgent()
    anomaly_detector = AnomalyDetectorAgent()
    orbit_predictor = OrbitPredictorAgent()
    collision_avoidance = CollisionAvoidanceAgent()
    alert_generator = AlertGeneratorAgent()
    report_agent = ReportAgent()

    class MissionCoordinator:
        def __init__(self):
            self.telemetry_monitor = telemetry_monitor
            self.anomaly_detector = anomaly_detector
            self.orbit_predictor = orbit_predictor
            self.collision_avoidance = collision_avoidance
            self.alert_generator = alert_generator
            self.report_agent = report_agent

        async def run(self, query: str) -> str:
            q = query.lower()
            if "status" in q or "show" in q:
                return await self.telemetry_monitor.run({})
            if "anomaly" in q or "detect" in q:
                telemetry = await self.telemetry_monitor.run({})
                return await self.anomaly_detector.run({"telemetry": telemetry})
            if "orbit" in q or "predict" in q:
                return await self.orbit_predictor.run({})
            if "collision" in q or "risk" in q:
                orbit_data = await self.orbit_predictor.run({})
                return await self.collision_avoidance.run({"orbit_data": orbit_data})
            if "report" in q:
                telemetry = await self.telemetry_monitor.run({})
                return await self.report_agent.run({"telemetry": telemetry})
            telemetry = await self.telemetry_monitor.run({})
            anomalies = await self.anomaly_detector.run({"telemetry": telemetry})
            return f"""
🛰️  SATELLITEOPS AI - Mission Status Report

{telemetry}

{anomalies}

For detailed analysis, try:
  • 'orbit' - Orbital trajectory predictions
  • 'collision' - Conjunction risk assessment
  • 'report' - Comprehensive mission report
"""
    return MissionCoordinator()
