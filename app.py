import streamlit as st
import numpy as np

st.title("AI Predictive Maintenance System")

def get_status(prob):
    if prob < 0.3:
        return "GREEN"
    elif prob < 0.7:
        return "YELLOW"
    else:
        return "RED"

if st.button("Check Status"):
    prob = np.random.rand()
    status = get_status(prob)

    st.write("Probability:", prob)

    if status == "GREEN":
        st.success("🟢 Safe")
    elif status == "YELLOW":
        st.warning("🟡 Risk")
    else:
        st.error("🔴 Danger")
# -----------------------------
# 📊 SENSOR DATA GRAPH
# -----------------------------
import pandas as pd

st.markdown("### 📊 Machine Sensor Data (Live)")

data = pd.DataFrame({
    "Time": range(20),
    "Temperature": np.random.randint(290, 320, 20),
    "Pressure": np.random.randint(50, 100, 20)
})

st.line_chart(data.set_index("Time"))
