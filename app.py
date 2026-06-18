import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("laptop_price_pipeline.pkl")

# Page Config
st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide"
)

# Rainbow Theme CSS
st.markdown("""
<style>

/* Rainbow Background */
.stApp {
    background: linear-gradient(
        135deg,
        #ff0000,
        #ff7f00,
        #ffff00,
        #00ff00,
        #00ffff,
        #0000ff,
        #8b00ff
    );
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #4e54c8,
        #8f94fb
    );
}

/* Buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #ff512f,
        #dd2476
    );
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.85);
    border-radius: 15px;
    padding: 10px;
}

/* Input Areas */
[data-testid="stVerticalBlock"] {
    background-color: rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 15px;
}

/* Title */
h1 {
    color: white !important;
    text-align: center;
}

/* Caption */
p {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📌 About Project")
st.sidebar.info("""
Laptop Price Prediction using:

• Python

• Pandas

• Scikit-Learn

• KNN Regressor

• Streamlit
""")

st.sidebar.success("👨‍💻 Developed By")
st.sidebar.write("Shaik Khaja Mainuddin")
st.sidebar.write("AI & DS Student")

# Title
st.title("💻 Laptop Price Prediction")
st.caption("Machine Learning Project using KNN Regressor and Streamlit")

st.divider()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Algorithm", "KNN")

with col2:
    st.metric("Model Type", "Regression")

with col3:
    st.metric("Status", "Live")

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
    ["Intel", "AMD"]
)

ram = st.selectbox(
    "RAM",
    ["4GB", "8GB", "16GB", "32GB"]
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

# Prediction
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

    st.markdown("## 🎯 Prediction Result")

    st.success(
        f"💰 Estimated Laptop Price: € {prediction[0]:.2f}"
    )

    if prediction[0] < 500:
        st.warning("💻 Budget Laptop")

    elif prediction[0] < 1000:
        st.info("🚀 Mid-Range Laptop")

    else:
        st.success("🔥 Premium Laptop")

    st.balloons()

st.divider()

st.markdown(
    """
    <center>
    <h4 style='color:white;'>
    Developed by Shaik Khaja Mainuddin | AI & DS Student
    </h4>
    </center>
    """,
    unsafe_allow_html=True
)
