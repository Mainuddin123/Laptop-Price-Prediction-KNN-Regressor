import streamlit as st
import pandas as pd
import joblib

# Load Pipeline Model
model = joblib.load("laptop_price_pipeline.pkl")

# Page Configuration
st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="centered"
)

# Title
st.title("💻 Laptop Price Prediction")
st.caption("Machine Learning Project using KNN Regressor and Streamlit")

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

company = st.selectbox(
    "Company",
    ["Apple", "HP", "Dell", "Lenovo", "Asus", "Acer", "MSI", "Toshiba"]
)

product = st.text_input(
    "Product",
    "Inspiron"
)

typename = st.selectbox(
    "Type Name",
    ["Notebook", "Ultrabook", "Gaming", "2 in 1 Convertible", "Workstation"]
)

screen = st.selectbox(
    "Screen Resolution",
    [
        "1366x768",
        "1920x1080",
        "2560x1600",
        "2880x1800"
    ]
)

cpu = st.selectbox(
    "CPU",
    [
        "Intel",
        "AMD"
    ]
)

ram = st.selectbox(
    "RAM",
    [
        "4GB",
        "8GB",
        "16GB",
        "32GB"
    ]
)

memory = st.selectbox(
    "Memory",
    [
        "128GB SSD",
        "256GB SSD",
        "512GB SSD",
        "1TB SSD",
        "500GB HDD"
    ]
)

weight = st.text_input(
    "Weight",
    "2.0kg"
)

st.divider()

if st.button("🔍 Predict Price"):

    data = pd.DataFrame({
        "laptop_ID": [laptop_id],
        "Company": [company],
        "Product": [product],
        "TypeName": [typename],
        "Inches": [inches],
        "ScreenResolution": [screen],
        "Cpu": [cpu],
        "Ram": [ram],
        "Memory": [memory],
        "Weight": [weight]
    })

    prediction = model.predict(data)

    st.success(
        f"💰 Predicted Laptop Price: € {prediction[0]:.2f}"
    )

st.sidebar.title("📌 About Project")

st.sidebar.info(
    """
    Laptop Price Prediction using:

    • Python

    • Pandas

    • Scikit-Learn

    • KNN Regressor

    • Streamlit
    """
)

st.markdown("---")
st.markdown(
    "Developed by **Shaik Khaja Mainuddin**"
)