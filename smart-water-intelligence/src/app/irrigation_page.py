import streamlit as st
import joblib
import numpy as np
import os
import sys
import plotly.express as px
import plotly.graph_objects as go

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from config import MODEL_PATH

model          = joblib.load(os.path.join(MODEL_PATH, "irrigation_model.pkl"))
crop_encoder   = joblib.load(os.path.join(MODEL_PATH, "crop_encoder.pkl"))
irrig_encoder  = joblib.load(os.path.join(MODEL_PATH, "irrigation_encoder.pkl"))

# ── Plotly dark theme defaults ───────────────────────────────────────────────
CHART_LAYOUT = dict(
    paper_bgcolor="rgba(5,13,26,0)",
    plot_bgcolor="rgba(5,13,26,0)",
    font=dict(family="DM Sans, sans-serif", color="#7aadce"),
    title_font=dict(family="Syne, sans-serif", color="#c8e8ff", size=15),
    xaxis=dict(gridcolor="rgba(0,120,220,0.08)", zerolinecolor="rgba(0,120,220,0.15)"),
    yaxis=dict(gridcolor="rgba(0,120,220,0.08)", zerolinecolor="rgba(0,120,220,0.15)"),
    margin=dict(l=20, r=20, t=44, b=20),
)

# Approximate reference water use by crop type (m³/kg) for benchmark chart
CROP_BENCHMARKS = {
    "Rice": 2500, "Wheat": 1200, "Maize": 900,
    "Sugarcane": 2000, "Cotton": 2800, "Soybean": 1800,
    "Vegetables": 300, "Fruits": 700,
}


def show_irrigation_page():
    # ── Page header ──────────────────────────────────────────────────────────
    st.markdown("""
<div style="
    display:flex;align-items:center;gap:0.75rem;
    margin-bottom:1.75rem;padding-bottom:1rem;
    border-bottom:1px solid rgba(0,140,255,0.12);
">
  <span style="font-size:2rem;">🌾</span>
  <div>
    <p style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;
       color:#e0f2ff;margin:0;letter-spacing:-0.02em;">Irrigation Efficiency Analysis</p>
    <p style="font-family:'DM Sans',sans-serif;font-size:0.85rem;color:#4a8aaf;margin:0;">
       Analyse water consumption efficiency by crop type and irrigation method</p>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Input section ─────────────────────────────────────────────────────────
    st.markdown("""
<p style="font-family:'Syne',sans-serif;font-size:0.7rem;color:#3a6a90;
   text-transform:uppercase;letter-spacing:0.12em;margin-bottom:0.75rem;">
Input Parameters
</p>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        crop = st.selectbox(
            "Crop Type",
            list(crop_encoder.classes_),
            help="Select the crop being irrigated"
        )
    with col2:
        irrigation = st.selectbox(
            "Irrigation Method",
            list(irrig_encoder.classes_),
            help="Current irrigation technique in use"
        )

    water_use = st.slider(
        "Water Use (m³/kg)",
        0, 5000, 1000,
        help="Water consumed per kg of crop produced"
    )

    # Efficiency hint
    bench = CROP_BENCHMARKS.get(crop, 1500)
    delta  = water_use - bench
    hint_color = "#f0a830" if delta > 0 else "#30d888"
    hint_text  = f"{'↑ ' + str(abs(delta)) + ' above' if delta > 0 else '↓ ' + str(abs(delta)) + ' below'} typical for {crop} ({bench} m³/kg)"

    st.markdown(f"""
<p style="font-family:'DM Sans',sans-serif;font-size:0.82rem;color:{hint_color};
   margin-top:-0.3rem;margin-bottom:1rem;">
  {hint_text}
</p>
""", unsafe_allow_html=True)

    analyze_btn = st.button("🔍 Analyse Irrigation Efficiency", use_container_width=False)

    if analyze_btn:
        crop_enc  = crop_encoder.transform([crop])[0]
        irrig_enc = irrig_encoder.transform([irrigation])[0]
        X = np.array([[crop_enc, water_use, irrig_enc]])
        prediction = model.predict(X)[0]

        # ── Result banner ────────────────────────────────────────────────────
        if prediction == "Inefficient":
            bg, border, dot, label, icon = (
                "rgba(220,30,60,0.1)", "rgba(220,60,80,0.35)",
                "#e05060", "INEFFICIENT", "🚨"
            )
        else:
            bg, border, dot, label, icon = (
                "rgba(0,180,100,0.08)", "rgba(0,200,120,0.3)",
                "#30d888", "EFFICIENT", "✅"
            )

        st.markdown(f"""
<div style="
    background:{bg};
    border:1px solid {border};
    border-radius:14px;
    padding:1.2rem 1.6rem;
    margin:1.25rem 0;
    display:flex;align-items:center;gap:1rem;
">
  <div style="
    width:10px;height:10px;border-radius:50%;
    background:{dot};
    box-shadow:0 0 12px {dot};
    flex-shrink:0;
  "></div>
  <div>
    <p style="font-family:'Syne',sans-serif;font-size:0.7rem;color:{dot};
       text-transform:uppercase;letter-spacing:0.15em;margin:0 0 0.15rem;">
       Irrigation Efficiency Classification
    </p>
    <p style="font-family:'Syne',sans-serif;font-size:1.45rem;font-weight:800;
       color:#e8f4ff;margin:0;letter-spacing:-0.02em;">
       {icon} {label}
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

        # ── Summary metrics ───────────────────────────────────────────────────
        colA, colB, colC = st.columns(3)
        with colA:
            st.metric("Water Use (m³/kg)", f"{water_use:,}")
        with colB:
            st.metric("Crop Benchmark (m³/kg)", f"{bench:,}")
        with colC:
            pct = round((water_use / bench - 1) * 100, 1) if bench else 0
            st.metric("vs. Benchmark", f"{pct:+.1f}%")

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        # ── Charts ────────────────────────────────────────────────────────────
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            fig_bar = go.Figure()
            bar_color = "#e05060" if water_use > bench else "#30d888"
            fig_bar.add_trace(go.Bar(
                name="Your Usage",
                x=["Your Usage", "Crop Benchmark"],
                y=[water_use, bench],
                marker=dict(
                    color=[bar_color, "#1a8cdb"],
                    line=dict(width=0),
                ),
                text=[f"{water_use:,}", f"{bench:,}"],
                textposition="outside",
                textfont=dict(family="DM Sans", color="#7aadce", size=12),
            ))
            fig_bar.update_layout(
                title="Usage vs. Benchmark",
                showlegend=False,
                **CHART_LAYOUT
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with chart_col2:
            # Top-crop comparison
            crops_to_show = list(CROP_BENCHMARKS.keys())[:6]
            vals = [CROP_BENCHMARKS[c] for c in crops_to_show]
            colors_list = [
                "#e05060" if c == crop else "#1a5a9a" for c in crops_to_show
            ]

            fig_crop = go.Figure(go.Bar(
                x=crops_to_show,
                y=vals,
                marker=dict(color=colors_list, line=dict(width=0)),
                text=vals,
                textposition="outside",
                textfont=dict(family="DM Sans", color="#7aadce", size=11),
            ))
            fig_crop.update_layout(
                title="Typical Water Use by Crop",
                showlegend=False,
                **CHART_LAYOUT
            )
            st.plotly_chart(fig_crop, use_container_width=True)