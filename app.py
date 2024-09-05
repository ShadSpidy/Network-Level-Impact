import streamlit as st

# Set page configuration
st.set_page_config(page_title="Network Level Impact Calculator", layout="wide")

# Add custom CSS to make it look darker
st.markdown(
    """
    <style>
    .reportview-container {
        background: #2e2e2e;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background: #1e1e1e;
        color: #ffffff;
    }
    .widget-label {
        color: #ffffff;
    }
    .stButton > button {
        background-color: #555555;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: #777777;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Network Level Impact Calculator")

# Getting user inputs with validation
try:
    total_traffic = float(st.number_input("Enter the Total Traffic:"))
    impacted_node_traffic = float(st.number_input("Enter the Traffic catered by impacted nodes:"))
    percentage_impact = float(st.number_input("Enter the current percentage impact (%):"))

    # Calculation and displaying results
    if st.button("Calculate"):
        if total_traffic > 0:
            NW_level_impact = ((impacted_node_traffic / total_traffic) * 100) * (percentage_impact / 100)
            st.markdown(f"<h3 style='font-size:18px;'>Current Network Level Impact is: {round(NW_level_impact, 2)}%</h3>", unsafe_allow_html=True)
        else:
            st.error("Total Traffic must be greater than zero.")
except ValueError:
    st.error("Please enter valid numerical values.")

# Footer credit
st.markdown("**Created by: Neha's Daddy**", unsafe_allow_html=True)

