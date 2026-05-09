import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('diabetes_model.pkl', 'rb'))

# Title
st.title("Diabetes Detection System")

# Inputs
pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

# Prediction button
if st.button("Predict"):

    input_data = np.array([[pregnancies, glucose,
                            blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Person is Diabetic")
    else:
        st.success("Person is Non-Diabetic")