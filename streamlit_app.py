import streamlit as st
import requests

st.title("Insurance Premium Predictor")
st.write("This app communicates with a FastAPI model deployed on AWS EKS.")

# Create input fields based on your model's requirements
age = st.number_input("Age", min_value=18, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker?", ["yes", "no"])

# Update this URL to your actual AWS Load Balancer URL
API_URL = "http://a4b537a33c27048d08198fac9dad6051-363075708.us-east-1.elb.amazonaws.com/predict"

if st.button("Predict Cost"):
    payload = {
        "age": age,
        "bmi": bmi,
        "children": children,
        "smoker": smoker
    }
    
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"Estimated Annual Premium: ${prediction:,.2f}")
    else:
        st.error("Error: Could not reach the API.")