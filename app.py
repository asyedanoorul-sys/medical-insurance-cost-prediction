
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("medical_insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")
st.write("Enter the customer's information to estimate medical insurance charges.")

# User inputs
age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

sex = st.selectbox(
    "Gender",
    ["female", "male"]
)

smoker = st.selectbox(
    "Smoking Status",
    ["no", "yes"]
)

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# Prediction button
if st.button("Predict Insurance Cost"):

    # Create input data
    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex_male": [1 if sex == "male" else 0],
        "smoker_yes": [1 if smoker == "yes" else 0],
        "region_northwest": [1 if region == "northwest" else 0],
        "region_southeast": [1 if region == "southeast" else 0],
        "region_southwest": [1 if region == "southwest" else 0]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Medical Insurance Cost: ${prediction:,.2f}"
    )
