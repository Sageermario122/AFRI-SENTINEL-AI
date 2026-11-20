import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DASHBOARD_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if DASHBOARD_ROOT not in sys.path:
    sys.path.insert(0, DASHBOARD_ROOT)

import streamlit as st

try:
    from dashboard.components.styles import apply_global_styles
    from dashboard.components.header import render_ops_header
    from dashboard.components.sidebar import render_sidebar
    from dashboard.components.footer import render_footer
except ModuleNotFoundError:
    from components.styles import apply_global_styles
    from components.header import render_ops_header
    from components.sidebar import render_sidebar
    from components.footer import render_footer

st.set_page_config(
    page_title="GeoIntel AI — Operations Center",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_global_styles()
render_sidebar()
render_ops_header("EXECUTIVE OVERVIEW & SYSTEM STATUS")

st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">🌐 GeoIntel AI Operations Center</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Explainable AI-Powered Geopolitical Risk Intelligence & Conflict Escalation Early-Warning System.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card" style="height: 100%;">
        <h4 style="color: #38bdf8; margin-top: 0;">🎯 INTELLIGENCE MODULES</h4>
        <ul style="color: #cbd5e1; line-height: 1.8;">
            <li><strong>Executive Overview</strong>: System status, global metric cards, and research scope.</li>
            <li><strong>Global Risk Map</strong>: Interactive Plotly world map with Target C risk scores.</li>
            <li><strong>Country Intelligence</strong>: Country deep dives, historical conflict trends, and 12M baselines.</li>
            <li><strong>Escalation Forecast</strong>: $T+1$ Risk scores, thresholding, and LLM text synthesis.</li>
            <li><strong>News Intelligence</strong>: Real GDELT news stream footprint, sentiment tone, & Goldstein scale.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="height: 100%;">
        <h4 style="color: #38bdf8; margin-top: 0;">📊 ANALYTICS & MONITORING</h4>
        <ul style="color: #cbd5e1; line-height: 1.8;">
            <li><strong>Explainable AI</strong>: TreeSHAP summary beeswarm and feature contribution waterfall charts.</li>
            <li><strong>Event Timeline</strong>: Chronological multi-source event log across ACLED, GDELT, and GTD.</li>
            <li><strong>Methodology</strong>: Transparent research methodology and Target C formulation.</li>
            <li><strong>Real-Time Monitor</strong>: Live risk monitoring page with data freshness tracking.</li>
            <li><strong>Alert Center & System Health</strong>: Risk alerts and PSI feature drift monitors.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("👈 Select an intelligence module from the sidebar navigation menu to begin exploration.")
render_footer()
