import streamlit as st
import joblib
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from config import MODEL_PATH

model = joblib.load(os.path.join(MODEL_PATH, "water_stress_model.pkl"))

def show_water_page():
    st.subheader("💧 District Water Stress Prediction")

    recharge = st.number_input("Annual Recharge")
    extraction = st.number_input("Annual Extraction")
    stage = st.slider("Extraction Stage (%)", 0, 200)

    if st.button("Predict Water Stress"):
        X = np.array([[recharge, extraction, stage]])
        prediction = model.predict(X)[0]
        st.success(f"Predicted Water Stress Level: {prediction}")
