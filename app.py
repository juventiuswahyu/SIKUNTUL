import streamlit as st
from groq import Groq
import base64
import requests
from datetime import datetime
import re

# ---------------------------------------------------------
# 1. Konfigurasi Halaman & Custom CSS (Light Mode Lock & Style)
# ---------------------------------------------------------
st.set_page_config(
    page_title="SIKUNTUL - Universitas Nasional Karangturi",
    page_icon="🎓",
    layout="centered"
)

if "form_key" not in st.session_state:
    st.session_state.form_key = 0

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return ""

bg_img_base64 = get_base64_of_bin_file("bd design uk (1).jpg")

st.markdown(
    f"""
    <style>
    /* Force Light Mode Color Overlay */
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #ffffff !important;
        color: #31333F !important;
    }}
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }}
    .header-container {{
        text-align: center;
        margin-top: -15px;
        margin-bottom: 10px;
    }}
    .header-title {{
        font-size: 2rem;
        font-weight: 700;
        margin-top: 0px;
        margin-bottom: 2px;
        line-height: 1.1;
    }}
    .header-subtitle {{
        font-size: 1.15rem;
        font-weight: 600;
        color: #31333F;
        margin-bottom: 4px;
        line-height: 1.2;
    }}
    .header-desc {{
        font-size: 0.9rem;
        color: #555555;
        line-height: 1.3;
    }}
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        border: 2.5px solid #800000 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        background-color: #ffffff;
        background-image: url("data:image/jpeg;base64,{bg_img_base64}");
        background-repeat: no-repeat;
        background-position: bottom center;
        background-size: contain;
        box-shadow: 0 4px 6px rgba(128, 0, 0, 0.08);
    }}
    div[aria-label="stRadio"] {{
        margin-bottom: -5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Helper Function: Kirim ke Google Apps Script Webhook
# ---------------------------------------------------------
def save_to_apps_script(payload):
    try:
        webhook_url = st.secrets["GSHEET_WEBHOOK_URL"]
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            return True
        else:
            st.error(f"Gagal menyimpan ke Apps Script. Status Code: {response.status_code}")
            return False
    except Exception as e:
        st.error(f"Terjadi kesalahan saat koneksi Apps Script: {e}")
        return False

# ---------------------------------------------------------
# Header & UI Layout
# ---------------------------------------------------------
col_left, col_logo, col_right = st.columns([1.3, 1.4, 1.3])
with col_logo:
    st.image("logo (2).png", use_container_width=True)

st.markdown(
    """
    <div class="header-container">
        <div class="header-title">SIKUNTUL</div>
        <div class="header-subtitle">Sistem Konsultasi untuk Menentukan Tujuan Kuliah</div>
        <div class="header-desc">Isi data diri dan pilih jawaban yang paling mencerminkan dirimu untuk mendapatkan analisis rekomendasi jurusan komprehensif beserta rincian biayanya!</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 2. Form Kuesioner
# ---------------------------------------------------------
