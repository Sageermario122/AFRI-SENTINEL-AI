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

st.set_page_config(page_title="Event Timeline — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("EVENT TIMELINE")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"

@st.cache_data
def load_timeline_data():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['month', 'country_iso3'], ascending=[False, True], inplace=True)
    return df

df = load_timeline_data()

st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">⏱️ Multi-Source Event Log</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Chronological event streams aggregated across ACLED conflict events, GDELT news footprints, and GTD terrorism metrics.</p>
</div>
""", unsafe_allow_html=True)

selected_country = st.selectbox("Filter Country (ISO3)", ["All"] + sorted(df['country_iso3'].unique().tolist()))

if selected_country != "All":
    df_filtered = df[df['country_iso3'] == selected_country]
else:
    df_filtered = df

st.dataframe(
    df_filtered[['month', 'country_iso3', 'conflict_event_count', 'battle_count', 'protest_count', 'fatality_count', 'news_count', 'terrorism_event_count']].head(100),
    use_container_width=True
)

render_footer()
