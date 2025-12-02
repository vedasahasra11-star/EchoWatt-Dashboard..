import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="EchoWatt Dashboard", layout="wide")

st.title("EchoWatt Dashboard")

# Simulated Energy Data
energy_generated_today = 3200  # Wh
battery_percent = 72
charging = True
power_watts = 200
energy_stored = energy_generated_today * (battery_percent / 100)
energy_used = energy_generated_today - energy_stored

# Display top summary cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Energy Generated Today (Wh)", energy_generated_today)
col2.progress(battery_percent / 100)
col2.write(f"Battery Percentage: {battery_percent}%")
col3.metric("Status", "Charging" if charging else "Discharging")

st.markdown("---")

# Energy Summary
st.subheader("Energy Summary")
col4, col5, col6 = st.columns(3)
col4.metric("Today's Energy Generated (Wh)", energy_generated_today)
col5.metric("Energy Stored (Wh)", int(energy_stored))
col6.metric("Energy Used (Wh)", int(energy_used))

# Traffic & Vehicle Insights
st.subheader("Traffic & Vehicle Insights")

vehicles = {
    "Cars": 420,
    "Bikes": 320,
    "Trucks": 90,
    "Vans": 70,
    "Others": 30
}

total_vehicles = sum(vehicles.values())
st.write(f"Total Vehicles Passed Today: {total_vehicles}")

vehicle_counts = pd.DataFrame(list(vehicles.items()), columns=["Vehicle Type", "Count"])
st.bar_chart(vehicle_counts.set_index("Vehicle Type"))

# Weight estimation (simulated)
weight_categories = {
    "Very High": 12,
    "High": 28,
    "Moderate": 40,
    "Low": 15,
    "Very Low": 5
}
st.subheader("Weight Estimation")
weight_df = pd.DataFrame(list(weight_categories.items()), columns=["Category", "Percentage"])
st.bar_chart(weight_df.set_index("Category"))

