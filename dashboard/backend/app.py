from fastapi import FastAPI
import pandas as pd
import joblib

from backend.database import (
    create_table,
    save_prediction,
    get_predictions
)

from backend.real_time_simulator import generate_sensor_data


# ==========================================
# CREATE FASTAPI APP
# ==========================================

app = FastAPI(
    title="Predictive Maintenance API",
    description="Machine Failure Prediction API",
    version="1.0"
)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load(
    "models/predictive_maintenance_model.pkl"
)


# ==========================================
# CREATE DATABASE TABLE
# ==========================================

create_table()


# ==========================================
# HOME API
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Predictive Maintenance API is running"
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "Running",
        "model": "Random Forest",
        "database": "Connected"
    }


# ==========================================
# NORMAL PREDICTION API
# ==========================================

@app.post("/predict")
def predict(

    Type: int,

    air_temperature: float,

    process_temperature: float,

    rotational_speed: float,

    torque: float,

    tool_wear: float,

    TWF: int = 0,

    HDF: int = 0,

    PWF: int = 0,

    OSF: int = 0,

    RNF: int = 0

):

    # ======================================
    # CREATE MACHINE INPUT
    # ======================================

    machine_data = pd.DataFrame([{

        "Type": Type,

        "Air temperature [K]":
            air_temperature,

        "Process temperature [K]":
            process_temperature,

        "Rotational speed [rpm]":
            rotational_speed,

        "Torque [Nm]":
            torque,

        "Tool wear [min]":
            tool_wear,

        "TWF": TWF,

        "HDF": HDF,

        "PWF": PWF,

        "OSF": OSF,

        "RNF": RNF

    }])


    # ======================================
    # MODEL PREDICTION
    # ======================================

    prediction = model.predict(
        machine_data
    )[0]

    probability = model.predict_proba(
        machine_data
    )[0][1]

    failure_probability = probability * 100


    # ======================================
    # RISK STATUS
    # ======================================

    if failure_probability < 30:

        risk_status = "NORMAL"

    elif failure_probability < 60:

        risk_status = "MONITOR"

    else:

        risk_status = "MAINTENANCE REQUIRED"


    # ======================================
    # SAVE PREDICTION TO DATABASE
    # ======================================

    save_prediction(

        machine_type=Type,

        air_temperature=air_temperature,

        process_temperature=process_temperature,

        rotational_speed=rotational_speed,

        torque=torque,

        tool_wear=tool_wear,

        prediction=int(prediction),

        failure_probability=round(
            failure_probability,
            2
        ),

        risk_status=risk_status

    )


    # ======================================
    # RETURN RESULT
    # ======================================

    return {

        "machine_failure":
            int(prediction),

        "prediction":
            (
                "FAILURE"
                if prediction == 1
                else "NO FAILURE"
            ),

        "failure_probability":
            round(
                failure_probability,
                2
            ),

        "risk_status":
            risk_status,

        "database_status":
            "Prediction saved successfully"

    }


# ==========================================
# PREDICTION HISTORY API
# ==========================================

@app.get("/history")
def history():

    rows = get_predictions()

    results = []

    for row in rows:

        results.append({

            "id": row[0],

            "machine_type": row[1],

            "air_temperature": row[2],

            "process_temperature": row[3],

            "rotational_speed": row[4],

            "torque": row[5],

            "tool_wear": row[6],

            "prediction": row[7],

            "failure_probability": row[8],

            "risk_status": row[9],

            "created_at": row[10]

        })


    return {

        "total_predictions":
            len(results),

        "history":
            results

    }


# ==========================================
# REAL-TIME SENSOR PREDICTION API
# ==========================================

@app.get("/realtime")
def realtime_prediction():

    # ======================================
    # GENERATE LIVE SENSOR DATA
    # ======================================

    sensor_data = generate_sensor_data()


    # ======================================
    # PREPARE DATA FOR ML MODEL
    # ======================================

    machine_data = pd.DataFrame([{

        "Type": 0,

        "Air temperature [K]":
            sensor_data["air_temperature"],

        "Process temperature [K]":
            sensor_data["process_temperature"],

        "Rotational speed [rpm]":
            sensor_data["rotational_speed"],

        "Torque [Nm]":
            sensor_data["torque"],

        "Tool wear [min]":
            sensor_data["tool_wear"],

        "TWF": 0,

        "HDF": 0,

        "PWF": 0,

        "OSF": 0,

        "RNF": 0

    }])


    # ======================================
    # ML PREDICTION
    # ======================================

    prediction = model.predict(
        machine_data
    )[0]

    probability = model.predict_proba(
        machine_data
    )[0][1]

    failure_probability = probability * 100


    # ======================================
    # RISK STATUS
    # ======================================

    if failure_probability < 30:

        risk_status = "NORMAL"

    elif failure_probability < 60:

        risk_status = "MONITOR"

    else:

        risk_status = "MAINTENANCE REQUIRED"


    # ======================================
    # RETURN REAL-TIME RESULT
    # ======================================

    return {

        "sensor_data": sensor_data,

        "prediction":
            (
                "FAILURE"
                if prediction == 1
                else "NO FAILURE"
            ),

        "failure_probability":
            round(
                failure_probability,
                2
            ),

        "risk_status":
            risk_status

    }