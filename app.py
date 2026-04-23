import streamlit as st
import numpy as np
import time
import joblib

# Load model and scaler (we will save them next)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def get_status(prob):
    if prob < 0.3:
        return "GREEN"
    elif prob < 0.7:
        return "YELLOW"
    else:
        return "RED"

st.title("AI Predictive Maintenance System")

placeholder = st.empty()

while True:
    sample = np.random.rand(1, scaler.n_features_in_)
    sample_scaled = scaler.transform(sample)

    prob = model.predict_proba(sample_scaled)[0][1]
    status = get_status(prob)

    with placeholder.container():
        if status == "GREEN":
            st.success("🟢 Machine Safe")
        elif status == "YELLOW":
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 Danger! Failure Expected")

    time.sleep(2)