import streamlit as st
import pandas as pd
import joblib
import os


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_path(*parts):
    return os.path.join(BASE_DIR, *parts)


# =========================================================
# CUSTOM CSS
# =========================================================

st.html(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(37, 99, 235, 0.18),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(124, 58, 237, 0.15),
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(6, 182, 212, 0.10),
                transparent 30%
            ),
            #0B1220;
        color: #F8FAFC;
    }

    .main {
        padding-top: 1rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #F8FAFC !important;
    }

    p, label {
        color: #CBD5E1;
    }


    /* ================= HERO ================= */

    .hero {
        padding: 32px;
        border-radius: 24px;
        margin-bottom: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(37, 99, 235, 0.22),
                rgba(124, 58, 237, 0.18),
                rgba(6, 182, 212, 0.12)
            ),
            #111827;

        border: 1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 20px 50px rgba(0,0,0,0.30);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 8px;
        color: #FFFFFF !important;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #CBD5E1 !important;
        margin-bottom: 20px;
    }


    /* ================= BADGES ================= */

    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }

    .badge {
        display: inline-block;
        padding: 7px 13px;
        border-radius: 999px;

        background: rgba(37,99,235,0.15);

        border: 1px solid rgba(37,99,235,0.35);

        color: #93C5FD !important;

        font-size: 13px;
        font-weight: 600;
    }


    /* ================= CARDS ================= */

    .card {
        background: rgba(17, 24, 39, 0.88);

        border: 1px solid rgba(255,255,255,0.08);

        border-radius: 20px;

        padding: 24px;

        margin-bottom: 20px;

        box-shadow:
            0 15px 40px rgba(0,0,0,0.22);

        backdrop-filter: blur(12px);
    }

    .card-title {
        font-size: 21px;
        font-weight: 750;

        color: #FFFFFF !important;

        margin-bottom: 5px;
    }

    .card-description {
        font-size: 13px;

        color: #94A3B8 !important;

        margin-bottom: 18px;
    }


    /* ================= INPUTS ================= */

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {

        background-color: #111827 !important;

        border:
            1px solid rgba(255,255,255,0.10) !important;

        border-radius: 11px !important;
    }

    input {
        color: #F8FAFC !important;
    }

    div[data-baseweb="select"] span {
        color: #F8FAFC !important;
    }


    /* ================= BUTTON ================= */

    div.stButton > button {

        width: 100%;

        min-height: 54px;

        border: none;

        border-radius: 14px;

        background:
            linear-gradient(
                90deg,
                #2563EB,
                #7C3AED
            );

        color: white;

        font-size: 17px;

        font-weight: 750;

        box-shadow:
            0 10px 30px rgba(37,99,235,0.25);

        transition: all 0.25s ease;
    }

    div.stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 15px 35px rgba(37,99,235,0.40);
    }


    /* ================= RESULT ================= */

    .result-good {

        padding: 30px;

        border-radius: 20px;

        text-align: center;

        margin-top: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(16,185,129,0.18),
                rgba(6,182,212,0.08)
            );

        border:
            1px solid rgba(16,185,129,0.45);

        box-shadow:
            0 15px 40px rgba(16,185,129,0.10);
    }

    .result-bad {

        padding: 30px;

        border-radius: 20px;

        text-align: center;

        margin-top: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(239,68,68,0.18),
                rgba(245,158,11,0.08)
            );

        border:
            1px solid rgba(239,68,68,0.45);

        box-shadow:
            0 15px 40px rgba(239,68,68,0.10);
    }

    .result-icon {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 8px;
        color: #FFFFFF !important;
    }

    .result-text {
        font-size: 14px;
        color: #CBD5E1 !important;
    }


    /* ================= INFO CARDS ================= */

    .info-card {

        background: #111827;

        border:
            1px solid rgba(255,255,255,0.08);

        border-radius: 16px;

        padding: 18px;

        height: 100%;
    }

    .info-number {
        font-size: 26px;
        font-weight: 800;

        color: #60A5FA !important;
    }

    .info-title {
        font-size: 14px;
        font-weight: 700;

        color: #F8FAFC !important;

        margin-top: 4px;
    }

    .info-text {
        font-size: 12px;

        color: #94A3B8 !important;

        margin-top: 5px;
    }


    /* ================= PIPELINE ================= */

    .pipeline {

        padding: 20px;

        border-radius: 18px;

        background:
            linear-gradient(
                135deg,
                rgba(37,99,235,0.10),
                rgba(124,58,237,0.08)
            );

        border:
            1px solid rgba(255,255,255,0.08);
    }

    .pipeline-step {

        padding: 13px 16px;

        margin: 8px 0;

        border-radius: 12px;

        background: rgba(17,24,39,0.85);

        border:
            1px solid rgba(255,255,255,0.06);

        color: #CBD5E1 !important;
    }


    /* ================= FOOTER ================= */

    .footer {

        text-align: center;

        padding: 30px 10px 15px;

        color: #64748B !important;

        font-size: 13px;
    }

    .footer strong {
        color: #94A3B8 !important;
    }


    /* ================= SIDEBAR ================= */

    section[data-testid="stSidebar"] {

        background: #0B1220;

        border-right:
            1px solid rgba(255,255,255,0.08);
    }


    /* ================= MOBILE ================= */

    @media (max-width: 768px) {

        .hero-title {
            font-size: 30px;
        }

        .hero {
            padding: 22px;
        }

        .card {
            padding: 18px;
        }
    }

    </style>
    """
)


# =========================================================
# MODEL + ENCODERS
# =========================================================

MODEL_PATH = get_path(
    "models",
    "extra_tress_credit_model.pkl"
)

ENCODER_PATHS = {
    "Sex": get_path(
        "encoders",
        "Sex_encoder.pkl"
    ),

    "Housing": get_path(
        "encoders",
        "Housing_encoder.pkl"
    ),

    "Saving accounts": get_path(
        "encoders",
        "Saving accounts_encoder.pkl"
    ),

    "Checking account": get_path(
        "encoders",
        "Checking account_encoder.pkl"
    ),

    "Purpose": get_path(
        "encoders",
        "Purpose_encoder.pkl"
    )
}


# =========================================================
# SAFE MODEL LOADING
# =========================================================

try:

    model = joblib.load(MODEL_PATH)

    encoders = {
        name: joblib.load(path)
        for name, path in ENCODER_PATHS.items()
    }

except FileNotFoundError as e:

    st.error(
        "Model or encoder file was not found."
    )

    st.code(
        str(e)
    )

    st.info(
        "Make sure the models and encoders folders are present "
        "in the GitHub repository."
    )

    st.stop()

except Exception as e:

    st.error(
        "Unable to load the machine learning model."
    )

    st.code(
        str(e)
    )

    st.stop()


# =========================================================
# HERO
# =========================================================

st.html(
    """
    <div class="hero">

        <div class="hero-title">
            💳 Credit Risk Prediction
        </div>

        <div class="hero-subtitle">
            AI-powered credit risk assessment for loan applicants
        </div>

        <div class="badge-container">

            <span class="badge">Python</span>
            <span class="badge">Machine Learning</span>
            <span class="badge">Extra Trees</span>
            <span class="badge">Scikit-learn</span>
            <span class="badge">Streamlit</span>

        </div>

    </div>
    """
)


# =========================================================
# INFORMATION CARDS
# =========================================================

info1, info2, info3, info4 = st.columns(4)


with info1:

    st.html(
        """
        <div class="info-card">

            <div class="info-number">
                01
            </div>

            <div class="info-title">
                Applicant Analysis
            </div>

            <div class="info-text">
                Evaluate applicant financial and personal information.
            </div>

        </div>
        """
    )


with info2:

    st.html(
        """
        <div class="info-card">

            <div class="info-number">
                02
            </div>

            <div class="info-title">
                Feature Encoding
            </div>

            <div class="info-text">
                Convert categorical applicant information into model-ready values.
            </div>

        </div>
        """
    )


with info3:

    st.html(
        """
        <div class="info-card">

            <div class="info-number">
                03
            </div>

            <div class="info-title">
                ML Prediction
            </div>

            <div class="info-text">
                Extra Trees model processes the applicant data.
            </div>

        </div>
        """
    )


with info4:

    st.html(
        """
        <div class="info-card">

            <div class="info-number">
                04
            </div>

            <div class="info-title">
                Risk Result
            </div>

            <div class="info-text">
                The application returns a Good or Bad credit risk result.
            </div>

        </div>
        """
    )


st.write("")
st.write("")


# =========================================================
# INPUT SECTION
# =========================================================

left_col, right_col = st.columns(
    [1, 1],
    gap="large"
)


# =========================================================
# APPLICANT DETAILS
# =========================================================

with left_col:

    st.html(
        """
        <div class="card">

            <div class="card-title">
                👤 Applicant Details
            </div>

            <div class="card-description">
                Enter the applicant's basic information.
            </div>

        </div>
        """
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=30
    )

    sex = st.selectbox(
        "Sex",
        [
            "male",
            "female"
        ]
    )

    job = st.selectbox(
        "Job",
        [
            0,
            1,
            2,
            3
        ]
    )

    housing = st.selectbox(
        "Housing",
        [
            "own",
            "rent",
            "free"
        ]
    )


# =========================================================
# LOAN DETAILS
# =========================================================

with right_col:

    st.html(
        """
        <div class="card">

            <div class="card-title">
                💰 Loan Details
            </div>

            <div class="card-description">
                Enter the applicant's financial and loan information.
            </div>

        </div>
        """
    )

    saving = st.selectbox(
        "Saving Account",
        [
            "little",
            "moderate",
            "quite rich",
            "rich"
        ]
    )

    checking = st.selectbox(
        "Checking Account",
        [
            "little",
            "moderate",
            "rich"
        ]
    )

    credit = st.number_input(
        "Credit Amount",
        min_value=0,
        max_value=100000,
        value=1000
    )

    duration = st.number_input(
        "Duration (Months)",
        min_value=1,
        max_value=72,
        value=12
    )


# =========================================================
# LOAN PURPOSE
# =========================================================

st.html(
    """
    <div class="card">

        <div class="card-title">
            🎯 Loan Purpose
        </div>

        <div class="card-description">
            Select the purpose for which the credit is being requested.
        </div>

    </div>
    """
)


purpose = st.selectbox(
    "Select Loan Purpose",
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
st.write("")


# =========================================================
# PREDICTION BUTTON
# =========================================================

predict_col1, predict_col2, predict_col3 = st.columns(
    [1, 2, 1]
)


with predict_col2:

    predict_button = st.button(
        "🔍  PREDICT CREDIT RISK",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    try:

        data = pd.DataFrame({
            "Age": [age],

            "Sex": [
                encoders["Sex"].transform([sex])[0]
            ],

            "Job": [job],

            "Housing": [
                encoders["Housing"].transform([housing])[0]
            ],

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


        # =================================================
        # GOOD CREDIT RISK
        # =================================================

        if prediction == 1:

            st.html(
                """
                <div class="result-good">

                    <div class="result-icon">
                        🟢
                    </div>

                    <div class="result-title">
                        GOOD CREDIT RISK
                    </div>

                    <div class="result-text">
                        Applicant shows a lower credit risk.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # =================================================
        # BAD CREDIT RISK
        # =================================================

        else:

            st.html(
                """
                <div class="result-bad">

                    <div class="result-icon">
                        🔴
                    </div>

                    <div class="result-title">
                        BAD CREDIT RISK
                    </div>

                    <div class="result-text">
                        Applicant shows a higher credit risk.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    except Exception as e:

        st.error(
            "Prediction failed."
        )

        st.code(
            str(e)
        )


# =========================================================
# HOW IT WORKS
# =========================================================

st.write("")
st.write("")


with st.expander(
    "⚙️ How This Credit Risk System Works"
):

    st.html(
        """
        <div class="pipeline">

            <div class="pipeline-step">
                <strong>1️⃣ Applicant Input</strong><br>
                Applicant and loan information is entered through the interface.
            </div>

            <div class="pipeline-step">
                <strong>2️⃣ Categorical Encoding</strong><br>
                Categorical applicant information is transformed using
                the trained encoders.
            </div>

            <div class="pipeline-step">
                <strong>3️⃣ Feature DataFrame</strong><br>
                The processed values are assembled into the feature
                structure expected by the trained model.
            </div>

            <div class="pipeline-step">
                <strong>4️⃣ Extra Trees Prediction</strong><br>
                The trained Extra Trees model generates the credit risk prediction.
            </div>

            <div class="pipeline-step">
                <strong>5️⃣ Final Result</strong><br>
                The application displays either Good Credit Risk or Bad Credit Risk.
            </div>

        </div>
        """
    )


# =========================================================
# MODEL INFORMATION
# =========================================================

with st.expander(
    "🤖 About the Machine Learning Model"
):

    st.html(
        """
        <div class="card">

            <div class="card-title">
                Extra Trees Classifier
            </div>

            <div class="card-description">
                This application uses a trained Extra Trees machine learning
                model to classify credit risk based on applicant and loan
                information.
            </div>

        </div>
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="footer">

        <strong>💳 Credit Risk Modelling</strong>

        <br>

        Machine Learning • Python • Scikit-learn • Streamlit

        <br><br>

        Built &amp; Deployed by Harsh Antla

    </div>
    """
)