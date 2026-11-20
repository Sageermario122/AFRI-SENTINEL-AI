import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DASHBOARD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path: sys.path.insert(0, PROJECT_ROOT)
if DASHBOARD_ROOT not in sys.path: sys.path.insert(0, DASHBOARD_ROOT)

import joblib
import json
import pandas as pd
import streamlit as st
from datetime import datetime

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

st.set_page_config(page_title="Real-Time Monitor — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("REAL-TIME MONITOR")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"
MODELS_DIR = r"D:\Geoplotics how it afftects millitary\models\trained"

@st.cache_data
def load_realtime_data():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    with open(os.path.join(MODELS_DIR, "feature_order.json")) as f:
        feature_cols = json.load(f)
    model = joblib.load(os.path.join(MODELS_DIR, "final_model.pkl"))
    
    train_medians = df[feature_cols].median()
    df['risk_prob'] = model.predict_proba(df[feature_cols].fillna(train_medians))[:, 1]
    df['risk_score_pct'] = df['risk_prob'] * 100
    return df, feature_cols

df, feature_cols = load_realtime_data()
latest_month = df['month'].max()

st.markdown(f"""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">📡 Live Country Escalation Score Monitor</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">
        Data Freshness: <span class="badge badge-fresh">FRESH</span> | 
        Latest Processed Month: <strong style="color: #38bdf8;">{latest_month}</strong> | 
        Last Refreshed: <strong>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</strong>
    </p>
</div>
""", unsafe_allow_html=True)

latest_df = df[df['month'] == latest_month].sort_values(by='risk_score_pct', ascending=False)
st.dataframe(
    latest_df[['country_iso3', 'month', 'risk_score_pct', 'conflict_event_count', 'news_count', 'negative_news_ratio']],
    use_container_width=True
)

render_footer()
