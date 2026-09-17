import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

# Load model and scaler
model = tf.keras.models.load_model("student_performance_ann.keras")
scaler = joblib.load("student_scaler.pkl")

# Title
st.title("Student Performance Predictor")

st.write("Enter student details to predict the final grade.")

# Input fields
age = st.number_input("Age", min_value=15, max_value=25, value=17)

studytime = st.number_input(
    "Study Time (1-4)",
    min_value=1,
    max_value=4,
    value=2
)

failures = st.number_input(
    "Number of Failures",
    min_value=0,
    max_value=4,
    value=0
)

absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=100,
    value=5
)

# Prediction
if st.button("Predict Grade"):

    new_student = pd.DataFrame({
        "age": [age],
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences]
    })

    new_student_scaled = scaler.transform(new_student)

    prediction = model.predict(
        new_student_scaled,
        verbose=0
    )

    predicted_grade = float(prediction[0][0])
    predicted_grade = np.clip(predicted_grade,0,20)

    st.success(
        f"Predicted Final Grade: {predicted_grade:.2f}/20"
    )