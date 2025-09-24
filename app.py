import streamlit as st
import pickle
import numpy as np

# Load your trained model
model = joblib.load("water_quality_predict.pkl")

st.title("Water Potability Prediction")

st.write("Enter the water quality parameters to check if the water is **Potable (Safe)** or **Not Potable (Unsafe)**.")

# Example input features (update based on your model training dataset)
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Hardness (mg/L)", min_value=0.0, step=0.1)
solids = st.number_input("Total Dissolved Solids (ppm)", min_value=0.0, step=1.0)
chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, step=0.1)
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, step=0.1)
conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, step=0.1)
organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, step=0.1)
trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, step=0.1)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, step=0.1)

# Prediction
if st.button("Predict Potability"):
    # Arrange inputs in same order as training dataset
    features = np.array([[ph, hardness, solids, chloramines, sulfate, 
                          conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("The water is **Potable (Safe to Drink)**")
    else:
        st.error("The water is **Not Potable (Unsafe for Drinking)**")
