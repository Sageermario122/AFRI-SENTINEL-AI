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
    from dashboard.components.cards import render_alert_card
except ModuleNotFoundError:
    from components.styles import apply_global_styles
    from components.header import render_ops_header
    from components.sidebar import render_sidebar
    from components.footer import render_footer
    from components.cards import render_alert_card

from src.realtime.alert_engine import evaluate_risk_change_alerts

st.set_page_config(page_title="Alert Center — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("ALERT CENTER")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"

@st.cache_data
def load_alerts():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    
    alerts = []
    for country, grp in df.groupby('country_iso3'):
        if len(grp) >= 2:
            last = grp.iloc[-1]
            prev = grp.iloc[-2]
            
            prob_curr = min(1.0, max(0.0, last['conflict_event_count'] / 50.0))
            prob_prev = min(1.0, max(0.0, prev['conflict_event_count'] / 50.0))
            
            alert = evaluate_risk_change_alerts(prob_curr, prob_prev, country, last['month'])
            alerts.append(alert)
            
    return pd.DataFrame(alerts)

df_alerts = load_alerts()

st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">🚨 Automated Escalation Risk Change Signals</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Safe alert language: Alerts indicate statistical model signal increases, NEVER war or attack predictions.</p>
</div>
""", unsafe_allow_html=True)

severity_filter = st.multiselect("Filter Severity", ["HIGH", "ELEVATED", "WATCH", "INFO"], default=["HIGH", "ELEVATED"])

filtered_alerts = df_alerts[df_alerts['severity'].isin(severity_filter)].sort_values(by="absolute_change", ascending=False)

st.markdown("---")
for _, r in filtered_alerts.head(10).iterrows():
    render_alert_card(
        severity=r['severity'],
        country=r['country_iso3'],
        message=r['alert_message'],
        month=r['prediction_month'],
        abs_change=r['absolute_change']
    )

render_footer()
