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
