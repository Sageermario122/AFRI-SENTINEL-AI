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
    from dashboard.components.cards import render_metric_card
except ModuleNotFoundError:
    from components.styles import apply_global_styles
    from components.header import render_ops_header
    from components.sidebar import render_sidebar
    from components.footer import render_footer
    from components.cards import render_metric_card

st.set_page_config(page_title="Executive Overview — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("EXECUTIVE OVERVIEW & SYSTEM STATUS")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"

@st.cache_data
def load_overview_data():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    df['future_conflict_count'] = df.groupby('country_iso3')['conflict_event_count'].shift(-1)
    df['roll12m_conflict'] = df.groupby('country_iso3')['conflict_event_count'].transform(lambda s: s.rolling(12, min_periods=1).mean())
    df['target_C'] = df.apply(
        lambda r: 1 if (pd.notnull(r['future_conflict_count']) and r['future_conflict_count'] > (1.5 * r['roll12m_conflict'] + 1)) else 0,
        axis=1
    )
    return df

df = load_overview_data()
latest_month = df['month'].max()

st.markdown(f"""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">Executive Overview & System Parameters</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Explainable AI-powered monitoring of country-level conflict escalation signals ($T+1$).</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: render_metric_card("Monitored Countries", f"{df['country_iso3'].nunique()}", "Global Coverage", "#38bdf8")
with c2: render_metric_card("Total Historical Obs", f"{len(df):,}", "1979–2014 (35 Years)", "#38bdf8")
with c3: render_metric_card("Historical Holdout F1", "0.2910", "Test Period 2010–2014", "#a855f7")
with c4: render_metric_card("PR-AUC (1.60x Lift)", "0.2449", "Baseline = 0.1532", "#22c55e")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card" style="border-left: 4px solid #f97316;">
    <h4 style="color: #f97316; margin-top: 0;">⚠️ Mandatory Research Disclaimers & Ethics Framing</h4>
    <ul style="color: #cbd5e1; line-height: 1.7; font-size: 0.95rem;">
        <li>GeoIntel AI evaluates statistical probability thresholds of country-level conflict event escalation ($T+1$).</li>
        <li>It <strong>does NOT predict wars, military attacks, or tactical battle outcomes</strong>.</li>
        <li>Feature contributions (TreeSHAP values) represent <strong>statistical model inputs, NOT cause-and-effect relationships</strong>.</li>
        <li>Numerical risk scores are strictly computed by the validated XGBoost model; LLM text synthesis is decoupled and grounded in evidence.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

render_footer()
