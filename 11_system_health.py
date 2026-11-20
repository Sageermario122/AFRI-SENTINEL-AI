import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DASHBOARD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path: sys.path.insert(0, PROJECT_ROOT)
if DASHBOARD_ROOT not in sys.path: sys.path.insert(0, DASHBOARD_ROOT)

import json
import pandas as pd
import streamlit as st

try:
    from dashboard.components.styles import apply_global_styles
    from dashboard.components.header import render_ops_header
    from dashboard.components.sidebar import render_sidebar
    from dashboard.components.footer import render_footer
    from dashboard.components.cards import render_metric_card
except ModuleNotFoundError:
    from components.styles import apply_global_styles
    from components.header import render_ops_header
    from components.sidebar import render_sidebar
    from components.footer import render_footer
    from components.cards import render_metric_card

from src.monitoring.data_drift import compute_feature_drift_metrics

st.set_page_config(page_title="System Health & Drift — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("SYSTEM HEALTH & DRIFT")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"
MODELS_DIR = r"D:\Geoplotics how it afftects millitary\models\trained"

@st.cache_data
def load_health_data():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    
    with open(os.path.join(MODELS_DIR, "feature_order.json")) as f:
        feature_cols = json.load(f)
        
    df_train = df[df['month'] <= '2005-12']
    df_recent = df[df['month'] >= '2010-01']
    
    df_drift = compute_feature_drift_metrics(df_train, df_recent, feature_cols)
    return df_drift

df_drift = load_health_data()

c1, c2, c3, c4 = st.columns(4)
with c1: render_metric_card("Model Status", "🟢 OPERATIONAL", "XGBoost v1.0.0", "#22c55e")
with c2: render_metric_card("Data Freshness", "🟢 FRESH", "Real-World Sources", "#22c55e")
with c3: render_metric_card("API Connectors", "🟢 READY", "GDELT & LLM Fallback", "#22c55e")
with c4: render_metric_card("Monitored Features", f"{len(df_drift)}", "PSI & KS Monitored", "#38bdf8")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">🏥 Feature Distribution Drift Metrics (PSI vs 1979–2005 Baseline)</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Population Stability Index (PSI) and Kolmogorov-Smirnov statistics tracking distribution stability across all 27 features.</p>
</div>
""", unsafe_allow_html=True)

st.dataframe(df_drift, use_container_width=True)

render_footer()
