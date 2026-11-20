import os
import base64
import streamlit as st

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def apply_global_styles():
    """
    Injects Operations Center styling matching the reference mockup UI:
    Hides default sidebar nav list and styles custom page_link navigation sections.
    """
    bg_path = r"D:\Geoplotics how it afftects millitary\assets\images\world_map_dark.jpg"
    base64_bg = get_base64_image(bg_path)
    
    bg_style = f"""
        background: linear-gradient(180deg, rgba(11, 19, 41, 0.80) 0%, rgba(15, 23, 42, 0.92) 100%), 
                    url("data:image/jpeg;base64,{base64_bg}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center top;
    """ if base64_bg else """
        background: linear-gradient(135deg, #0b1329 0%, #0f172a 100%);
    """

    st.markdown(f"""
    <style>
    /* Global Application Theme */
    .stApp {{
        {bg_style}
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    /* Main Container Padding */
    .main .block-container {{
        padding-top: 0.8rem;
        padding-bottom: 2rem;
        max-width: 1440px;
    }}

    /* Hide Streamlit Default Components for Operations Center Look */
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    header[data-testid="stHeader"] {{ background: transparent !important; }}
    
    /* Hide Default Auto-Generated Sidebar Navigation List */
    div[data-testid="stSidebarNav"] {{ display: none !important; }}

    /* TRANSPARENT GLASSMORPHISM SIDEBAR */
    section[data-testid="stSidebar"] {{
        background-color: rgba(11, 19, 41, 0.45) !important;
        backdrop-filter: blur(24px) !important;
        -webkit-backdrop-filter: blur(24px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 4px 0 28px rgba(0, 0, 0, 0.5);
    }}

    section[data-testid="stSidebar"] > div {{
        background-color: transparent !important;
        padding-top: 1rem !important;
    }}

    /* Custom Page Link Items in Sidebar */
    section[data-testid="stSidebar"] [data-testid="stPageLink"] a {{
        background-color: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.04) !important;
        border-radius: 8px !important;
        margin-bottom: 0.25rem !important;
        transition: all 0.2s ease !important;
        color: #cbd5e1 !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
        padding: 0.55rem 0.85rem !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {{
        background-color: rgba(56, 189, 248, 0.12) !important;
        border-color: rgba(56, 189, 248, 0.4) !important;
        color: #38bdf8 !important;
        transform: translateX(4px) !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] {{
        background-color: rgba(56, 189, 248, 0.18) !important;
        border-left: 3px solid #38bdf8 !important;
        border-color: rgba(56, 189, 248, 0.4) !important;
        color: #f8fafc !important;
        font-weight: 600 !important;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.2);
    }}

    /* Sidebar Section Title */
    .sidebar-section-title {{
        font-size: 0.7rem;
        font-weight: 700;
        color: #38bdf8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 1rem;
        margin-bottom: 0.4rem;
    }}

    /* Glassmorphism Panel Cards */
    .glass-card {{
        background: rgba(15, 23, 42, 0.76);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.4rem;
        margin-bottom: 1.1rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }}

    .glass-card:hover {{
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.35);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5);
    }}

    /* Hero Banner Header with Map Background */
    .hero-banner {{
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.6) 0%, rgba(15, 23, 42, 0.85) 100%), 
                    url("data:image/jpeg;base64,{base64_bg}");
        background-size: cover;
        background-position: center;
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 2.2rem 1.5rem;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    }}

    /* Formula Box Container */
    .formula-box {{
        background: rgba(10, 15, 30, 0.88);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 10px;
        padding: 1.3rem;
        text-align: center;
        margin: 1.2rem 0;
        box-shadow: inset 0 0 16px rgba(56, 189, 248, 0.08);
    }}

    /* Metric Cards */
    .metric-card {{
        background: rgba(30, 41, 59, 0.55);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .metric-card:hover {{
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.4);
    }}

    .metric-title {{
        font-size: 0.8rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.3rem;
    }}

    .metric-value {{
        font-size: 1.75rem;
        font-weight: 700;
        color: #f8fafc;
    }}

    .metric-subtitle {{
        font-size: 0.75rem;
        color: #38bdf8;
        margin-top: 0.2rem;
    }}

    /* Operations Center Top Header Bar */
    .ops-header {{
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 0.75rem 1.4rem;
        margin-bottom: 1.2rem;
        border-radius: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }}

    .ops-title {{
        font-size: 1.2rem;
        font-weight: 700;
        color: #f8fafc;
        letter-spacing: 0.02em;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }}

    .ops-status-group {{
        display: flex;
        gap: 1.2rem;
        align-items: center;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.03em;
    }}

    .status-item {{
        display: flex;
        align-items: center;
        gap: 0.45rem;
        color: #cbd5e1;
    }}

    .status-dot-green {{
        height: 7px; width: 7px; background-color: #22c55e; border-radius: 50%; display: inline-block; box-shadow: 0 0 6px #22c55e;
    }}
    .status-dot-blue {{
        height: 7px; width: 7px; background-color: #38bdf8; border-radius: 50%; display: inline-block; box-shadow: 0 0 6px #38bdf8;
    }}

    /* Sidebar Status Box */
    .sidebar-status-card {{
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 8px;
        padding: 0.75rem;
        margin-top: 1.5rem;
    }}

    /* Footer Container */
    .footer-container {{
        text-align: center;
        padding: 1.2rem 0;
        margin-top: 2.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        color: #94a3b8;
        font-size: 0.85rem;
        display: flex;
        justify-content: center;
        gap: 2.5rem;
        align-items: center;
        font-weight: 500;
    }}
    </style>
    """, unsafe_allow_html=True)
