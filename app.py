import streamlit as st
import pandas as pd
import pickle

# Title
st.title("Loan Approval Prediction App")

# Input fields
income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
credit_history = st.selectbox("Credit History", [0, 1])

# Load model (you must save your model first)
model = pickle.load(open("model.pkl", "rb"))

# Prediction button
if st.button("Predict"):
    data = [[income, loan_amount, credit_history]]
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Not Approved ❌")