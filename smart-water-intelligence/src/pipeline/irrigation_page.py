import streamlit as st
import joblib
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from config import MODEL_PATH

model = joblib.load(os.path.join(MODEL_PATH, "irrigation_model.pkl"))

def show_irrigation_page():
    st.subheader("🌾 Irrigation Inefficiency Detection")

    crop = st.number_input("Crop Code (numeric)")
    water_use = st.number_input("Water Use (m³/kg)")
    irrigation_type = st.number_input("Irrigation Type Code (numeric)")

    if st.button("Predict Irrigation Efficiency"):
        X = np.array([[crop, water_use, irrigation_type]])
        prediction = model.predict(X)[0]
        st.success(f"Irrigation Status: {prediction}")
