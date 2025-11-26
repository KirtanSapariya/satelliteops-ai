"""
Visualization Utilities
Orbital plots and telemetry dashboards
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from typing import List, Dict


def plot_orbital_trajectory(positions: List[np.ndarray], 
                            satellite_names: List[str],
                            save_path: str = None):
    """
    Plot 3D orbital trajectories

    Args:
        positions: List of position arrays (x, y, z) for each satellite
        satellite_names: List of satellite names
        save_path: Path to save plot (optional)
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot Earth
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 6371 * np.outer(np.cos(u), np.sin(v))
    y = 6371 * np.outer(np.sin(u), np.sin(v))
    z = 6371 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='blue', alpha=0.3)

    # Plot satellite trajectories
    for pos, name in zip(positions, satellite_names):
        ax.plot(pos[:, 0], pos[:, 1], pos[:, 2], label=name)

    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('Satellite Orbital Trajectories')
    ax.legend()

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


def plot_telemetry_timeseries(telemetry_data: Dict, 
                              metrics: List[str],
                              save_path: str = None):
    """
    Plot telemetry time series

    Args:
        telemetry_data: Dict with timestamps and metric values
        metrics: List of metrics to plot
        save_path: Path to save plot (optional)
    """
    fig, axes = plt.subplots(len(metrics), 1, figsize=(12, 8), sharex=True)

    if len(metrics) == 1:
        axes = [axes]

    for ax, metric in zip(axes, metrics):
        timestamps = telemetry_data['timestamps']
        values = telemetry_data[metric]

        ax.plot(timestamps, values)
        ax.set_ylabel(metric.replace('_', ' ').title())
        ax.grid(True)

    axes[-1].set_xlabel('Time')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


def create_mission_dashboard(telemetry: Dict, 
                             anomalies: List[Dict],
                             collision_risks: List[Dict],
                             save_path: str = "dashboard.png"):
    """
    Create comprehensive mission dashboard

    Args:
        telemetry: Current telemetry data
        anomalies: List of detected anomalies
        collision_risks: List of collision risks
        save_path: Path to save dashboard
    """
    fig = plt.figure(figsize=(16, 10))

    # Create subplots for different metrics
    # This is a placeholder - production would include detailed visualizations

    plt.suptitle('SatelliteOps AI - Mission Dashboard', fontsize=16, fontweight='bold')

    if save_path:
        plt.savefig(save_path, dpi=150)
    else:
        plt.show()
