import streamlit as st
from water_stress_page import show_water_page
from irrigation_page import show_irrigation_page
from project_guide_page import show_project_guide

st.set_page_config(
    page_title=" Smart Water Intelligence",
    layout="wide",
    page_icon="💧",
    initial_sidebar_state="expanded"
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #050d1a !important;
    color: #c8dff5 !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Animated mesh background ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 50% at 20% 10%, rgba(0,120,200,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(0,60,140,0.15) 0%, transparent 55%),
        radial-gradient(ellipse 40% 60% at 50% 50%, rgba(0,30,80,0.08) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071628 0%, #040e1e 100%) !important;
    border-right: 1px solid rgba(0,140,255,0.12) !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-family: 'DM Sans', sans-serif !important;
    color: #7ab3d8 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.02em;
}
[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {
    color: #a0c8e8 !important;
}

/* ── Header ── */
h1, h2, h3, h4 {
    font-family: 'Syne', sans-serif !important;
    letter-spacing: -0.02em;
}

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: rgba(0, 100, 200, 0.08) !important;
    border: 1px solid rgba(0, 140, 255, 0.18) !important;
    border-radius: 12px !important;
    padding: 1rem 1.25rem !important;
    backdrop-filter: blur(8px) !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    color: #5bc8fa !important;
    font-size: 1.8rem !important;
}
[data-testid="stMetricLabel"] {
    color: #6a9abf !important;
    font-size: 0.8rem !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #0070c0 0%, #003d82 100%) !important;
    color: #e8f4ff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em !important;
    padding: 0.6rem 1.8rem !important;
    font-size: 0.9rem !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(0, 100, 200, 0.35) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(0, 140, 255, 0.45) !important;
    background: linear-gradient(135deg, #0088e0 0%, #0050a8 100%) !important;
}

/* ── Inputs ── */
.stNumberInput input, .stSlider, .stSelectbox select,
[data-testid="stSelectbox"] > div {
    background: rgba(10, 30, 60, 0.6) !important;
    border-color: rgba(0, 120, 220, 0.25) !important;
    color: #c8e4f8 !important;
    border-radius: 8px !important;
}
[data-baseweb="select"] {
    background: rgba(10, 30, 60, 0.6) !important;
}
[data-baseweb="select"] > div {
    background: rgba(10, 30, 60, 0.6) !important;
    border-color: rgba(0, 120, 220, 0.25) !important;
    color: #c8e4f8 !important;
    border-radius: 8px !important;
}

/* ── Alerts ── */
.stAlert {
    border-radius: 10px !important;
    border-left-width: 4px !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Plotly chart container ── */
.js-plotly-plot {
    border-radius: 14px !important;
    overflow: hidden;
}

/* ── Dividers ── */
hr {
    border-color: rgba(0, 100, 200, 0.15) !important;
}

/* ── Subheader text ── */
[data-testid="stMarkdownContainer"] h3 {
    color: #4db8f0 !important;
    font-size: 1.4rem !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #050d1a; }
::-webkit-scrollbar-thumb { background: #1a4a80; border-radius: 3px; }

/* ══════════════════════════════════════════
   FLOATING BUBBLES — minimized, subtle
   - Max size: 14px
   - Only 10 bubbles (down from 28)
   - Slower rise: 28s–42s duration
   - Lower opacity: max 0.35
   - Minimal sway (--sw reduced to ±8px)
   ══════════════════════════════════════════ */
.bubble-wrap {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9999;
    overflow: hidden;
}
.b {
    position: absolute;
    bottom: -30px;
    border-radius: 50%;
    opacity: 0;
    animation: rise linear infinite;
}
.b::after {
    content: '';
    position: absolute;
    top: 18%; left: 22%;
    width: 28%; height: 18%;
    background: rgba(255,255,255,0.20);
    border-radius: 50%;
    filter: blur(1px);
}
.ba {
    background: radial-gradient(circle at 35% 35%, rgba(100,200,255,0.40) 0%, rgba(0,120,220,0.10) 55%, transparent 100%);
    border: 1px solid rgba(100,200,255,0.22);
    box-shadow: inset 0 0 4px rgba(255,255,255,0.10);
}
.bb {
    background: radial-gradient(circle at 35% 35%, rgba(60,220,255,0.32) 0%, rgba(0,80,180,0.08) 55%, transparent 100%);
    border: 1px solid rgba(60,220,255,0.18);
    box-shadow: inset 0 0 4px rgba(255,255,255,0.08);
}
.bc {
    background: radial-gradient(circle at 35% 35%, rgba(180,240,255,0.25) 0%, rgba(0,60,140,0.06) 55%, transparent 100%);
    border: 1px solid rgba(180,240,255,0.14);
}
@keyframes rise {
    0%   { transform: translateY(0)      translateX(0px)      scale(1.00); opacity: 0;    }
    8%   {                                                                  opacity: 0.35; }
    50%  { transform: translateY(-52vh)  translateX(var(--sw)) scale(1.02); opacity: 0.28; }
    92%  {                                                                  opacity: 0.12; }
    100% { transform: translateY(-112vh) translateX(0px)      scale(0.90); opacity: 0;    }
}
</style>
""", unsafe_allow_html=True)

# ── Bubble HTML — 10 bubbles, all ≤14px, slow & subtle ──────────────────────
st.markdown("""
<div class="bubble-wrap">
  <div class="b ba" style="width:8px; height:8px; left:6vw;  animation-duration:32s;animation-delay:-4s;  --sw:6px"></div>
  <div class="b bb" style="width:12px;height:12px;left:15vw; animation-duration:38s;animation-delay:-14s; --sw:-7px"></div>
  <div class="b bc" style="width:6px; height:6px; left:24vw; animation-duration:28s;animation-delay:-8s;  --sw:5px"></div>
  <div class="b ba" style="width:14px;height:14px;left:34vw; animation-duration:42s;animation-delay:-22s; --sw:-8px"></div>
  <div class="b bb" style="width:8px; height:8px; left:44vw; animation-duration:35s;animation-delay:-3s;  --sw:7px"></div>
  <div class="b bc" style="width:10px;height:10px;left:54vw; animation-duration:30s;animation-delay:-18s; --sw:-6px"></div>
  <div class="b ba" style="width:6px; height:6px; left:63vw; animation-duration:40s;animation-delay:-11s; --sw:8px"></div>
  <div class="b bb" style="width:12px;height:12px;left:73vw; animation-duration:36s;animation-delay:-26s; --sw:-5px"></div>
  <div class="b bc" style="width:8px; height:8px; left:82vw; animation-duration:33s;animation-delay:-7s;  --sw:6px"></div>
  <div class="b ba" style="width:10px;height:10px;left:91vw; animation-duration:39s;animation-delay:-16s; --sw:-7px"></div>
</div>
""", unsafe_allow_html=True)

# ── Hero Banner ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="
    padding: 2.5rem 2rem 2rem;
    background: linear-gradient(135deg, rgba(0,60,140,0.25) 0%, rgba(0,20,60,0.1) 100%);
    border: 1px solid rgba(0,140,255,0.12);
    border-radius: 18px;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
">
  <div style="
    position: absolute; top:-40px; right:-40px;
    width:200px; height:200px; border-radius:50%;
    background: radial-gradient(circle, rgba(0,140,255,0.12), transparent 70%);
  "></div>
  <div style="position:relative;">
    <p style="
        font-family:'Syne',sans-serif;
        font-size:2.4rem;
        font-weight:800;
        color:#e0f2ff;
        margin:0 0 0.4rem;
        letter-spacing:-0.03em;
        line-height:1.1;
    ">💧 Smart Water Crisis & Irrigation Intelligence</p>
    <p style="
        font-family:'Syne',sans-serif;
        font-size:1rem;
        font-weight:600;
        color:#4db8f0;
        margin:0 0 0.8rem;
        letter-spacing:0.15em;
        text-transform:uppercase;
    ">Intelligent Water Management Solutions</p>
    <p style="
        font-family:'DM Sans',sans-serif;
        font-size:0.95rem;
        color:#7aadce;
        margin:0;
        max-width:560px;
        font-weight:300;
        line-height:1.6;
    ">Real-time AI analytics for groundwater stress prediction and irrigation efficiency — district-level intelligence at your fingertips.</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.markdown("""
<div style="
    font-family:'Syne',sans-serif;
    font-size:1.05rem;
    font-weight:700;
    color:#4db8f0;
    letter-spacing:0.12em;
    text-transform:uppercase;
    margin-bottom:0.5rem;
    padding-bottom:0.75rem;
    border-bottom:1px solid rgba(0,140,255,0.15);
">Modules</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "",
    ["Project Guide", "💧 Water Crisis Prediction", "🌾 Irrigation Efficiency", "📘 About Project"],
    label_visibility="collapsed"
)

st.sidebar.markdown("""
<div style="
    margin-top:2rem;
    padding:1rem;
    background:rgba(0,100,200,0.07);
    border:1px solid rgba(0,140,255,0.1);
    border-radius:10px;
">
  <p style="font-family:'Syne',sans-serif;font-size:0.7rem;color:#3a7aaa;letter-spacing:0.1em;text-transform:uppercase;margin:0 0 0.4rem;">Stack</p>
  <p style="font-family:'DM Sans',sans-serif;font-size:0.82rem;color:#5a9abf;margin:0;line-height:1.8;">Python · Pandas · Scikit-Learn<br>Streamlit · Plotly · Random Forest</p>
</div>
""", unsafe_allow_html=True)

# ── Page routing ─────────────────────────────────────────────────────────────
if menu == "Project Guide":
    show_project_guide()

elif menu == "💧 Water Crisis Prediction":
    show_water_page()

elif menu == "🌾 Irrigation Efficiency":
    show_irrigation_page()

elif menu == "📘 About Project":
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
<h3 style="font-family:'Syne',sans-serif;font-size:1.6rem;font-weight:800;color:#e0f2ff;margin-bottom:1rem;">
About This System
</h3>
<p style="font-family:'DM Sans',sans-serif;color:#7aadce;line-height:1.8;font-size:0.95rem;">
This system predicts district-level water crisis risk and analyzes irrigation inefficiency
using machine learning models trained on real-world groundwater and agriculture datasets.
</p>
""", unsafe_allow_html=True)

        st.markdown("""
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.5rem;">
  <div style="background:rgba(0,80,180,0.1);border:1px solid rgba(0,140,255,0.15);border-radius:12px;padding:1.2rem;">
    <p style="font-family:'Syne',sans-serif;font-size:0.75rem;color:#3a7aaa;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 0.5rem;">Module 01</p>
    <p style="font-family:'Syne',sans-serif;font-weight:700;color:#c8e8ff;font-size:1rem;margin:0 0 0.4rem;">Water Stress</p>
    <p style="font-family:'DM Sans',sans-serif;color:#5a9abf;font-size:0.85rem;margin:0;line-height:1.6;">Groundwater recharge & extraction analysis with stress classification.</p>
  </div>
  <div style="background:rgba(0,80,180,0.1);border:1px solid rgba(0,140,255,0.15);border-radius:12px;padding:1.2rem;">
    <p style="font-family:'Syne',sans-serif;font-size:0.75rem;color:#3a7aaa;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 0.5rem;">Module 02</p>
    <p style="font-family:'Syne',sans-serif;font-weight:700;color:#c8e8ff;font-size:1rem;margin:0 0 0.4rem;">Irrigation</p>
    <p style="font-family:'DM Sans',sans-serif;color:#5a9abf;font-size:0.85rem;margin:0;line-height:1.6;">Crop-type efficiency scoring and water consumption benchmarking.</p>
  </div>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div style="background:rgba(0,60,140,0.12);border:1px solid rgba(0,140,255,0.15);border-radius:14px;padding:1.5rem;margin-top:0.2rem;">
  <p style="font-family:'Syne',sans-serif;font-size:0.75rem;color:#3a7aaa;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 1rem;">🚀 Future Scope</p>
  <ul style="font-family:'DM Sans',sans-serif;color:#6a9abf;font-size:0.88rem;line-height:2;padding-left:1.2rem;margin:0;">
    <li>Rainfall forecasting via time-series models</li>
    <li>GIS-based district heatmaps</li>
    <li>Real-time IoT sensor integration</li>
    <li>Government policy support dashboard</li>
  </ul>
</div>
""", unsafe_allow_html=True)