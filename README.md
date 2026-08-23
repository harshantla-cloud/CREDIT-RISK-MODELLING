# 💳 Credit Risk Modelling

A Machine Learning based **Credit Risk Prediction System** that predicts whether a customer represents **Good Credit Risk** or **Bad Credit Risk** based on financial and personal attributes.

The project includes data preprocessing, exploratory data analysis, feature encoding, model training, evaluation, model saving, and an interactive **Streamlit web application** for real-time prediction.

---

## 🚀 Live Demo

🌐 **Streamlit App:** Add your deployed Streamlit URL here

---

## 📌 Project Overview

Credit risk assessment is an important task for banks and financial institutions.

Before approving a loan, financial institutions need to estimate the likelihood that a customer will repay the borrowed amount.

This project uses Machine Learning to classify applicants into:

- 🟢 **Good Credit Risk**
- 🔴 **Bad Credit Risk**

The goal is to build a practical ML application that can assist with credit-risk assessment using historical customer data.

---

## 🎯 Objectives

- Analyze customer credit data
- Perform data preprocessing and cleaning
- Encode categorical variables
- Train multiple Machine Learning classification models
- Compare model performance
- Save the trained model and encoders
- Build an interactive Streamlit application
- Generate real-time credit-risk predictions

---

## 🧠 Machine Learning Workflow

```text
Customer Credit Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Categorical Encoding
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Selection
        ↓
Model Serialization
        ↓
Streamlit Application
        ↓
Credit Risk Prediction
```

---

## 📊 Dataset

The project uses the **German Credit Dataset**.

The dataset contains customer information such as:

- Age
- Sex
- Job
- Housing
- Saving Accounts
- Checking Account
- Credit Amount
- Duration
- Purpose

### Dataset Location

```text
data/
└── german_credit_data.csv
```

---

## 🔍 Features Used

| Feature | Description |
|---|---|
| Age | Customer age |
| Sex | Customer gender |
| Job | Job category |
| Housing | Housing status |
| Saving accounts | Customer savings category |
| Checking account | Checking account status |
| Credit amount | Requested credit amount |
| Duration | Loan duration |
| Purpose | Purpose of the loan |

---

## 🤖 Machine Learning Models

The project experiments with multiple classification algorithms:

### 🌳 Decision Tree
Used as a baseline classification model.

### 🌲 Random Forest
An ensemble learning algorithm that combines multiple decision trees.

### 🌲 Extra Trees
An ensemble model based on randomized decision trees.

### ⚡ XGBoost
A gradient boosting algorithm used for classification.

---

## 📈 Model Performance

The models were evaluated using classification accuracy.

| Model | Accuracy |
|---|---:|
| Decision Tree | 59.05% |
| Random Forest | 63.81% |
| Extra Trees | 65.71% |
| XGBoost | **73.33%** |

### 🏆 Best Experimental Model

**XGBoost — 73.33% Accuracy**

> Note: The Streamlit application should use the same model reported as the deployed model. If `extra_tress_credit_model.pkl` is used in `app.py`, update this section to reflect the deployed Extra Trees model, or replace the deployed model with the trained XGBoost model.

---

## 💾 Saved Models

The trained model is stored using Joblib.

```text
models/
└── extra_tress_credit_model.pkl
```

Categorical encoders:

```text
encoders/
├── Sex_encoder.pkl
├── Housing_encoder.pkl
├── Saving accounts_encoder.pkl
├── Checking account_encoder.pkl
├── Purpose_encoder.pkl
└── target_encoder.pkl
```

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application where users can enter customer information and receive a credit-risk prediction.

### Application Features

- 📋 Customer information input
- 💰 Credit amount input
- 🏠 Housing information
- 💼 Job information
- 💳 Account information
- 🎯 Loan purpose selection
- ⚡ Real-time prediction
- 🟢 Good Credit Risk result
- 🔴 Bad Credit Risk result

---

## 📸 Project Screenshots

### Streamlit Dashboard

![Streamlit Dashboard](Project%20Images/App%20Dashboard%20Image.jpg)

### Good Credit Risk

![Good Credit Risk](Project%20Images/Good%20Credit%20Risk.jpg)

### Bad Credit Risk

![Bad Credit Risk](Project%20Images/Bad%20Credit%20Risk.jpg)

---

## 🏗️ Project Architecture

![Credit Risk Pipeline](Project%20Images/Project%20Structure%20Credit%20Risk%20Pipeline.png)

---

## 🔄 Project Workflow

![Project Workflow](Project%20Images/WORK%20FLOW%20OF%20PROJECT.png)

---

## 📂 Project Structure

```text
Credit-Risk-Modelling/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── german_credit_data.csv
│
├── models/
│   └── extra_tress_credit_model.pkl
│
├── encoders/
│   ├── Sex_encoder.pkl
│   ├── Housing_encoder.pkl
│   ├── Saving accounts_encoder.pkl
│   ├── Checking account_encoder.pkl
│   ├── Purpose_encoder.pkl
│   └── target_encoder.pkl
│
├── analysis_model.ipynb
│
└── Project Images/
    ├── App Dashboard Image.jpg
    ├── Bad Credit Risk.jpg
    ├── Good Credit Risk.jpg
    ├── Project Structure Credit Risk Pipeline.png
    ├── PROJECT STRUCTURE IMAGE.png
    └── WORK FLOW OF PROJECT.png
```

---

## 🛠️ Technologies Used

### Programming
- Python

### Data Science
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- XGBoost

### Model Serialization
- Joblib

### Deployment
- Streamlit

### Development Tools
- Jupyter Notebook
- Git
- GitHub

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/harshantla-cloud/CREDIT-RISK-MODELLING.git
```

### 2. Navigate to the Project

```bash
cd CREDIT-RISK-MODELLING
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

Recommended `requirements.txt`:

```text
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
```

---

## 🌐 Deployment

This application can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Deploy the application.
6. Add the generated public URL to the **Live Demo** section.

---

## 🧪 Prediction Flow

```text
User Input
    ↓
Data Validation
    ↓
Categorical Encoding
    ↓
Feature Preparation
    ↓
Trained ML Model
    ↓
Credit Risk Prediction
    ↓
Good / Bad Credit Risk
```

---

## 📚 Key Learnings

Through this project, I worked on:

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Categorical encoding
- Classification algorithms
- Model comparison
- Model evaluation
- Model serialization
- Streamlit application development
- Machine Learning deployment
- Git and GitHub workflow

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Class imbalance handling
- SHAP-based explainable AI
- Feature importance visualization
- Probability-based credit-risk scoring
- Improved Streamlit UI/UX
- Model monitoring
- Automated model retraining
- Cloud deployment

---

## ⚠️ Disclaimer

This project is created for **educational and portfolio purposes**.

The predictions should not be used as the sole basis for real-world financial or lending decisions. A production credit-risk system would require additional validation, fairness testing, security controls, regulatory compliance, and domain expertise.

---

## 👨‍💻 Author

### Harsh

**B.Tech – Computer Science & Engineering**

Aspiring **Data Scientist / Machine Learning Engineer**

### 🔗 Connect With Me

- 💻 GitHub: https://github.com/harshantla-cloud
- 🔗 LinkedIn: https://www.linkedin.com/in/harsh-5694b13ab

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

### 💳 Credit Risk Modelling

**Turning customer financial data into actionable credit-risk predictions using Machine Learning.**
