import streamlit as st
import requests
import pandas as pd


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Predictive Maintenance System",
    page_icon="⚙️",
    layout="wide"
)


# ==========================================
# API URL
# ==========================================

API_URL = "http://127.0.0.1:8000"


# ==========================================
# TITLE
# ==========================================

st.title("⚙️ Predictive Maintenance System")
st.write(
    "AI-powered machine failure prediction and maintenance monitoring dashboard"
)

st.divider()


# ==========================================
# GET HISTORY
# ==========================================

try:

    response = requests.get(
        f"{API_URL}/history",
        timeout=5
    )

    if response.status_code == 200:

        data = response.json()

        history = data.get("history", [])

    else:

        history = []

except Exception:

    history = []


# ==========================================
# DASHBOARD STATISTICS
# ==========================================

total_predictions = len(history)

normal_count = sum(
    1 for item in history
    if item["risk_status"] == "NORMAL"
)

monitor_count = sum(
    1 for item in history
    if item["risk_status"] == "MONITOR"
)

maintenance_count = sum(
    1 for item in history
    if item["risk_status"] == "MAINTENANCE REQUIRED"
)


# ==========================================
# DASHBOARD CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Predictions",
        total_predictions
    )

with col2:
    st.metric(
        "Normal",
        normal_count
    )

with col3:
    st.metric(
        "Monitor",
        monitor_count
    )

with col4:
    st.metric(
        "Maintenance Required",
        maintenance_count
    )


st.divider()


# ==========================================
# PREDICTION SECTION
# ==========================================

st.header("🤖 Machine Failure Prediction")

col1, col2 = st.columns(2)


# ==========================================
# MACHINE INPUTS
# ==========================================

with col1:

    st.subheader("Machine Parameters")

    machine_type = st.selectbox(
        "Machine Type",
        options=["L", "M", "H"]
    )

    air_temperature = st.number_input(
        "Air Temperature [K]",
        min_value=250.0,
        max_value=350.0,
        value=300.0
    )

    process_temperature = st.number_input(
        "Process Temperature [K]",
        min_value=250.0,
        max_value=350.0,
        value=310.0
    )

    rotational_speed = st.number_input(
        "Rotational Speed [rpm]",
        min_value=500,
        max_value=3000,
        value=1500
    )

    torque = st.number_input(
        "Torque [Nm]",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

    tool_wear = st.number_input(
        "Tool Wear [min]",
        min_value=0,
        max_value=300,
        value=100
    )


# ==========================================
# FAILURE FLAGS
# ==========================================

with col2:

    st.subheader("Failure Indicators")

    TWF = st.selectbox(
        "Tool Wear Failure (TWF)",
        [0, 1]
    )

    HDF = st.selectbox(
        "Heat Dissipation Failure (HDF)",
        [0, 1]
    )

    PWF = st.selectbox(
        "Power Failure (PWF)",
        [0, 1]
    )

    OSF = st.selectbox(
        "Overstrain Failure (OSF)",
        [0, 1]
    )

    RNF = st.selectbox(
        "Random Failure (RNF)",
        [0, 1]
    )


# ==========================================
# PREDICTION BUTTON
# ==========================================

if st.button(
    "🔮 Predict Machine Failure",
    use_container_width=True
):

    # Convert machine type
    type_mapping = {
        "L": 0,
        "M": 1,
        "H": 2
    }

    Type = type_mapping[machine_type]


    # API parameters

    params = {

        "Type": Type,

        "air_temperature": air_temperature,

        "process_temperature": process_temperature,

        "rotational_speed": rotational_speed,

        "torque": torque,

        "tool_wear": tool_wear,

        "TWF": TWF,

        "HDF": HDF,

        "PWF": PWF,

        "OSF": OSF,

        "RNF": RNF
    }


    try:

        prediction_response = requests.post(
            f"{API_URL}/predict",
            params=params,
            timeout=10
        )


        if prediction_response.status_code == 200:

            result = prediction_response.json()

            st.success("Prediction completed successfully!")


            st.divider()

            # ==================================
            # RESULT
            # ==================================

            result_col1, result_col2, result_col3 = st.columns(3)


            with result_col1:

                st.metric(
                    "Prediction",
                    result["prediction"]
                )


            with result_col2:

                st.metric(
                    "Failure Probability",
                    f'{result["failure_probability"]}%'
                )


            with result_col3:

                st.metric(
                    "Risk Status",
                    result["risk_status"]
                )


            # ==================================
            # RISK MESSAGE
            # ==================================

            if result["risk_status"] == "NORMAL":

                st.success(
                    "🟢 Machine condition is NORMAL."
                )

            elif result["risk_status"] == "MONITOR":

                st.warning(
                    "🟡 Machine should be MONITORED."
                )

            else:

                st.error(
                    "🔴 MAINTENANCE REQUIRED."
                )


        else:

            st.error(
                "Prediction API returned an error."
            )

    except Exception as e:

        st.error(
            "Could not connect to FastAPI backend."
        )

        st.info(
            "Make sure the FastAPI server is running."
        )


# ==========================================
# HISTORY SECTION
# ==========================================

st.divider()

st.header("📋 Prediction History")


# Refresh history

try:

    history_response = requests.get(
        f"{API_URL}/history",
        timeout=5
    )

    if history_response.status_code == 200:

        history_data = history_response.json()

        history = history_data.get(
            "history",
            []
        )

        if history:

            history_df = pd.DataFrame(history)

            # Convert prediction number
            history_df["prediction"] = history_df[
                "prediction"
            ].map({
                0: "NO FAILURE",
                1: "FAILURE"
            })


            st.dataframe(
                history_df,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No prediction history available."
            )

except Exception:

    st.warning(
        "Unable to load prediction history."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Predictive Maintenance System | "
    "Machine Learning + FastAPI + SQLite"
)