# 💳 Credit Risk Modeling & Prediction

An end-to-end **Machine Learning Credit Risk Modeling project** that predicts whether a loan applicant represents a **Good or Bad Credit Risk** based on financial and demographic information.

The project covers the complete machine learning workflow — from **data cleaning and exploratory data analysis (EDA)** to **feature encoding, model training, hyperparameter tuning, evaluation, model serialization, and Streamlit deployment**.

---

## 🚀 Project Overview

Credit risk assessment is an important task in the banking and financial industry. Incorrectly approving high-risk applicants can lead to financial losses, while rejecting reliable applicants can result in missed business opportunities.

This project uses the **German Credit Dataset** to build classification models capable of predicting an applicant's credit risk.

### 🎯 Objective

The primary objective is to:

- Analyze customer financial and demographic information
- Perform data cleaning and preprocessing
- Explore relationships between applicant characteristics and credit risk
- Encode categorical variables for machine learning
- Train and compare multiple classification algorithms
- Perform hyperparameter tuning using `GridSearchCV`
- Evaluate model performance
- Save the trained model and preprocessing encoders
- Build an interactive **Streamlit web application** for real-time prediction

---

## 🧠 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Categorical Encoding
     ↓
Train-Test Split
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
Streamlit Deployment
     ↓
Credit Risk Prediction
```

---

## 📊 Dataset

The project uses the **German Credit Dataset**.

The dataset contains information about loan applicants such as:

| Feature | Description |
|---|---|
| Age | Applicant's age |
| Sex | Applicant's gender |
| Job | Job category |
| Housing | Housing status |
| Saving accounts | Savings account status |
| Checking account | Checking account status |
| Credit amount | Requested credit amount |
| Duration | Loan duration in months |
| Purpose | Purpose of the loan |
| Risk | Target variable: Good / Bad |

### Target Variable

**Risk**

- `Good` → Good Credit Risk
- `Bad` → Bad Credit Risk

---

## 🔍 Exploratory Data Analysis

The project performs extensive EDA to understand the dataset and identify patterns in credit risk.

Visualizations include:

- Distribution plots
- Histograms
- Box plots
- Violin plots
- Count plots
- Scatter plots
- Correlation analysis
- Pivot tables
- Feature-wise risk analysis

The analysis focuses on relationships between variables such as:

- Age vs Credit Amount
- Credit Amount vs Risk
- Housing vs Credit Amount
- Savings Account vs Credit Amount
- Loan Purpose vs Risk
- Applicant characteristics vs Credit Risk

---

## 🛠️ Data Preprocessing

The following preprocessing steps were performed:

### Missing Value Handling

Missing values were handled during the data-cleaning stage, followed by index resetting.

### Categorical Encoding

Categorical variables were converted into numerical representations using **Label Encoding**.

Encoders were separately saved using `joblib` so that the same transformations could be applied during prediction in the Streamlit application.

Encoded features include:

- Sex
- Housing
- Saving accounts
- Checking account
- Purpose

The target variable `Risk` was also encoded.

---

## 🤖 Models Implemented

Multiple machine learning classification algorithms were trained and compared:

1. Decision Tree Classifier
2. Random Forest Classifier
3. Extra Trees Classifier
4. XGBoost Classifier

Hyperparameter optimization was performed using:

```python
GridSearchCV
```

with **5-fold cross-validation** and accuracy as the scoring metric.

---

## 📈 Model Performance

The models achieved the following test-set accuracy:

| Model | Accuracy |
|---|---:|
| Decision Tree | 59.05% |
| Random Forest | 63.81% |
| Extra Trees | 65.71% |
| XGBoost | **73.33%** |

### 🏆 Best Model Performance

Based on the evaluation performed in the notebook, **XGBoost achieved the highest test accuracy of 73.33%** among the compared models.

> **Deployment Note:** The current Streamlit application loads the serialized `Extra Trees` model (`extra_tress_credit_model.pkl`). Therefore, the deployed application and the best-performing experimental model are currently separate. This is intentionally documented to keep the project technically transparent.

---

## 🌐 Streamlit Application

The project includes an interactive **Streamlit-based Credit Risk Prediction application**.

Users can enter applicant information such as:

- Age
- Sex
- Job
- Housing
- Saving Account
- Checking Account
- Credit Amount
- Loan Duration
- Loan Purpose

The application processes the inputs using the saved encoders and generates a credit-risk prediction.

### Application Output

The application provides one of two outcomes:

```text
✅ GOOD CREDIT RISK
```

or

```text
❌ BAD CREDIT RISK
```

---

## 📁 Project Structure

```text
Credit Risk Modeling/
│
├── analysis_model.ipynb
├── app.py
├── german_credit_data.csv
│
├── extra_tress_credit_model.pkl
│
├── Sex_encoder.pkl
├── Housing_encoder.pkl
├── Saving accounts_encoder.pkl
├── Checking account_encoder.pkl
├── Purpose_encoder.pkl
├── target_encoder.pkl
│
└── Project Images/
    ├── App Dashboard Image.jpg
    ├── Good Credit Risk.jpg
    └── Bad Credit Risk.jpg
