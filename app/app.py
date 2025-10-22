import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('../models/delay_model.pkl')

st.title("Flight Delay Predictor")

# --- User Inputs ---
st.sidebar.header("Enter Flight Details")
distance = st.sidebar.number_input("Distance (miles)", min_value=1, value=500)
dep_delay = st.sidebar.number_input("Departure Delay (minutes)", value=0)
dep_hour = st.sidebar.number_input("Scheduled Departure Hour (0-23)", min_value=0, max_value=23, value=12)
weekday = st.sidebar.selectbox("Day of the Week", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
weekday_num = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"].index(weekday)

# Carrier selection
carrier_cols = [c for c in model.feature_names_in_ if c.startswith('CARRIER_')]
carrier_options = ['None'] + [c.replace('CARRIER_', '') for c in carrier_cols]
carrier = st.sidebar.selectbox("Select Carrier", carrier_options)

# Prepare input dataframe
# Remove WEEKDAY from input_dict
input_dict = {
    'Distance': distance,
    'DepDelay': dep_delay,
    'CRS_DEP_HOUR': dep_hour
}


# Add carrier dummies
for c in carrier_cols:
    input_dict[c] = 1 if c == f"CARRIER_{carrier}" else 0

input_df = pd.DataFrame([input_dict])

# Predict
pred = model.predict(input_df)[0]
st.write(f"Predicted Arrival Delay: {pred:.2f} minutes")
