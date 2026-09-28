```python
import os
import base64

import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Credit Risk Intelligence",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PREMIUM UI STYLING
# ============================================================
def load_background(path):
    """
    Loads the existing project background image if available.
    The original project path is preserved.
    """
    if not os.path.exists(path):
        return ""

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


background_image = load_background(
    "Project Images/credit_risk_background.webp.webp"
)


background_css = ""

if background_image:
    background_css = f"""
    .stApp {{
        background:
            linear-gradient(
                135deg,
                rgba(11, 18, 32, 0.96),
                rgba(17, 24, 39, 0.93)
            ),
            url("data:image/webp;base64,{background_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """

else:
    background_css = """
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(37, 99, 235, 0.14),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(124, 58, 237, 0.12),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #0B1220 0%,
                #111827 50%,
                #0B1220 100%
            );
    }
    """


st.markdown(
    f"""
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    {background_css}

    .stApp {{
        color: #F8FAFC;
    }}

    .main .block-container {{
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: #F8FAFC !important;
        letter-spacing: -0.02em;
    }}

    p, label, span {{
        color: #CBD5E1;
    }}

    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {{
        background:
            linear-gradient(
                180deg,
                #0B1220 0%,
                #111827 55%,
                #0B1220 100%
            );
        border-right: 1px solid rgba(148, 163, 184, 0.12);
    }}

    section[data-testid="stSidebar"] > div {{
        padding-top: 1.5rem;
    }}

    .sidebar-brand {{
        padding: 18px;
        border-radius: 18px;
        background:
            linear-gradient(
                135deg,
                rgba(37, 99, 235, 0.18),
                rgba(124, 58, 237, 0.14)
            );
        border: 1px solid rgba(96, 165, 250, 0.18);
        margin-bottom: 20px;
    }}

    .sidebar-brand-title {{
        font-size: 20px;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 5px;
    }}

    .sidebar-brand-subtitle {{
        font-size: 13px;
        color: #94A3B8;
        line-height: 1.5;
    }}

    .sidebar-section {{
        color: #64748B;
        text-transform: uppercase;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.12em;
        margin: 24px 0 10
```
