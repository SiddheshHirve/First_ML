import streamlit as st
import pickle
import numpy as np

# Load the trained modeljj 
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("Housing Price Prediction App")

# Input fields
society = st.number_input("Society", min_value=0, value=0, step=1)
price_per_sqft = st.number_input("Price per Sqft", min_value=0.0, value=0.0, step=0.1)
area = st.number_input("Area", min_value=0.0, value=0.0, step=1.0)
area_with_type = st.number_input("Area With Type", min_value=0, value=0, step=1)
bedroom = st.number_input("Number of Bedrooms", min_value=0, value=0, step=1)
bathroom = st.number_input("Number of Bathrooms", min_value=0, value=0, step=1)
balcony = st.number_input("Number of Balconies", min_value=0, value=0, step=1)
additional_room = st.number_input("Additional Rooms", min_value=0, value=0, step=1)
floor_num = st.number_input("Floor Number", min_value=0.0, value=0.0, step=1.0)
facing = st.number_input("Facing", min_value=0, value=0, step=1)
age_possession = st.number_input("Age Possession", min_value=0, value=0, step=1)
furnish_details = st.number_input("Furnish Details", min_value=0, value=0, step=1)

# Prediction
if st.button("Predict"):
    # Create an input array
    input_data = np.array([society, price_per_sqft, area, area_with_type, 
                           bedroom, bathroom, balcony, additional_room, 
                           floor_num, facing, age_possession, furnish_details]).reshape(1, -1)
    # Make prediction
    prediction = model.predict(input_data)
    st.success(f"The predicted price is ₹ {prediction[0]:,.2f}L")

