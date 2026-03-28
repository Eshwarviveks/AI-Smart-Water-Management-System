import streamlit as st
import joblib
import numpy as np
import os
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from config import MODEL_PATH

model = joblib.load(os.path.join(MODEL_PATH, "water_stress_model.pkl"))

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


def show_water_page():
    # ── Page header ──────────────────────────────────────────────────────────
    st.markdown("""
<div style="
    display:flex;align-items:center;gap:0.75rem;
    margin-bottom:1.75rem;padding-bottom:1rem;
    border-bottom:1px solid rgba(0,140,255,0.12);
">
  <span style="font-size:2rem;">💧</span>
  <div>
    <p style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;
       color:#e0f2ff;margin:0;letter-spacing:-0.02em;">District Water Crisis Prediction</p>
    <p style="font-family:'DM Sans',sans-serif;font-size:0.85rem;color:#4a8aaf;margin:0;">
       Enter groundwater parameters to classify stress level</p>
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

    col1, col2, col3 = st.columns(3)

    with col1:
        recharge = st.number_input(
            "Annual Recharge (MCM)",
            min_value=0.0,
            help="Annual groundwater recharge in million cubic meters"
        )
    with col2:
        extraction = st.number_input(
            "Annual Extraction (MCM)",
            min_value=0.0,
            help="Annual groundwater extraction in million cubic meters"
        )
    with col3:
        stage = st.slider(
            "Extraction Stage (%)",
            0, 200, 60,
            help="Stage of groundwater extraction as % of recharge"
        )

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    predict_btn = st.button("🔍 Predict Water Stress Level", use_container_width=False)

    if predict_btn:
        X = np.array([[recharge, extraction, stage]])
        prediction = model.predict(X)[0]

        # ── Result banner ────────────────────────────────────────────────────
        stress_config = {
            "High":   {"bg": "rgba(220,30,60,0.1)",   "border": "rgba(220,60,80,0.35)",
                       "dot": "#e05060", "label": "HIGH STRESS",  "icon": "🚨"},
            "Medium": {"bg": "rgba(220,140,0,0.1)",   "border": "rgba(220,160,30,0.35)",
                       "dot": "#f0a830", "label": "MEDIUM STRESS", "icon": "⚠️"},
            "Low":    {"bg": "rgba(0,180,100,0.08)",  "border": "rgba(0,200,120,0.3)",
                       "dot": "#30d888", "label": "LOW STRESS",   "icon": "✅"},
        }
        cfg = stress_config.get(prediction, stress_config["Low"])

        st.markdown(f"""
<div style="
    background:{cfg['bg']};
    border:1px solid {cfg['border']};
    border-radius:14px;
    padding:1.2rem 1.6rem;
    margin:1.25rem 0;
    display:flex;align-items:center;gap:1rem;
">
  <div style="
    width:10px;height:10px;border-radius:50%;
    background:{cfg['dot']};
    box-shadow:0 0 12px {cfg['dot']};
    flex-shrink:0;
  "></div>
  <div>
    <p style="font-family:'Syne',sans-serif;font-size:0.7rem;color:{cfg['dot']};
       text-transform:uppercase;letter-spacing:0.15em;margin:0 0 0.15rem;">
       Water Stress Classification
    </p>
    <p style="font-family:'Syne',sans-serif;font-size:1.45rem;font-weight:800;
       color:#e8f4ff;margin:0;letter-spacing:-0.02em;">
       {cfg['icon']} {cfg['label']}
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

        # ── Metrics row ───────────────────────────────────────────────────────
        colA, colB, colC = st.columns(3)
        with colA:
            st.metric("Recharge (MCM)", f"{recharge:,.1f}")
        with colB:
            st.metric("Extraction (MCM)", f"{extraction:,.1f}")
        with colC:
            ratio = (extraction / recharge * 100) if recharge > 0 else 0
            st.metric("Extraction Ratio", f"{ratio:.1f}%")

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        # ── Charts row ────────────────────────────────────────────────────────
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            importance = model.feature_importances_
            features = ["Recharge", "Extraction", "Extraction Stage"]
            colors = ["#1a8cdb", "#0ec4f1", "#5bc8fa"]

            fig_imp = go.Figure(go.Bar(
                x=features, y=importance,
                marker=dict(
                    color=colors,
                    line=dict(width=0),
                ),
                text=[f"{v:.3f}" for v in importance],
                textposition="outside",
                textfont=dict(family="DM Sans", color="#7aadce", size=12),
            ))
            fig_imp.update_layout(
                title="Feature Importance",
                showlegend=False,
                **CHART_LAYOUT
            )
            st.plotly_chart(fig_imp, use_container_width=True)

        with chart_col2:
            # Gauge for extraction stage
            gauge_color = (
                "#e05060" if stage > 100
                else "#f0a830" if stage > 70
                else "#30d888"
            )
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=stage,
                domain={"x": [0, 1], "y": [0, 1]},
                title={"text": "Extraction Stage (%)",
                       "font": {"family": "Syne", "color": "#c8e8ff", "size": 14}},
                number={"font": {"family": "Syne", "color": "#5bc8fa", "size": 36},
                        "suffix": "%"},
                gauge={
                    "axis": {"range": [0, 200], "tickcolor": "#3a6a90",
                             "tickfont": {"color": "#3a6a90", "size": 10}},
                    "bar": {"color": gauge_color, "thickness": 0.25},
                    "bgcolor": "rgba(0,0,0,0)",
                    "borderwidth": 0,
                    "steps": [
                        {"range": [0, 70],   "color": "rgba(0,200,120,0.07)"},
                        {"range": [70, 100], "color": "rgba(240,170,48,0.07)"},
                        {"range": [100, 200],"color": "rgba(220,50,70,0.07)"},
                    ],
                    "threshold": {
                        "line": {"color": gauge_color, "width": 2},
                        "thickness": 0.8,
                        "value": stage,
                    },
                },
            ))
            fig_gauge.update_layout(
                paper_bgcolor="rgba(5,13,26,0)",
                font=dict(family="DM Sans", color="#7aadce"),
                margin=dict(l=20, r=20, t=44, b=20),
                height=260,
            )
            st.plotly_chart(fig_gauge, use_container_width=True)