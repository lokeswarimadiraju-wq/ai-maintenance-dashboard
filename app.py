import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(page_title="AI Predictive Maintenance", layout="centered")

st.title("🤖 AI Powered Predictive Maintenance System")
st.markdown("### Real-Time Machine Health Monitoring Dashboard")

# -----------------------------
# STATUS FUNCTION
# -----------------------------
def get_status(prob):
    if prob < 0.3:
        return "GREEN"
    elif prob < 0.7:
        return "YELLOW"
    else:
        return "RED"

# -----------------------------
# BUTTON
# -----------------------------
if st.button("🔍 Check Machine Status"):

    # Generate probability
    prob = np.random.rand()
    status = get_status(prob)

    # -----------------------------
    # FAILURE TIME CALCULATION
    # -----------------------------
    current_time = datetime.now()

    if status == "GREEN":
        failure_time = current_time + timedelta(days=5)
    elif status == "YELLOW":
        failure_time = current_time + timedelta(hours=12)
    else:
        failure_time = current_time + timedelta(hours=2)

    # -----------------------------
    # DISPLAY OUTPUT
    # -----------------------------
    st.write(f"🔢 Failure Probability: **{prob:.2f}**")

    if status == "GREEN":
        st.success("🟢 Machine is SAFE")
    elif status == "YELLOW":
        st.warning("🟡 Medium Risk - Maintenance Needed")
    else:
        st.error("🔴 High Risk - Failure Expected!")

    # -----------------------------
    # DISPLAY FAILURE TIME
    # -----------------------------
    st.markdown("### ⏰ Predicted Failure Time")
    st.success(failure_time.strftime("%Y-%m-%d %H:%M:%S"))

# -----------------------------
# GRAPH SECTION
# -----------------------------
st.markdown("### 📊 Machine Sensor Data")

data = pd.DataFrame({
    "Time": range(20),
    "Temperature": np.random.randint(290, 320, 20),
    "Pressure": np.random.randint(50, 100, 20)
})

st.line_chart(data.set_index("Time"))
