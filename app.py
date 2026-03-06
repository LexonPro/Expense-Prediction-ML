import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load model
with open("expense_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Expense Prediction App", page_icon="💰")

st.title("💰 Expense Prediction App")
st.write("Predict your total monthly expense using a machine learning model.")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Income", min_value=0)
    food = st.number_input("Food Expense", min_value=0)
    travel = st.number_input("Travel Expense", min_value=0)

with col2:
    rent = st.number_input("Rent Expense", min_value=0)
    other = st.number_input("Other Expense", min_value=0)

# Prediction button
if st.button("Predict Expense"):

    features = np.array([[income, food, travel, rent, other]])
    prediction = model.predict(features)[0]

    st.success(f"Predicted Monthly Expense: ₹{prediction:.2f}")

    # Chart visualization
    labels = ["Food", "Travel", "Rent", "Other"]
    values = [food, travel, rent, other]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    ax.set_title("Expense Distribution")

    st.pyplot(fig)