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

st.set_page_config(page_title="Explainable AI — GeoIntel AI", layout="wide", initial_sidebar_state="expanded")
apply_global_styles()
render_sidebar()
render_ops_header("EXPLAINABLE AI")

EVAL_DIR = r"D:\Geoplotics how it afftects millitary\outputs\evaluation"
FIGURES_DIR = r"D:\Geoplotics how it afftects millitary\outputs\figures"

st.markdown("""
<div class="hero-banner">
    <h2 style="color: #f8fafc; font-weight: 800; font-size: 1.85rem; margin-bottom: 0.4rem;">🧠 TreeSHAP Global Feature Contributions</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 0;">SHAP values quantify statistical model contributions to risk scores. They do NOT represent cause-and-effect relationships.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("SHAP Feature Importance (Bar Plot)")
    bar_img = os.path.join(FIGURES_DIR, "shap_bar.png")
    if os.path.exists(bar_img):
        st.image(bar_img, use_container_width=True)
    else:
        st.info("SHAP Bar plot image generating...")

with col2:
    st.subheader("SHAP Summary Impact (Beeswarm Plot)")
    beeswarm_img = os.path.join(FIGURES_DIR, "shap_summary.png")
    if os.path.exists(beeswarm_img):
        st.image(beeswarm_img, use_container_width=True)
    else:
        st.info("SHAP Summary plot image generating...")

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Feature Importance Ranking Table")
fi_csv = os.path.join(EVAL_DIR, "feature_importance.csv")
if os.path.exists(fi_csv):
    st.dataframe(pd.read_csv(fi_csv), use_container_width=True)

render_footer()
