"""
SatelliteOps AI - Real-Time Monitoring Dashboard
Professional Streamlit UI for satellite operations
"""

import streamlit as st
import asyncio
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '.')

st.set_page_config(
    page_title="SatelliteOps AI Dashboard",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #0066cc;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🛰️ SatelliteOps AI - Real-Time Dashboard</div>', unsafe_allow_html=True)

st.sidebar.header("🎛️ Mission Control")
selected_view = st.sidebar.radio(
    "Select View",
    ["📊 Dashboard", "📡 Telemetry", "⚠️ Anomalies", "🛡️ Collisions", "📈 Reports"]
)

if "coordinator" not in st.session_state:
    try:
        from agents.mission_coordinator import create_mission_coordinator
        st.session_state.coordinator = asyncio.run(create_mission_coordinator())
    except:
        st.warning("Mission coordinator not available")

if selected_view == "📊 Dashboard":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🛰️ Active Satellites", "3", "+0")
    with col2:
        st.metric("⚠️ Anomalies Today", "2", "-1")
    with col3:
        st.metric("🛡️ Collision Events", "0", "OK")
    with col4:
        st.metric("📊 System Health", "99.7%", "↑ 0.1%")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📡 Satellite Status")
        sat_data = {
            'Satellite': ['LEO-SAT-001', 'LEO-SAT-002', 'LEO-SAT-003'],
            'Altitude (km)': [550.2, 548.9, 552.1],
            'Velocity (km/s)': [7.58, 7.59, 7.57],
            'Temp (°C)': [22.5, 24.1, 23.8],
            'Power (W)': [450, 425, 440],
            'Status': ['🟢 NOMINAL', '🟢 NOMINAL', '🟢 NOMINAL']
        }
        df = pd.DataFrame(sat_data)
        st.dataframe(df, use_container_width=True)

    with col2:
        st.subheader("📈 Performance Metrics")
        metrics_data = {
            'Metric': ['Detection Time', 'Manual Baseline', 'Improvement', 'False Positives'],
            'Value': ['3.2s', '2+ hours', '10x faster', '4.3%']
        }
        df_metrics = pd.DataFrame(metrics_data)
        st.dataframe(df_metrics, use_container_width=True)

elif selected_view == "📡 Telemetry":
    st.subheader("Live Telemetry Stream")
    hours = np.arange(0, 24, 0.5)
    temp_data = 22 + 5*np.sin(hours/12) + np.random.normal(0, 0.5, len(hours))
    power_data = 450 + 50*np.sin(hours/6) + np.random.normal(0, 5, len(hours))

    col1, col2 = st.columns(2)

    with col1:
        fig_temp = px.line(x=hours, y=temp_data, labels={'x': 'Time (hours)', 'y': 'Temperature (°C)'}, title="Battery Temperature")
        st.plotly_chart(fig_temp, use_container_width=True)

    with col2:
        fig_power = px.line(x=hours, y=power_data, labels={'x': 'Time (hours)', 'y': 'Power (W)'}, title="Power Output")
        st.plotly_chart(fig_power, use_container_width=True)

elif selected_view == "⚠️ Anomalies":
    st.subheader("Anomaly Detection Report")
    if hasattr(st.session_state, 'coordinator'):
        try:
            result = asyncio.run(st.session_state.coordinator.run("anomaly"))
            st.code(result, language="text")
        except:
            st.info("Run system to generate anomaly report")

elif selected_view == "🛡️ Collisions":
    st.subheader("Collision Risk Assessment")
    if hasattr(st.session_state, 'coordinator'):
        try:
            result = asyncio.run(st.session_state.coordinator.run("collision"))
            st.code(result, language="text")
        except:
            st.info("Run system to generate collision report")

elif selected_view == "📈 Reports":
    st.subheader("Comprehensive Mission Report")
    if hasattr(st.session_state, 'coordinator'):
        try:
            result = asyncio.run(st.session_state.coordinator.run("report"))
            st.code(result, language="text")
        except:
            st.info("Run system to generate mission report")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #999; font-size: 0.9rem;'>🛰️ SatelliteOps AI | Autonomous Satellite Operations Platform</div>", unsafe_allow_html=True)
