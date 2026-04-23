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
