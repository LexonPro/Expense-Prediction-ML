import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

st.title("💰 Expense Prediction App")

st.write("Enter your monthly expense details:")

income = st.number_input("Income", min_value=0)
food = st.number_input("Food Expense", min_value=0)
travel = st.number_input("Travel Expense", min_value=0)
rent = st.number_input("Rent Expense", min_value=0)
other = st.number_input("Other Expense", min_value=0)

# simple trained model placeholder
if st.button("Predict Total Expense"):
    total = food + travel + rent + other
    st.success(f"Estimated Total Expense: ₹{total}")
