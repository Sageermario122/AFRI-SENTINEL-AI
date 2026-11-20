import streamlit as st

def render_footer():
    """
    Renders footer matching the exact reference mockup UI:
    👤 Prem Kumar T  |  📅 2026  |  🌐 GeoIntel AI
    """
    st.markdown("""
    <div class="footer-container">
        <div><span style="color: #38bdf8;">👤</span> Prem Kumar T</div>
        <div style="color: rgba(255,255,255,0.2);">|</div>
        <div><span style="color: #38bdf8;">📅</span> 2026</div>
        <div style="color: rgba(255,255,255,0.2);">|</div>
        <div><span style="color: #38bdf8;">🌐</span> GeoIntel AI</div>
    </div>
    """, unsafe_allow_html=True)
