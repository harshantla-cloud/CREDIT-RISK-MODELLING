import streamlit as st
import pandas as pd
import joblib
import base64

# ================= PAGE =================
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="wide"
)

# ================= BACKGROUND =================
def background(path):
    with open(path, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,5,20,.72),rgba(0,5,20,.78)),
        url("data:image/webp;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    h1,h2,h3,p,label {{color:white !important;}}

    .card {{
        background:rgba(5,15,40,.75);
        padding:22px;
        border-radius:18px;
        border:1px solid rgba(255,255,255,.15);
        margin-bottom:20px;
    }}

    .result {{
        padding:25px;
        border-radius:18px;
        text-align:center;
        font-size:26px;
        font-weight:800;
        margin-top:20px;
        backdrop-filter:blur(10px);
    }}

    .good {{
        background:rgba(16,185,129,.18);
        border:1px solid #34d399;
        color:#6ee7b7;
    }}

    .bad {{
        background:rgba(239,68,68,.18);
        border:1px solid #f87171;
        color:#fca5a5;
    }}

    div.stButton > button {{
        background:linear-gradient(90deg,#2563eb,#4f46e5);
        color:white;
        border:0;
        border-radius:12px;
        height:50px;
        font-size:17px;
        font-weight:700;
    }}
    </style>
    """, unsafe_allow_html=True)

background("Project Images/credit_risk_background.webp.webp")


# ================= MODEL =================
model = joblib.load("models/extra_tress_credit_model.pkl")

encoders = {
    "Sex": joblib.load("encoders/Sex_encoder.pkl"),
    "Housing": joblib.load("encoders/Housing_encoder.pkl"),
    "Saving accounts": joblib.load(
        "encoders/Saving accounts_encoder.pkl"),
    "Checking account": joblib.load(
        "encoders/Checking account_encoder.pkl"),
    "Purpose": joblib.load("encoders/Purpose_encoder.pkl")
}


# ================= HEADER =================
st.title("💳 Credit Risk Prediction")
st.caption("AI-powered loan applicant credit risk assessment")
st.divider()


# ================= INPUTS =================
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👤 Applicant Details")

    age = st.number_input("Age", 18, 80, 30)
    sex = st.selectbox("Sex", ["male", "female"])
    job = st.selectbox("Job", [0, 1, 2, 3])
    housing = st.selectbox("Housing", ["own", "rent", "free"])

    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
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

    st.markdown('</div>', unsafe_allow_html=True)


purpose = st.selectbox(
    "🎯 Loan Purpose",
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

st.write("")


# ================= PREDICTION =================
if st.button("🔍  PREDICT CREDIT RISK", use_container_width=True):

    data = pd.DataFrame({
        "Age": [age],
        "Sex": [encoders["Sex"].transform([sex])[0]],
        "Job": [job],
        "Housing": [encoders["Housing"].transform([housing])[0]],
        "Saving accounts": [
            encoders["Saving accounts"].transform([saving])[0]
        ],
        "Checking account": [
            encoders["Checking account"].transform([checking])[0]
        ],
        "Credit amount": [credit],
        "Duration": [duration],
        "Purpose": [
            encoders["Purpose"].transform([purpose])[0]
        ]
    })

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.markdown("""
        <div class="result good">
        🟢<br>
        GOOD CREDIT RISK
        <br>
        <small>Applicant shows a lower credit risk.</small>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result bad">
        🔴<br>
        BAD CREDIT RISK
        <br>
        <small>Applicant shows a higher credit risk.</small>
        </div>
        """, unsafe_allow_html=True)


# ================= FOOTER =================
st.markdown("""
<div style="text-align:center;color:#94a3b8;margin-top:30px;">
💳 Credit Risk Modelling • Machine Learning • Streamlit
</div>
""", unsafe_allow_html=True)