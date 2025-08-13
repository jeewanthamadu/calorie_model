import streamlit as st
import pandas as pd
import requests

st.title("AI-Driven Calorie Predictor")

# Input fields (example: adjust according to your features)
age = st.number_input("Age", min_value=0, max_value=120, value=25)
weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=70.0)
height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=170.0)
duration = st.number_input("Exercise Duration (minutes)", min_value=0.0, max_value=300.0, value=30.0)
heart_rate = st.number_input("Average Heart Rate", min_value=0.0, max_value=220.0, value=120.0)
body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=36.5)
sex = st.selectbox("Sex", ["Male", "Female"])

# Send data for prediction
if st.button("Predict Calories"):
    input_data = pd.DataFrame([{
        "Age": age,
        "Weight": weight,
        "Height": height,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp,
        "Sex": sex
    }])
    
    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=input_data.to_dict(orient="records"))
        print(response.json())
        if response.status_code == 200:
            prediction = response.json()["predictions"][0]
            st.success(f"Predicted Calories Burned: {prediction:.2f}")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Could not connect to backend: {e}")
