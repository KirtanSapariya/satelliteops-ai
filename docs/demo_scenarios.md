# SatelliteOps AI - Demo Scenarios

## Setup

```bash
# Clone repository
git clone https://github.com/your-username/satelliteops-ai
cd satelliteops-ai

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add GOOGLE_API_KEY

# Run system
python main.py
```

## Scenario 1: Normal Operations Monitoring

**Objective**: Check constellation status under normal conditions

**Steps**:
1. Start the system: `python main.py`
2. Enter command: `status`
3. Observe telemetry report showing all satellites nominal

**Expected Output**:
```
📡 TELEMETRY STATUS (Updated: 2025-11-18 13:00:00)
----------------------------------------------------------------------

🛰️  LEO-SAT-001
   Altitude: 550.2 km
   Velocity: 7.58 km/s
   Battery Temp: 22.5°C
   Power Output: 450 W
   Attitude Error: 0.020°
   Status: ✅ NOMINAL

[Similar for LEO-SAT-002 and LEO-SAT-003]
```

**Success Criteria**:
- All 3 satellites reported
- Status shows NOMINAL
- Response time < 5 seconds

## Scenario 2: Anomaly Detection

**Objective**: Detect thermal anomaly in battery system

**Steps**:
1. Enter command: `anomaly`
2. System injects simulated temperature spike (demo mode)
3. Observe anomaly detection and recommendations

**Expected Output**:
```
⚠️  ANOMALY DETECTED
==================================================================
Satellite: LEO-SAT-001
Metric: Battery Temperature
Current Value: 58.2°C
Normal Range: 20-45°C
Anomaly Score: 0.87 (threshold: 0.50)
Severity: HIGH

🔍 Root Cause Analysis:
   • Thermal system degradation detected
   • Power draw exceeds thermal capacity
   • Possible battery cell failure

💡 Recommendations:
   1. Reduce non-critical power systems
   2. Activate secondary thermal management
   3. Schedule thermal diagnostic routine
   4. Monitor battery health every 5 minutes

⏱️  Detection Time: 3.2 seconds (vs 2+ hours manual)
```

**Success Criteria**:
- Anomaly detected within 5 seconds
- Root cause analysis provided
- Actionable recommendations listed
- Detection time < 10 seconds

## Scenario 3: Orbital Trajectory Prediction

**Objective**: Forecast satellite positions for next 24 hours

**Steps**:
1. Enter command: `orbit`
2. System calculates orbital propagation using SGP4
3. Observe predicted positions and ground station passes

**Expected Output**:
```
🌍 ORBITAL TRAJECTORY PREDICTION
==================================================================
Prediction Time: 2025-11-18 13:00:00 UTC
Forecast Period: Next 24 hours

🛰️  LEO-SAT-001
   Current Position (ECI):
      X: 3456.7 km, Y: 4521.3 km, Z: 2345.8 km
   Current Velocity:
      Vx: -3.2 km/s, Vy: 6.1 km/s, Vz: 2.8 km/s
   Orbital Period: 95.8 minutes
   Next Ground Station Pass: +2.3 hours
   Next Downlink Window: +3.1 hours (duration: 8 min)

[Similar for other satellites]

📊 Trajectory Confidence: 99.2%
🔄 Update Frequency: Every 60 seconds
```

**Success Criteria**:
- Positions calculated for all satellites
- Ground station passes identified
- Confidence level reported
- Response time < 8 seconds

## Scenario 4: Collision Risk Assessment

**Objective**: Detect conjunction event and recommend avoidance maneuver

**Steps**:
1. Enter command: `collision`
2. System screens 25,000+ cataloged objects
3. Observe conjunction detection and maneuver recommendations

**Expected Output** (when conjunction detected):
```
🛡️  COLLISION RISK ASSESSMENT
==================================================================
Analysis Time: 2025-11-18 13:00:00 UTC
Monitored Objects: 25,483 (satellites + debris)

⚠️  CONJUNCTION DETECTED

Primary Object: LEO-SAT-002
Secondary Object: DEBRIS-5472 (spent rocket stage)
Time to Closest Approach (TCA): 36.2 hours
Miss Distance: 850 meters
Probability of Collision: 1.2e-4 (0.012%)
Risk Level: MEDIUM (threshold: 1000m)

📍 Conjunction Details:
   • TCA: 2025-11-20 03:45:23 UTC
   • Relative Velocity: 14.3 km/s
   • Combined Object Size: 8.2 meters

💡 Recommended Actions:
   1. Perform collision avoidance maneuver
   2. Maneuver Type: Radial burn
   3. Delta-V Required: +2.3 m/s
   4. Optimal Burn Time: T-24 hours
   5. Post-maneuver orbit verification required

🔄 Monitoring: Continuous tracking until conjunction passes
```

**Success Criteria**:
- Conjunction detected 24-48 hours in advance
- Miss distance calculated
- Collision probability computed
- Maneuver recommendations provided
- Response time < 15 seconds

## Scenario 5: Comprehensive Mission Report

**Objective**: Generate full mission performance report

**Steps**:
1. Enter command: `report`
2. System aggregates metrics from all agents
3. Observe comprehensive mission summary

**Expected Output**:
```
📊 COMPREHENSIVE MISSION REPORT
==================================================================
Report Generated: 2025-11-18 13:00:00 UTC
Mission Duration: 24 hours

🎯 MISSION SUMMARY
----------------------------------------------------------------------
Total Satellites: 3
Operational: 3 (100%)
Anomalies Detected: 2
Anomalies Resolved: 2
Collision Avoidance Maneuvers: 1
Downlink Sessions Completed: 18
Data Downloaded: 145.2 GB

📈 PERFORMANCE METRICS
----------------------------------------------------------------------
Average Anomaly Detection Time: 3.2 seconds
Manual Detection Baseline: 2+ hours
Performance Improvement: 10x faster
False Positive Rate: 4.3% (baseline: 15%)
System Uptime: 99.7%
Mission Success Rate: 100%

💡 RECOMMENDATIONS
----------------------------------------------------------------------
1. Schedule battery maintenance for LEO-SAT-001
2. Update collision database (25,483 objects tracked)
3. Optimize downlink schedules for +15% capacity
4. Review thermal management protocols
```

**Success Criteria**:
- All mission metrics aggregated
- Performance improvements quantified
- Recommendations actionable
- Response time < 12 seconds

## Video Demo Script

For competition video (8 minutes):

**0:00-1:00**: Hook & Problem
- Show satellite failure news
- Explain scalability crisis
- State problem clearly

**1:00-2:00**: Solution Overview
- Show architecture diagram
- Explain 7-agent system
- Highlight key technologies

**2:00-4:00**: Demo Scenario 1 (Normal Ops)
- Run `status` command
- Show telemetry visualization
- Explain real-time processing

**4:00-6:00**: Demo Scenario 2 (Anomaly)
- Run `anomaly` command
- Show 3.2-second detection
- Compare vs 2+ hour manual
- Highlight recommendations

**6:00-7:30**: Demo Scenario 4 (Collision)
- Run `collision` command
- Show 36-hour advance warning
- Display maneuver recommendations
- Explain space sustainability impact

**7:30-8:00**: Impact & Conclusion
- Show performance dashboard
- Quantify improvements
- State social impact
- GitHub repo link
