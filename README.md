# Predictive Maintenance System using Machine Learning

## 📌 Project Overview

The Predictive Maintenance System is a Machine Learning based application designed to predict whether a machine is likely to fail based on sensor and operational data.

The system analyzes machine parameters such as air temperature, process temperature, rotational speed, torque, and tool wear to predict machine failure and determine the maintenance risk level.

The project combines Data Science, Machine Learning, Big Data processing, FastAPI, SQLite database, and dashboard visualization.

---

## 🎯 Objectives

- Predict machine failure using Machine Learning
- Analyze industrial machine sensor data
- Compare different Machine Learning models
- Provide failure probability and risk status
- Store prediction history in a database
- Provide an API for machine failure prediction
- Implement Big Data processing using PySpark
- Develop an interactive dashboard for monitoring

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Logistic Regression
- Gradient Boosting
- PySpark
- FastAPI
- SQLite
- Streamlit
- Matplotlib
- Joblib
- Git & GitHub

---

## 📊 Dataset

The project uses the **AI4I 2020 Predictive Maintenance Dataset**.

Dataset size:

- Records: 10,000
- Features: 14
- Target: Machine Failure

Important parameters include:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear
- Machine Failure

---

## 🤖 Machine Learning Models

The following models are implemented and compared:

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier

The project evaluates models using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The trained Random Forest model is saved as:

`models/predictive_maintenance_model.pkl`

---

## ⚙️ System Architecture

```text
Machine Sensor Data
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Machine Learning Models
        ↓
Model Comparison
        ↓
Best Model
        ↓
FastAPI Backend
        ↓
SQLite Database
        ↓
Streamlit Dashboard
        ↓
Prediction & Risk Monitoring
---

## 🚦 Risk Classification

| Failure Probability | Risk Status |
|---|---|
| 0% - 30% | NORMAL |
| 30% - 60% | MONITOR |
| 60% - 100% | MAINTENANCE REQUIRED |

---

## 🗄️ Database

SQLite is used to store prediction history including machine parameters, prediction results, failure probability, risk status, and prediction time.

---

## 🚀 FastAPI Backend

The FastAPI backend provides APIs for machine failure prediction and prediction history.

### API Endpoints

- `GET /` - API status
- `GET /health` - System health check
- `POST /predict` - Predict machine failure
- `GET /history` - View prediction history

Interactive API documentation:

`http://127.0.0.1:8000/docs`

---

## 👨‍🎓 Student Information

**Student:** Vedant Ajay Ware  
**Roll No.:** 75  
**Class:** TY B.Sc. Data Science  
**Department:** CASAS Department  
**College:** New Arts, Commerce and Science College, Ahilyanagar  
**Project Mentor:** Mansi Gugale

---

## 📌 Project Status

🚧 Project under development

- ✅ Dataset Analysis
- ✅ Data Preprocessing
- ✅ Machine Learning Models
- ✅ Model Comparison
- ✅ Random Forest Model
- ✅ Prediction System
- ✅ FastAPI Backend
- ✅ SQLite Database
- 🔄 Streamlit Dashboard Integration
- 🔄 Final Testing
---

## 📁 Project Structure

```text
Predictive-Maintenance-System/
│
├── backend/
│   ├── app.py
│   └── database.py
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── predictive_maintenance.csv
│
├── models/
│   └── predictive_maintenance_model.pkl
│
├── notebooks/
│   ├── 01_data_analysis.py
│   ├── 02_preprocessing.py
│   ├── 03_model_training.py
│   └── 04_prediction.py
│
├── reports/
│
├── .gitignore
├── requirements.txt
└── README.md
