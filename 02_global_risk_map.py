import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DASHBOARD_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path: sys.path.insert(0, PROJECT_ROOT)
if DASHBOARD_ROOT not in sys.path: sys.path.insert(0, DASHBOARD_ROOT)

import joblib
import json
import pandas as pd
import plotly.express as px
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

st.set_page_config(page_title="Global Risk Map — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("GLOBAL RISK MAP")

PROCESSED_CSV = r"D:\Geoplotics how it afftects millitary\datasets\processed\final_dataset\country_month_features.csv"
MODELS_DIR = r"D:\Geoplotics how it afftects millitary\models\trained"

@st.cache_data
def load_map_data():
    df = pd.read_csv(PROCESSED_CSV)
    df.sort_values(by=['country_iso3', 'month'], inplace=True)
    
    with open(os.path.join(MODELS_DIR, "feature_order.json")) as f:
        feature_cols = json.load(f)
        
    model = joblib.load(os.path.join(MODELS_DIR, "final_model.pkl"))
    
    train_medians = df[feature_cols].median()
    X_all = df[feature_cols].fillna(train_medians)
    
    df['risk_prob'] = model.predict_proba(X_all)[:, 1]
    df['risk_score_pct'] = df['risk_prob'] * 100
    
    return df, feature_cols

df, feature_cols = load_map_data()

st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">Global Conflict Escalation Risk Score Map</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">Interactive global mapping displaying Target C escalation risk probabilities computed by the frozen XGBoost model ($T+1$).</p>
</div>
""", unsafe_allow_html=True)

selected_month = st.selectbox("Select Timeline Month", sorted(df['month'].unique(), reverse=True))
df_month = df[df['month'] == selected_month].copy()

def assign_cat(p):
    if p <= 20: return "Very Low"
    elif p <= 40: return "Low"
    elif p <= 60: return "Moderate"
    elif p <= 80: return "High"
    else: return "Very High"
    
df_month['risk_category'] = df_month['risk_score_pct'].apply(assign_cat)

fig = px.choropleth(
    df_month,
    locations="country_iso3",
    color="risk_score_pct",
    hover_name="country_iso3",
    hover_data=["risk_category", "conflict_event_count", "news_count"],
    color_continuous_scale="Reds",
    range_color=[0, 100],
    title=f"Global Conflict Escalation Risk Score (%) — {selected_month}"
)
fig.update_layout(
    height=600, 
    margin={"r":0,"t":40,"l":0,"b":0},
    paper_bgcolor='rgba(15, 23, 42, 0.75)',
    plot_bgcolor='rgba(15, 23, 42, 0.75)',
    font=dict(color='#f8fafc')
)
st.plotly_chart(fig, use_container_width=True)

st.markdown(f"### Country Risk Rankings for {selected_month}")
st.dataframe(
    df_month[['country_iso3', 'risk_score_pct', 'risk_category', 'conflict_event_count', 'news_count']].sort_values(by="risk_score_pct", ascending=False), 
    use_container_width=True
)

render_footer()
