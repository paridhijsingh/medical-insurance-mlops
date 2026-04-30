import streamlit as st
import requests

st.title("Insurance Premium Predictor")
st.write("This app communicates with a FastAPI model deployed on AWS EKS.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=22.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker?", ["yes", "no"])

API_URL = "http://127.0.0.1:8000/predict"

if st.button("Predict"):
    # 1. YOU MUST DEFINE THE PAYLOAD HERE
    # In streamlit_app.py
    payload = {
    "age": age,
    "bmi": bmi,
    "children": children,
    "smoker": 1 if smoker == "yes" else 0,
    "sex": 1 
    }
    st.info("Attempting to connect to backend...")
    with st.spinner("Processing..."):
        try:
            # Send the request with a 15-second timeout
            response = requests.post(API_URL, json=payload, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                prediction = data.get("estimated_charges")
                
                if prediction is not None:
                    # Apply the safety floor here
                    final_val = max(0, float(prediction))
                    st.success(f"Predicted Premium: ${prediction:,.2f}")
                else:
                    st.warning("API call succeeded, but 'estimated_charges' was not found.")
                    st.json(data) # Shows what the API actually sent back
            else:
                st.error(f"Backend Error: {response.status_code}")
                st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error("Connection Refused! Is your FastAPI/Uvicorn server running on port 8000?")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")