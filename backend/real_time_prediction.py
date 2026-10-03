import time
import joblib
import pandas as pd

from real_time_simulator import generate_sensor_data


# Load trained ML model
model = joblib.load(
    "models/predictive_maintenance_model.pkl"
)

print("========================================")
print(" Real-Time ML Prediction System")
print("========================================")
print("ML Model loaded successfully")
print("Press CTRL+C to stop\n")


try:
    while True:

        # Get live simulated sensor data
        sensor_data = generate_sensor_data()

        # Prepare data for ML model
        input_data = pd.DataFrame([{
            "Type": 0,
            "Air temperature [K]": sensor_data["air_temperature"],
            "Process temperature [K]": sensor_data["process_temperature"],
            "Rotational speed [rpm]": sensor_data["rotational_speed"],
            "Torque [Nm]": sensor_data["torque"],
            "Tool wear [min]": sensor_data["tool_wear"],
            "TWF": 0,
            "HDF": 0,
            "PWF": 0,
            "OSF": 0,
            "RNF": 0
        }])

        # Prediction
        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1] * 100

        if prediction == 1:
            status = "MAINTENANCE REQUIRED"
        elif probability >= 30:
            status = "MONITOR"
        else:
            status = "NORMAL"

        print("----------------------------------------")
        print(
            f"Temperature      : {sensor_data['air_temperature']} K"
        )
        print(
            f"Process Temp.    : {sensor_data['process_temperature']} K"
        )
        print(
            f"RPM              : {sensor_data['rotational_speed']}"
        )
        print(
            f"Torque           : {sensor_data['torque']} Nm"
        )
        print(
            f"Tool Wear        : {sensor_data['tool_wear']} min"
        )
        print(
            f"Vibration        : {sensor_data['vibration']} g"
        )

        print(f"Failure Probability : {probability:.2f}%")
        print(f"Machine Prediction  : {status}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nReal-time prediction stopped.")