import streamlit as st
import pickle
import numpy as np
import datetime


gradient_bg = """
<style>
    .stApp {
        background: linear-gradient(180deg, #E6E6FA, #FFE4E1);
        /* Lavender to very light pink */
        height: 100vh;
    }
</style>
"""

st.markdown(gradient_bg, unsafe_allow_html=True)

# Load the trained model
with open('C:/Users/Rahila/Desktop/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.markdown(
    '<h1 style="color: #007acc">🚕 Taxi Fare Predictor</h1>', 
    unsafe_allow_html=True
)

st.markdown("Enter your trip details to predict the fare amount:")

# User inputs
pickup_hour = st.slider('Pickup Hour (24h)', 0, 23, 12)
trip_distance = st.number_input('Trip Distance (in km)', min_value=0.1, step=0.1)
trip_duration_min = st.number_input('Trip Duration (in minutes)', min_value=1.0, step=0.1)
passenger_count = st.slider('Passenger Count', 1, 6, 1)

# Time-based binary flags
is_weekend = st.selectbox("Is it a weekend?", ["No", "Yes"]) == "Yes"
is_night = st.selectbox("Is it a night ride (10PM–5AM)?", ["No", "Yes"]) == "Yes"

# Predict button
if st.button('Predict Fare'):
    input_data = np.array([[trip_distance, trip_duration_min, passenger_count,
                            pickup_hour, int(is_weekend), int(is_night)]])

    predicted_fare = model.predict(input_data)[0]
    st.success(f"💰 Estimated Fare: ${predicted_fare:.2f}")

#footer
st.markdown('<div class="footer"> Developed by Reshma | 📊 Data Science Project</div>', unsafe_allow_html=True)