import streamlit as st
import pandas as pd
import joblib

# Load model and transformer
model = joblib.load("model.pkl")
transformer = joblib.load("transformer.pkl")

# Page Config
st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="centered"
)

# Title
st.title("💻 Laptop Price Prediction")
st.markdown("Predict laptop prices using a KNN Regressor Machine Learning model.")

st.divider()

# Inputs
laptop_id = st.number_input(
    "Laptop ID",
    min_value=1,
    value=1
)

inches = st.number_input(
    "Screen Size (Inches)",
    min_value=10.0,
    max_value=20.0,
    value=15.6
)

company = st.text_input("Company", "Dell")
product = st.text_input("Product", "Inspiron")
typename = st.text_input("Type Name", "Notebook")
screen = st.text_input("Screen Resolution", "1920x1080")
cpu = st.text_input("CPU", "Intel Core i5")
ram = st.text_input("RAM", "8GB")
memory = st.text_input("Memory", "256GB SSD")
weight = st.text_input("Weight", "2.0kg")

st.divider()

if st.button("🔍 Predict Price"):

    data = pd.DataFrame({
        "laptop_ID": [laptop_id],
        "Company": [company],
        "Product": [product],
        "TypeName": [typename],
        "ScreenResolution": [screen],
        "Cpu": [cpu],
        "Ram": [ram],
        "Memory": [memory],
        "Weight": [weight],
        "Inches": [inches]
    })

    transformed_data = transformer.transform(data)

    prediction = model.predict(transformed_data)

    st.success(f"💰 Predicted Laptop Price: € {prediction[0]:.2f}")

st.sidebar.title("📌 About Project")
st.sidebar.info(
    """
    Laptop Price Prediction using:
    
    • Python
    
    • Scikit-Learn
    
    • KNN Regressor
    
    • Streamlit
    
    • Pandas
    """
)