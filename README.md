# Student Performance Predictor

## Project Overview

The Student Performance Predictor is a Machine Learning and Deep Learning project that predicts a student's final grade out of 20.

This project uses an Artificial Neural Network (ANN) to predict student performance based on the following inputs:

- Age
- Study Time
- Number of Failures
- Number of Absences

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow
- Keras
- Streamlit

## Machine Learning Model

We use an Artificial Neural Network (ANN) for predicting the final student grade.

The model is trained using student performance data and standardized input features.

## Application

The project includes a Streamlit web application where users can enter student details and receive a predicted final grade out of 20.

## Project Files

- `student_app.py` – Streamlit web application
- `student_performance_ann.keras` – Trained ANN model
- `student_scaler.pkl` – Feature scaling file

## How to Run

1. Install the required libraries.
2. Open the project folder in PowerShell.
3. Run the following command:

```bash
streamlit run student_app.py
```

## Project Objective

The objective of this project is to understand how deep learning can be used to predict student academic performance.
