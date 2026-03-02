import streamlit as st
import numpy as np
import pickle

st.title("💰 Expense Prediction App")
st.write("Enter your monthly expense details:")

with open("expense_model.pkl", "rb") as f:
    model = pickle.load(f)

income = st.number_input("Income", min_value=0)
food = st.number_input("Food Expense", min_value=0)
travel = st.number_input("Travel Expense", min_value=0)
rent = st.number_input("Rent Expense", min_value=0)
other = st.number_input("Other Expense", min_value=0)

if st.button("Predict Total Expense"):
    features = np.array([[income, food, travel, rent, other]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Total Expense: ₹{prediction:.2f}")