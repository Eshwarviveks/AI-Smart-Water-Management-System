import streamlit as st
from water_stress_page import show_water_page
from irrigation_page import show_irrigation_page

st.set_page_config(page_title="Smart Water Intelligence", layout="wide")

st.title("💧 Smart Water Crisis & Irrigation Intelligence System")

menu = st.sidebar.selectbox(
    "Select Module",
    ["Water Crisis Prediction", "Irrigation Inefficiency"]
)

if menu == "Water Crisis Prediction":
    show_water_page()

if menu == "Irrigation Inefficiency":
    show_irrigation_page()
