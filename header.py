import streamlit as st

def render_ops_header(page_title="METHODOLOGY"):
    """
    Renders top Operations Center Header matching the reference mockup UI:
    📖 Page Title | ● LIVE | ● DATA CONNECTED | ● MODEL ONLINE | 🔄
    """
    st.markdown(f"""
    <div class="ops-header">
        <div class="ops-title">
            <span style="color: #38bdf8; margin-right: 0.5rem;">📖</span> {page_title.upper()}
        </div>
        <div class="ops-status-group">
            <div class="status-item">
                <span class="status-dot-green"></span> LIVE
            </div>
            <div class="status-item">
                <span class="status-dot-green"></span> DATA CONNECTED
            </div>
            <div class="status-item">
                <span class="status-dot-blue"></span> MODEL ONLINE
            </div>
            <div class="status-item" style="color: #94a3b8; margin-left: 0.5rem; cursor: pointer;">
                🔄
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
