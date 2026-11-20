import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DASHBOARD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path: sys.path.insert(0, PROJECT_ROOT)
if DASHBOARD_ROOT not in sys.path: sys.path.insert(0, DASHBOARD_ROOT)

import joblib
import json
import pandas as pd
import plotly.graph_objects as go
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

st.set_page_config(page_title="Country Intelligence — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("COUNTRY INTELLIGENCE")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"

@st.cache_data
def load_country_data():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    df['future_conflict_count'] = df.groupby('country_iso3')['conflict_event_count'].shift(-1)
    df['roll12m_conflict'] = df.groupby('country_iso3')['conflict_event_count'].transform(lambda s: s.rolling(12, min_periods=1).mean())
    df['escalation_threshold'] = 1.5 * df['roll12m_conflict'] + 1
    return df

df = load_country_data()

selected_country = st.selectbox("Select Country (ISO3)", sorted(df['country_iso3'].unique()))
c_df = df[df['country_iso3'] == selected_country].copy()

st.markdown(f"""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">🏛️ Country Profile: {selected_country}</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Historical conflict activity, 12-month baseline mean, and Target C escalation threshold trajectory.</p>
</div>
""", unsafe_allow_html=True)

fig = go.Figure()
fig.add_trace(go.Scatter(x=c_df['month'], y=c_df['conflict_event_count'], mode='lines+markers', name='Monthly Conflict Events', line=dict(color='#ef4444', width=2)))
fig.add_trace(go.Scatter(x=c_df['month'], y=c_df['roll12m_conflict'], mode='lines', name='12-Month Rolling Mean Baseline', line=dict(color='#38bdf8', dash='dash')))
fig.add_trace(go.Scatter(x=c_df['month'], y=c_df['escalation_threshold'], mode='lines', name='Target C Threshold (1.5x + 1)', line=dict(color='#f97316', dash='dot')))

fig.update_layout(
    title=f"Conflict Event Activity vs Rolling Historical Baseline — {selected_country}", 
    xaxis_title="Month", 
    yaxis_title="Event Count", 
    height=500,
    paper_bgcolor='rgba(15, 23, 42, 0.75)',
    plot_bgcolor='rgba(15, 23, 42, 0.75)',
    font=dict(color='#f8fafc')
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Country Summary Data")
st.dataframe(c_df[['month', 'conflict_event_count', 'roll12m_conflict', 'escalation_threshold', 'news_count', 'fatality_count']].tail(12), use_container_width=True)

render_footer()
