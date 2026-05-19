
import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("diabetes_model.pkl")

# App title
st.title("Diabetes Prediction App")

st.write("Enter Patient Details")

# Input fields
Pregnancies = st.number_input("Pregnancies")
Glucose = st.number_input("Glucose")
BloodPressure = st.number_input("Blood Pressure")
SkinThickness = st.number_input("Skin Thickness")
Insulin = st.number_input("Insulin")
BMI = st.number_input("BMI")
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function")
Age = st.number_input("Age")

# Prediction button
if st.button("Predict"):

    data = np.array([[Pregnancies, Glucose, BloodPressure,
                      SkinThickness, Insulin, BMI,
                      DiabetesPedigreeFunction, Age]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("The person is likely to have Diabetes")
    else:
        st.success("The person is NOT likely to have Diabetes")
