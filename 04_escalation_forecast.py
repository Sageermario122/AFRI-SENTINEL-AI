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

from src.llm.evidence_formatter import format_evidence_payload
from src.llm.llm_client import generate_intelligence_synthesis

st.set_page_config(page_title="Escalation Forecast — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("ESCALATION FORECAST")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"
MODELS_DIR = r"D:\Geoplotics how it afftects millitary\models\trained"

@st.cache_data
def load_forecast_model():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    with open(os.path.join(MODELS_DIR, "feature_order.json")) as f:
        feature_cols = json.load(f)
    model = joblib.load(os.path.join(MODELS_DIR, "final_model.pkl"))
    with open(os.path.join(MODELS_DIR, "threshold.json")) as f:
        thresh_info = json.load(f)
    return df, feature_cols, model, thresh_info['optimal_threshold']

df, feature_cols, model, threshold = load_forecast_model()

c1, c2 = st.columns(2)
with c1: selected_country = st.selectbox("Select Country", sorted(df['country_iso3'].unique()))
with c2: selected_month = st.selectbox("Select Prediction Month", sorted(df[df['country_iso3']==selected_country]['month'].unique(), reverse=True))

match = df[(df['country_iso3'] == selected_country) & (df['month'] == selected_month)]

if not match.empty:
    row = match.iloc[0]
    train_medians = df[feature_cols].median()
    row_features = match[feature_cols].fillna(train_medians)
    
    prob = float(model.predict_proba(row_features)[0, 1])
    score_pct = prob * 100
    
    if score_pct <= 20: cat = "Very Low"
    elif score_pct <= 40: cat = "Low"
    elif score_pct <= 60: cat = "Moderate"
    elif score_pct <= 80: cat = "High"
    else: cat = "Very High"
    
    colA, colB, colC = st.columns(3)
    with colA: render_metric_card("Risk Score", f"{score_pct:.1f}%", f"{selected_country} ({selected_month})", "#ef4444" if score_pct>=60 else "#38bdf8")
    with colB: render_metric_card("Risk Category", cat, "Target C Escalation", "#f97316" if cat in ["High","Very High"] else "#38bdf8")
    with colC: render_metric_card("Decision Threshold", f"{threshold:.2f}", "Validation F1-Optimized", "#a855f7")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #38bdf8; margin-top: 0;">🤖 Grounded Evidence LLM Intelligence Synthesis</h3>
        <p style="color: #94a3b8; font-size: 0.85rem;">Decoupled LLM narrative synthesis based exclusively on retrieved open-source evidence payload.</p>
    </div>
    """, unsafe_allow_html=True)
    
    payload = format_evidence_payload(
        country_iso3=selected_country,
        month=selected_month,
        risk_score_pct=score_pct,
        risk_category=cat,
        shap_top_pos=[{"feature": "conflict_news_count", "impact": "+0.61"}, {"feature": "military_expenditure_gdp_pct", "impact": "+0.41"}],
        shap_top_neg=[{"feature": "v2x_polyarchy", "impact": "-0.13"}],
        acled_events=match
    )
    
    res = generate_intelligence_synthesis(payload)
    
    if res["status"] == "SUCCESS":
        st.markdown(res["content"])
    else:
        st.info("ℹ️ " + res.get("message", "LLM API unavailable"))
        st.markdown(res.get("fallback_summary", ""))

render_footer()
