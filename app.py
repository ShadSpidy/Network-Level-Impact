import streamlit as st

st.title("Network Level Impact Calculator")
st.subheader("By: Shadman")

# Getting user inputs
total_traffic = st.number_input("Enter the Total Traffic:")
impacted_node_traffic = st.number_input("Enter the Traffic catered by impacted nodes:")
percentage_impact = st.number_input("Enter the current percentage impact (%):")

# Calculation
if st.button("Calculate"):
    NW_level_impact = ((impacted_node_traffic / total_traffic) * 100) * (percentage_impact / 100)
    st.write(f"Current Network Level Impact is {NW_level_impact:.2f}")
