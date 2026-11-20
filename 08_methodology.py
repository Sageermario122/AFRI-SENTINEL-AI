import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DASHBOARD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path: sys.path.insert(0, PROJECT_ROOT)
if DASHBOARD_ROOT not in sys.path: sys.path.insert(0, DASHBOARD_ROOT)

import pandas as pd
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

st.set_page_config(page_title="Methodology — GeoIntel AI", layout="wide")
apply_global_styles()
render_sidebar()
render_ops_header("METHODOLOGY")

REDESIGN_DIR = r"D:\Geoplotics how it afftects millitary\outputs\evaluation\target_redesign"

# Hero Banner Header matching the reference image satellite map background
st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">Research Methodology & Evaluation History</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Transparent research design, target formulation, evaluation protocol and data sources.</p>
</div>
""", unsafe_allow_html=True)

# Target C Formulation Card
st.markdown("""
<div class="glass-card">
    <h3 style="color: #38bdf8; margin-top: 0; display: flex; align-items: center; gap: 0.6rem; font-size: 1.25rem;">
        🎯 Target C Formulation (Relative Escalation)
    </h3>
    <div class="formula-box">
        <span style="font-size: 1.35rem; color: #f8fafc; font-weight: 600;">
            $$\\text{Target C}_{c, T+1} = \\mathbb{I}\\left( \\text{Conflict}_{c, T+1} > 1.5 \\times \\text{Mean}_{12M}(c, T) + 1 \\right)$$
        </span>
    </div>
    <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 0;">
        Target C measures whether country-level conflict in month $T+1$ increases materially above recent 12-month historical levels. Rolling baselines use information strictly up to month $T$.
    </p>
</div>
""", unsafe_allow_html=True)

# Temporal Split Boundaries & Multi-Source Integrated Datasets
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card" style="height: 100%;">
        <h4 style="color: #38bdf8; margin-top: 0; display: flex; align-items: center; gap: 0.5rem; font-size: 1.1rem;">
            📅 Temporal Split Boundaries
        </h4>
        <ul style="color: #cbd5e1; line-height: 1.85; font-size: 0.95rem; padding-left: 1.2rem;">
            <li><strong>Training Set (1979–2005)</strong><br><span style="color: #94a3b8;">59,321 country-month rows (15.80% prevalence)</span></li>
            <li style="margin-top: 0.6rem;"><strong>Validation Set (2006–2009)</strong><br><span style="color: #94a3b8;">9,553 country-month rows (23.56% prevalence)</span></li>
            <li style="margin-top: 0.6rem;"><strong>Historical Holdout (2010–2014)</strong><br><span style="color: #94a3b8;">9,828 country-month rows (15.32% prevalence)</span></li>
        </ul>
        <div style="background: rgba(56, 189, 248, 0.1); border-left: 3px solid #38bdf8; padding: 0.75rem; border-radius: 6px; margin-top: 1rem; font-size: 0.85rem; color: #cbd5e1;">
            ℹ️ Temporal splits ensure strict separation to prevent information leakage from future periods.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="height: 100%;">
        <h4 style="color: #38bdf8; margin-top: 0; display: flex; align-items: center; gap: 0.5rem; font-size: 1.1rem;">
            🗄️ Multi-Source Integrated Datasets
        </h4>
        <ul style="color: #cbd5e1; line-height: 1.85; font-size: 0.95rem; padding-left: 1.2rem;">
            <li><strong>GDELT</strong>: News article streams, Goldstein scale, media tone.</li>
            <li><strong>ACLED</strong>: Armed conflict events, battles, protests, fatalities.</li>
            <li><strong>SIPRI</strong>: Military expenditure (% GDP) & spending growth rates.</li>
            <li><strong>V-Dem</strong>: Electoral democracy, corruption, and rule of law indices.</li>
            <li><strong>GTD</strong>: Terrorism events, fatalities, attack success, and diversity.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Selection Matrix Table
st.markdown("""
<div class="glass-card">
    <h4 style="color: #38bdf8; margin-top: 0; display: flex; align-items: center; gap: 0.5rem; font-size: 1.1rem;">
        ⚖️ Target Redesign Selection Matrix (Targets A–D)
    </h4>
</div>
""", unsafe_allow_html=True)

matrix_csv = os.path.join(REDESIGN_DIR, "final_target_selection_matrix.csv")
if os.path.exists(matrix_csv):
    st.dataframe(pd.read_csv(matrix_csv), use_container_width=True)

render_footer()
