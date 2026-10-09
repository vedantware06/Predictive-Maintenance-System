import sqlite3
from datetime import datetime

# ==========================================
# DATABASE PATH
# ==========================================

DATABASE_PATH = "database/predictive_maintenance.db"


# ==========================================
# CREATE DATABASE TABLE
# ==========================================

def create_table():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            machine_type INTEGER,

            air_temperature REAL,

            process_temperature REAL,

            rotational_speed REAL,

            torque REAL,

            tool_wear REAL,

            prediction INTEGER,

            failure_probability REAL,

            risk_status TEXT,

            created_at TEXT
        )
    """)

    connection.commit()

    connection.close()


# ==========================================
# SAVE PREDICTION
# ==========================================

def save_prediction(
    machine_type,
    air_temperature,
    process_temperature,
    rotational_speed,
    torque,
    tool_wear,
    prediction,
    failure_probability,
    risk_status
):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions (

            machine_type,
            air_temperature,
            process_temperature,
            rotational_speed,
            torque,
            tool_wear,
            prediction,
            failure_probability,
            risk_status,
            created_at

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        machine_type,
        air_temperature,
        process_temperature,
        rotational_speed,
        torque,
        tool_wear,
        prediction,
        failure_probability,
        risk_status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ))

    connection.commit()

    connection.close()


# ==========================================
# GET PREDICTION HISTORY
# ==========================================

def get_predictions():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            machine_type,
            air_temperature,
            process_temperature,
            rotational_speed,
            torque,
            tool_wear,
            prediction,
            failure_probability,
            risk_status,
            created_at

        FROM predictions

        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows