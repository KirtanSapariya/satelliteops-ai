# SatelliteOps AI - API Documentation

## Agent APIs

### Mission Coordinator Agent

```python
async def create_mission_coordinator() -> MissionCoordinator:
    """
    Creates and configures the mission coordinator agent

    Returns:
        Configured mission coordinator
    """
```

```python
async def MissionCoordinator.run(query: str) -> str:
    """
    Process user query through appropriate agents

    Args:
        query: Natural language query from user

    Returns:
        Synthesized response from agents
    """
```

### Telemetry Monitor Agent

```python
class TelemetryMonitorAgent(BaseAgent):
    async def run(context: Dict[str, Any]) -> str:
        """
        Process telemetry data and return current status

        Args:
            context: Execution context with state

        Returns:
            Formatted telemetry report
        """
```

### Anomaly Detector Agent

```python
class AnomalyDetectorAgent(BaseAgent):
    async def run(context: Dict[str, Any]) -> str:
        """
        Analyze telemetry for anomalies

        Args:
            context: Execution context with telemetry data

        Returns:
            Anomaly detection report with recommendations
        """
```

## Tool APIs

### Telemetry Tools

```python
def parse_telemetry(raw_data: bytes) -> Dict:
    """
    Parse raw telemetry data into structured format

    Args:
        raw_data: Raw telemetry bytes from satellite

    Returns:
        Parsed telemetry dictionary with:
            - timestamp: datetime
            - position: np.ndarray [x, y, z] in km
            - velocity: np.ndarray [vx, vy, vz] in km/s
            - temperature: float in Celsius
            - power: float in Watts
            - attitude: np.ndarray [roll, pitch, yaw] in degrees
    """
```

```python
def validate_telemetry(telemetry: Dict) -> Tuple[bool, List[str]]:
    """
    Validate telemetry data quality

    Args:
        telemetry: Telemetry dictionary

    Returns:
        (is_valid, error_messages)
    """
```

### Orbital Mechanics Tools

```python
def sgp4_propagate(tle_line1: str, tle_line2: str, 
                   time_delta_hours: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Propagate satellite orbit using SGP4

    Args:
        tle_line1: TLE first line
        tle_line2: TLE second line
        time_delta_hours: Hours to propagate forward

    Returns:
        (position_km, velocity_km_s) in ECI coordinates
    """
```

```python
def calculate_miss_distance(pos1: np.ndarray, pos2: np.ndarray,
                            vel1: np.ndarray, vel2: np.ndarray,
                            time_to_tca_hours: float) -> float:
    """
    Calculate miss distance at Time of Closest Approach

    Args:
        pos1, pos2: Current positions in ECI (km)
        vel1, vel2: Current velocities in ECI (km/s)
        time_to_tca_hours: Time to TCA in hours

    Returns:
        Miss distance in meters
    """
```

### ML Tools

```python
class AnomalyDetector:
    def __init__(contamination: float = 0.1):
        """Initialize Isolation Forest detector"""

    def fit(telemetry_data: np.ndarray):
        """Train detector on historical data"""

    def detect(telemetry_sample: np.ndarray) -> Tuple[float, bool]:
        """
        Detect anomalies

        Returns:
            (anomaly_score, is_anomaly)
        """
```

## Usage Examples

### Basic Query

```python
from agents.mission_coordinator import create_mission_coordinator

coordinator = await create_mission_coordinator()
response = await coordinator.run("Show satellite status")
print(response)
```

### Anomaly Detection

```python
response = await coordinator.run("Detect anomalies")
# Returns anomaly report with recommendations
```

### Orbit Prediction

```python
response = await coordinator.run("Predict orbit for next 24 hours")
# Returns orbital trajectory with position/velocity
```

### Collision Risk

```python
response = await coordinator.run("Check collision risks")
# Returns conjunction analysis with maneuver recommendations
```