```

### File Description

| File | Purpose |
|---|---|
| `analysis_model.ipynb` | Complete data analysis, preprocessing, model training and evaluation |
| `app.py` | Streamlit application for real-time prediction |
| `german_credit_data.csv` | Dataset used for model development |
| `extra_tress_credit_model.pkl` | Serialized Extra Trees model used by the Streamlit app |
| `*_encoder.pkl` | Saved categorical encoders used during prediction |
| `target_encoder.pkl` | Saved target-label encoder |
| `Project Images/` | Screenshots demonstrating the application and predictions |

---

## ⚙️ Technologies Used

### Programming Language
- Python

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- XGBoost

### Model Optimization
- GridSearchCV

### Model Serialization
- Joblib

### Deployment
- Streamlit

### Development Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/credit-risk-modeling.git
```

Navigate to the project directory:

```bash
cd credit-risk-modeling
```

Install the required dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib streamlit
```

---

## ▶️ Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Prediction

### Good Credit Risk

The application displays:

```text
✅ GOOD CREDIT RISK
```

when the model predicts a low-risk applicant.

### Bad Credit Risk

The application displays:

```text
❌ BAD CREDIT RISK
```

when the model predicts a high-risk applicant.

---

## 📸 Project Screenshots

### Streamlit Dashboard

### Good Credit Risk Prediction

### Bad Credit Risk Prediction

---

## 🔑 Key Machine Learning Concepts Demonstrated

This project demonstrates practical implementation of:

- Exploratory Data Analysis
- Data Cleaning
- Missing Value Handling
- Feature Selection
- Categorical Encoding
- Train-Test Split
- Stratified Sampling
- Classification
- Ensemble Learning
- Decision Trees
- Random Forest
- Extra Trees
- XGBoost
- Hyperparameter Tuning
- Cross-Validation
- Model Evaluation
- Model Serialization
- Streamlit Deployment

---

## 📌 Future Improvements

Potential improvements for the project include:

- Add Precision, Recall, F1-Score and ROC-AUC evaluation
- Add confusion matrix visualization
- Implement probability-based risk scoring
- Use a preprocessing pipeline to combine transformations and modeling
- Deploy the application using Streamlit Cloud
- Add model explainability using SHAP
- Improve class-imbalance handling
- Add automated model monitoring
- Deploy the best-performing XGBoost model consistently with the application

---

## 🎯 Business Impact

A production-grade credit risk system can help financial institutions:

- Identify potentially high-risk applicants
- Support faster credit assessment
- Reduce manual evaluation effort
- Improve consistency in lending decisions
- Assist financial teams in risk-based decision making

> **Note:** This project is developed for educational and portfolio purposes and should not be used as the sole basis for real-world lending decisions.

---

## 👨‍💻 Author

**Harsh**

B.Tech CSE | Data Science & Machine Learning

Interested in building practical **Machine Learning, Data Science and AI applications**.

---

## ⭐ If You Found This Project Useful

If you found this project interesting, consider giving the repository a ⭐ on GitHub.
