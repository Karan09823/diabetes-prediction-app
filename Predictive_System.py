import streamlit as st
import numpy as np
import pickle
import streamlit as st
# Load the saved model
model = pickle.load(open('trained_model.sav', 'rb'))

# If you used scaling, load the scaler as well
# scaler = pickle.load(open('scaler.sav', 'rb'))

# Title and description
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details below to predict if they are diabetic.")

# Input fields
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=33)

# Collect inputs into a single array
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                        bmi, diabetes_pedigree, age]])

# If you used a scaler during training, apply it here
# input_data = scaler.transform(input_data)

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)
    
    if prediction[0] == 0:
        st.success("✅ The person is **not diabetic**.")
    else:
        st.error("⚠️ The person is **diabetic**.")
