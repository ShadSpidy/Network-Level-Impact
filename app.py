import streamlit as st

st.title("Network Level Impact Calculator")
st.subheader("By: Shadman")

# Getting user inputs with validation
try:
    total_traffic = float(st.number_input("Enter the Total Traffic:"))
    impacted_node_traffic = float(st.number_input("Enter the Traffic catered by impacted nodes:"))
    percentage_impact = float(st.number_input("Enter the current percentage impact (%):"))

    # Calculation and displaying results
    if st.button("Calculate"):
        if total_traffic > 0:
            NW_level_impact = ((impacted_node_traffic / total_traffic) * 100) * (percentage_impact / 100)
            st.write(f"Current Network Level Impact is {NW_level_impact:.2f}%")
        else:
            st.error("Total Traffic must be greater than zero.")
except ValueError:
    st.error("Please enter valid numerical values.")

