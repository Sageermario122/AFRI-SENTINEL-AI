import streamlit as st

def render_metric_card(title, value, subtitle="", border_color="#38bdf8"):
    st.markdown(f"""
    <div class="metric-card" style="border-top: 3px solid {border_color};">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def render_news_card(title, source, timestamp, country, tone, goldstein, url=None):
    tone_color = "#22c55e" if tone >= 0 else "#ef4444"
    st.markdown(f"""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
            <div style="font-weight: 700; font-size: 1rem; color: #f8fafc;">📰 {title}</div>
            <span class="badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">{country}</span>
        </div>
        <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 0.8rem;">
            Source: <strong style="color: #cbd5e1;">{source}</strong> | Date: <strong>{timestamp}</strong>
        </div>
        <div style="display: flex; gap: 1rem; font-size: 0.8rem;">
            <div>Media Tone: <strong style="color: {tone_color};">{tone:+.2f}</strong></div>
            <div>Goldstein Scale: <strong style="color: #38bdf8;">{goldstein:+.1f}</strong></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_alert_card(severity, country, message, month, abs_change):
    badge_class = f"badge-{severity.lower()}"
    st.markdown(f"""
    <div class="glass-card" style="border-left: 4px solid {'#ef4444' if severity=='HIGH' else ('#f97316' if severity=='ELEVATED' else '#eab308')};">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span class="badge {badge_class}">🚨 {severity} SIGNAL</span>
            <span style="font-size: 0.8rem; color: #94a3b8;">Country: <strong>{country}</strong> ({month})</span>
        </div>
        <div style="font-weight: 600; font-size: 1.05rem; color: #f8fafc; margin-bottom: 0.5rem;">
            {message}
        </div>
        <div style="font-size: 0.8rem; color: #94a3b8;">
            Statistical Probability Change: <strong style="color: #38bdf8;">{abs_change*100:+.1f}%</strong> | Disclaimer: Model signal output, not war prediction.
        </div>
    </div>
    """, unsafe_allow_html=True)
