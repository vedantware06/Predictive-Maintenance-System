import pandas as pd
import joblib

# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load(
    "models/predictive_maintenance_model.pkl"
)

print("==========================================")
print("PREDICTIVE MAINTENANCE SYSTEM")
print("==========================================")

print("\nTrained model loaded successfully.")


# ==========================================
# SAMPLE MACHINE INPUT
# ==========================================

machine_data = pd.DataFrame([{
    "Type": 0,
    "Air temperature [K]": 300.0,
    "Process temperature [K]": 310.0,
    "Rotational speed [rpm]": 1500,
    "Torque [Nm]": 40.0,
    "Tool wear [min]": 100,
    "TWF": 0,
    "HDF": 0,
    "PWF": 0,
    "OSF": 0,
    "RNF": 0
}])


# ==========================================
# DISPLAY INPUT
# ==========================================

print("\n===== MACHINE INPUT =====")

print(machine_data)


# ==========================================
# PREDICTION
# ==========================================

prediction = model.predict(machine_data)[0]

probability = model.predict_proba(machine_data)[0][1]

failure_probability = probability * 100


# ==========================================
# RISK STATUS
# ==========================================

if failure_probability < 30:
    risk_status = "NORMAL"

elif failure_probability < 60:
    risk_status = "MONITOR"

else:
    risk_status = "MAINTENANCE REQUIRED"


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n==========================================")
print("PREDICTION RESULT")
print("==========================================")

if prediction == 0:
    print("Machine Failure Prediction : NO FAILURE")
else:
    print("Machine Failure Prediction : FAILURE")

print(
    "Failure Probability         :",
    round(failure_probability, 2),
    "%"
)

print("Risk Status                 :", risk_status)

print("==========================================")

print("\nPrediction completed successfully.")