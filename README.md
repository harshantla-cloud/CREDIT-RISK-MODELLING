# Credit Risk Modelling

Machine Learning system that predicts whether a loan applicant represents **Good Credit Risk** or **Bad Credit Risk** using customer and loan attributes.

## Overview

This project builds a credit-risk classification pipeline using the **German Credit Dataset**. It covers data preprocessing, exploratory analysis, categorical encoding, model training, hyperparameter tuning, evaluation, model serialization, and a Streamlit application for credit-risk prediction.

## Key Features

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Categorical feature encoding
- Multiple classification models
- Hyperparameter tuning using GridSearchCV
- Model comparison using accuracy
- Saved trained model and encoders
- Interactive Streamlit prediction interface

## Tech Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Model Persistence | Joblib |
| Application | Streamlit |
| Development | Jupyter Notebook |

## ML Workflow

```text
German Credit Dataset
        ↓
Data Cleaning
        ↓
Missing Value Handling
        ↓
Feature Selection
        ↓
Categorical Encoding
        ↓
Train-Test Split
        ↓
Model Training
        ↓
GridSearchCV
        ↓
Model Evaluation
        ↓
Model Serialization
        ↓
Streamlit Prediction
```

## Dataset

The project uses the **German Credit Dataset**.

| Detail | Value |
|---|---:|
| Original Records | 1,000 |
| Records After Cleaning | 522 |
| Features | 9 |
| Train/Test Split | 80/20 |
| Training Samples | 417 |
| Testing Samples | 105 |
| Target | `Risk` |

### Features

| Feature | Description |
|---|---|
| `Age` | Customer age |
| `Sex` | Customer sex |
| `Job` | Job category |
| `Housing` | Housing status |
| `Saving accounts` | Savings account category |
| `Checking account` | Checking account category |
| `Credit amount` | Credit amount |
| `Duration` | Loan duration |
| `Purpose` | Loan purpose |

### Target

`Risk`

- `good`
- `bad`

After preprocessing:

- Good Risk: **291**
- Bad Risk: **231**

## Model & Performance

Multiple classification models were evaluated:

| Model | Accuracy |
|---|---:|
| Decision Tree | 59.05% |
| Random Forest | 63.81% |
| Extra Trees | **65.71%** |
| XGBoost | 73.33% |

The saved model used by the Streamlit application is:

```text
models/extra_tress_credit_model.pkl
```

### Model Training

The Extra Trees model was tuned using **GridSearchCV with 5-fold cross-validation**.

**Extra Trees Test Accuracy:** `65.71%`

## Project Structure

```text
Credit Risk Modeling/
│
├── app.py
├── analysis_model.ipynb
├── requirements.txt
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
└── Project Images/
    ├── App Dashboard Image.jpg
    ├── Bad Credit Risk.jpg
    ├── Good Credit Risk.jpg
    ├── credit_risk_background.webp.webp
    ├── Project Structure Credit Risk Pipeline.png
    ├── PROJECT STRUCTURE IMAGE.png
    └── WORK FLOW OF PROJECT.png
```

## Installation & Run

### Clone the Repository

```bash
git clone https://github.com/harshantla-cloud/CREDIT-RISK-MODELLING.git
cd CREDIT-RISK-MODELLING
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

## Live Demo

[Credit Risk Modelling – Live Demo](https://harsh-credit-risk.streamlit.app/)

## Screenshots

### Streamlit Dashboard

![Streamlit Dashboard](Project%20Images/App%20Dashboard%20Image.jpg)

### Good Credit Risk

![Good Credit Risk](Project%20Images/Good%20Credit%20Risk.jpg)

### Bad Credit Risk

![Bad Credit Risk](Project%20Images/Bad%20Credit%20Risk.jpg)

### ML Workflow

![ML Workflow](Project%20Images/WORK%20FLOW%20OF%20PROJECT.png)

## Future Improvements

- Improve model performance through further hyperparameter tuning
- Add model explainability
- Add feature importance visualization
- Improve credit-risk scoring
- Enhance Streamlit UI/UX
- Add model monitoring
- Automate model retraining

## Author

**Harsh**

B.Tech – Computer Science & Engineering
