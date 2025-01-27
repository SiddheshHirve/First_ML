import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("Housing Price Prediction App")

# Input fields with appropriate data types
society = st.text_input("Society", "")  # Object
price_per_sqft = st.number_input("Price per Sqft", min_value=0.0, value=0.0, step=0.1)  # Float
area = st.number_input("Area (in Sqft)", min_value=0.0, value=0.0, step=1.0)  # Float
area_with_type = st.text_input("Area With Type", "")  # Object
bedroom = st.number_input("Number of Bedrooms", min_value=0, value=0, step=1)  # Int
bathroom = st.number_input("Number of Bathrooms", min_value=0, value=0, step=1)  # Int
balcony = st.text_input("Number of Balconies", "")  # Object
additional_room = st.text_input("Additional Rooms", "")  # Object
floor_num = st.number_input("Floor Number", min_value=0.0, value=0.0, step=1.0)  # Float
facing = st.text_input("Facing", "")  # Object
age_possession = st.text_input("Age Possession", "")  # Object
furnish_details = st.text_input("Furnish Details", "")  # Object

# Prediction
if st.button("Predict"):
    # Encode categorical fields if necessary
    # Assuming categorical fields need to be encoded (e.g., one-hot or label encoding)
    categorical_fields = [society, area_with_type, balcony, additional_room, facing, age_possession, furnish_details]
    categorical_encoded = [hash(field) % 1000 if field else 0 for field in categorical_fields]  # Simple hash encoding

    # Combine numerical and encoded categorical fields
    input_data = np.array([
        *categorical_encoded,
        price_per_sqft,
        area,
        bedroom,
        bathroom,
        floor_num
    ]).reshape(1, -1)

    # Make prediction
    try:
        prediction = model.predict(input_data)
        st.success(f"The predicted price is ₹ {prediction[0]:,.2f}L")
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")

