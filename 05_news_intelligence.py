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
    from dashboard.components.cards import render_news_card
except ModuleNotFoundError:
    from components.styles import apply_global_styles
    from components.header import render_ops_header
    from components.sidebar import render_sidebar
    from components.footer import render_footer
    from components.cards import render_news_card

st.set_page_config(page_title="News Intelligence — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("NEWS INTELLIGENCE")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"

@st.cache_data
def load_news_data():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    return df

df = load_news_data()

st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">📰 Real-World GDELT Media Footprint</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Article volumes, sentiment tone, and Goldstein conflict-cooperation scales.</p>
</div>
""", unsafe_allow_html=True)

selected_country = st.selectbox("Select Country (ISO3)", sorted(df['country_iso3'].unique()))
c_df = df[df['country_iso3'] == selected_country].sort_values(by='month', ascending=False)

st.subheader(f"Recent GDELT Media Metrics for {selected_country}")
st.dataframe(
    c_df[['month', 'news_count', 'conflict_news_count', 'negative_news_ratio', 'average_news_tone', 'average_goldstein_scale', 'news_growth_rate']].head(24),
    use_container_width=True
)

render_footer()
