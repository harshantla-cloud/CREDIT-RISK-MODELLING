import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("extra_tress_credit_model.pkl")

encoders = {
    "Sex": joblib.load("Sex_encoder.pkl"),
    "Housing": joblib.load("Housing_encoder.pkl"),
    "Saving accounts": joblib.load("Saving accounts_encoder.pkl"),
    "Checking account": joblib.load("Checking account_encoder.pkl"),
    "Purpose": joblib.load("Purpose_encoder.pkl")
}

# Page
st.set_page_config(
    page_title="Credit Risk",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Risk Prediction")
st.caption("Predict whether a loan applicant is Good or Bad Credit Risk")

st.divider()

# Input section
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Applicant Details")
    
    age = st.number_input("Age", 18, 80, 30)
    sex = st.selectbox("Sex", ["male", "female"])
    job = st.selectbox("Job", [0, 1, 2, 3])
    housing = st.selectbox("Housing", ["own", "rent", "free"])

with col2:
    st.subheader("💰 Loan Details")
    
    saving = st.selectbox(
        "Saving Account",
        ["little", "moderate", "quite rich", "rich"]
    )
    
    checking = st.selectbox(
        "Checking Account",
        ["little", "moderate", "rich"]
    )
    
    credit = st.number_input("Credit Amount", 0, 100000, 1000)
    duration = st.number_input("Duration (Months)", 1, 72, 12)

purpose = st.selectbox(
    "Loan Purpose",
    [
        "radio/TV",
        "furniture/equipment",
        "car",
        "business",
        "domestic appliances",
        "repairs",
        "vacation/others",
        "education"
    ]
)

st.divider()

# Prediction
if st.button("🔍 Predict Credit Risk", use_container_width=True):

    data = pd.DataFrame({
        "Age": [age],
        "Sex": [encoders["Sex"].transform([sex])[0]],
        "Job": [job],
        "Housing": [encoders["Housing"].transform([housing])[0]],
        "Saving accounts": [encoders["Saving accounts"].transform([saving])[0]],
        "Checking account": [encoders["Checking account"].transform([checking])[0]],
        "Credit amount": [credit],
        "Duration": [duration],
        "Purpose": [encoders["Purpose"].transform([purpose])[0]]
    })

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("✅ GOOD CREDIT RISK")
    else:
        st.error("❌ BAD CREDIT RISK")