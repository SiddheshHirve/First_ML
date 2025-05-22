import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# App Title
st.title("🏠 Housing Price Prediction App")

st.markdown("Enter the property details below to get an estimated price.")

# --- Input Fields ---
society = st.text_input("Society (e.g., Green Homes)", "")
price_per_sqft = st.number_input("Price per Sqft", min_value=1.0, value=1.0, step=0.1)
area = st.number_input("Area (in Sqft)", min_value=1.0, value=500.0, step=10.0)
area_with_type = st.text_input("Area Type (e.g., Super Area, Built-Up Area)", "")
bedroom = st.number_input("Number of Bedrooms", min_value=1, value=1, step=1)
bathroom = st.number_input("Number of Bathrooms", min_value=1, value=1, step=1)
balcony = st.text_input("Number of Balconies (e.g., 1 Balcony)", "")
additional_room = st.text_input("Additional Rooms (e.g., Study Room, Servant Room)", "")
floor_num = st.number_input("Floor Number", min_value=0.0, value=0.0, step=1.0)
facing = st.text_input("Facing (e.g., East, West)", "")
age_possession = st.text_input("Age of Property or Possession Status", "")
furnish_details = st.text_input("Furnish Status (e.g., Semi-Furnished)", "")

# --- Prediction ---
if st.button("Predict"):
    # Validate that no required fields are empty
    required_text_fields = {
        "Society": society,
        "Area With Type": area_with_type,
        "Balcony": balcony,
        "Additional Rooms": additional_room,
        "Facing": facing,
        "Age Possession": age_possession,
        "Furnish Details": furnish_details
    }

    missing_fields = [field for field, value in required_text_fields.items() if not value.strip()]
    
    if missing_fields:
        st.error(f"⚠️ Please enter values for: {', '.join(missing_fields)}")
    else:
        try:
            # Encode categorical fields using simple hashing (quick workaround; should match training)
            categorical_fields = [society, area_with_type, balcony, additional_room, facing, age_possession, furnish_details]
            categorical_encoded = [hash(val.strip().lower()) % 1000 for val in categorical_fields]

            # Combine inputs into a feature vector
            input_data = np.array([
                *categorical_encoded,
                price_per_sqft,
                area,
                bedroom,
                bathroom,
                floor_num
            ]).reshape(1, -1)

            # Predict
            prediction = model.predict(input_data)[0]
            st.success(f"💰 Estimated Price: ₹ {prediction:,.2f} Lakh")

        except Exception as e:
            st.error(f"❌ Prediction failed: {str(e)}")
