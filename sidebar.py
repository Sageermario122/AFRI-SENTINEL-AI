import os
import streamlit as st
from datetime import datetime, timezone


def _page_link_safe(path, label, icon):
    """Render a page_link; if the page file is missing, show a warning instead
    of silently hiding it. Silent hiding is worse than visible breakage on
    demo day."""
    if not os.path.exists(path):
        st.sidebar.markdown(
            f'<div style="font-size:0.8rem;color:#f87171;padding:0.15rem 0.5rem;">'
            f'⚠ {icon} {label} (missing: {path})</div>',
            unsafe_allow_html=True,
        )
        return
    try:
        st.sidebar.page_link(path, label=label, icon=icon)
    except Exception as e:
        st.sidebar.markdown(
            f'<div style="font-size:0.8rem;color:#f87171;padding:0.15rem 0.5rem;">'
            f'⚠ {icon} {label} (error: {type(e).__name__})</div>',
            unsafe_allow_html=True,
        )


def render_sidebar():
    """Sidebar navigation for AFRI-SENTINEL AI."""
    # Header — AFRI-SENTINEL AI, Africa-scoped
    st.sidebar.markdown("""
    <div style="padding-bottom: 0.8rem; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 0.8rem;">
        <div style="font-size: 1.3rem; font-weight: 800; color: #f8fafc; display: flex; align-items: center; gap: 0.5rem;">
            <span style="color: #38bdf8;">🌍</span> AFRI-SENTINEL AI
        </div>
        <div style="font-size: 0.78rem; color: #94a3b8; font-weight: 500; margin-top: 0.2rem; line-height: 1.3;">
            Explainable Early-Warning for Africa
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section 1: INTELLIGENCE
    st.sidebar.markdown(
        '<div class="sidebar-section-title">INTELLIGENCE</div>',
        unsafe_allow_html=True,
    )
    _page_link_safe("pages/01_overview.py", "Overview", "🏠")
    _page_link_safe("pages/02_africa_risk_map.py", "Africa Risk Map", "🌍")
    _page_link_safe("pages/03_country_intelligence.py", "Country Intelligence", "📍")
    _page_link_safe("pages/04_escalation_forecast.py", "Escalation Forecast", "📈")
    _page_link_safe("pages/05_news_intelligence.py", "News Intelligence", "📰")

    # Section 2: ANALYTICS
    st.sidebar.markdown(
        '<div class="sidebar-section-title">ANALYTICS</div>',
        unsafe_allow_html=True,
    )
    _page_link_safe("pages/06_explainable_ai.py", "Explainable AI", "🧠")
    _page_link_safe("pages/07_event_timeline.py", "Event Timeline", "📅")

    # Section 3: MONITORING (renamed from "Real-Time")
    st.sidebar.markdown(
        '<div class="sidebar-section-title">MONITORING</div>',
        unsafe_allow_html=True,
    )
    _page_link_safe("pages/09_realtime_monitor.py", "Scheduled Monitor", "📡")
    _page_link_safe("pages/10_alert_center.py", "Alert Center", "🚨")
    _page_link_safe("pages/11_system_health.py", "System Health", "💻")

    # Section 4: DOCUMENTATION
    st.sidebar.markdown(
        '<div class="sidebar-section-title">DOCUMENTATION</div>',
        unsafe_allow_html=True,
    )
    _page_link_safe("pages/08_methodology.py", "Methodology", "📖")

    # Bottom status card — computed, not hardcoded
    now_utc = datetime.now(timezone.utc).strftime("%d %b %Y • %H:%M UTC")

    # Read status from environment or a config file; default to "DEMO"
    system_status = os.getenv("AFRI_SENTINEL_STATUS", "DEMO").upper()
    status_colors = {
        "OPERATIONAL": ("#4ade80", "status-dot-green"),
        "DEMO":        ("#38bdf8", "status-dot-blue"),
        "CONDITIONAL": ("#fbbf24", "status-dot-amber"),
        "DEGRADED":    ("#f87171", "status-dot-red"),
    }
    status_color, status_dot_class = status_colors.get(
        system_status, ("#94a3b8", "status-dot-grey")
    )

    st.sidebar.markdown(f"""
    <div class="sidebar-status-card">
        <div style="font-size: 0.78rem; font-weight: 700; color: {status_color}; display: flex; align-items: center; gap: 0.4rem;">
            <span class="{status_dot_class}"></span> {system_status}
        </div>
        <div style="font-size: 0.7rem; color: #64748b; margin-top: 0.3rem;">
            Rendered: {now_utc}
        </div>
        <div style="font-size: 0.65rem; color: #475569; margin-top: 0.15rem;">
            Research prototype — not for operational use
        </div>
    </div>
    """, unsafe_allow_html=True)