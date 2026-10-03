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
st.caption(
    "AI-powered machine failure prediction, real-time monitoring and maintenance analytics"
)

st.divider()


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def get_history():

    try:
        response = requests.get(
            f"{API_URL}/history",
            timeout=5
        )

        if response.status_code == 200:
            return response.json().get("history", [])

    except Exception:
        pass

    return []


def get_realtime():

    try:
        response = requests.get(
            f"{API_URL}/realtime",
            timeout=5
        )

        if response.status_code == 200:
            return response.json()

    except Exception:
        pass

    return None


# ==========================================
# GET HISTORY
# ==========================================

history = get_history()


# ==========================================
# DASHBOARD STATISTICS
# ==========================================

total_predictions = len(history)

normal_count = sum(
    1 for item in history
    if item.get("risk_status") == "NORMAL"
)

monitor_count = sum(
    1 for item in history
    if item.get("risk_status") == "MONITOR"
)

maintenance_count = sum(
    1 for item in history
    if item.get("risk_status") == "MAINTENANCE REQUIRED"
)


# ==========================================
# TOP STATISTICS
# ==========================================

st.subheader("📊 System Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Predictions",
        total_predictions
    )

with col2:
    st.metric(
        "🟢 Normal",
        normal_count
    )

with col3:
    st.metric(
        "🟡 Monitor",
        monitor_count
    )

with col4:
    st.metric(
        "🔴 Maintenance",
        maintenance_count
    )


st.divider()


# ==========================================
# REAL-TIME MONITORING
# ==========================================

st.header("⚡ Real-Time Machine Monitoring")

st.caption(
    "Live sensor simulation with machine failure prediction"
)


realtime = get_realtime()


if realtime:

    sensor = realtime.get("sensor_data", {})

    prediction = realtime.get(
        "prediction",
        "UNKNOWN"
    )

    probability = realtime.get(
        "failure_probability",
        0
    )

    risk = realtime.get(
        "risk_status",
        "NORMAL"
    )


    # ======================================
    # MACHINE STATUS
    # ======================================

    if risk == "NORMAL":

        st.success(
            f"🟢 MACHINE STATUS: {risk}"
        )

    elif risk == "MONITOR":

        st.warning(
            f"🟡 MACHINE STATUS: {risk}"
        )

    else:

        st.error(
            f"🔴 MACHINE STATUS: {risk}"
        )


    # ======================================
    # SENSOR CARDS
    # ======================================

    sensor_col1, sensor_col2, sensor_col3, sensor_col4 = st.columns(4)

    with sensor_col1:

        st.metric(
            "🌡️ Air Temperature",
            f'{sensor.get("air_temperature", 0)} K'
        )

    with sensor_col2:

        st.metric(
            "🌡️ Process Temperature",
            f'{sensor.get("process_temperature", 0)} K'
        )

    with sensor_col3:

        st.metric(
            "⚙️ Rotational Speed",
            f'{sensor.get("rotational_speed", 0)} rpm'
        )

    with sensor_col4:

        st.metric(
            "🔧 Torque",
            f'{sensor.get("torque", 0)} Nm'
        )


    sensor_col5, sensor_col6, sensor_col7 = st.columns(3)

    with sensor_col5:

        st.metric(
            "🛠️ Tool Wear",
            f'{sensor.get("tool_wear", 0)} min'
        )

    with sensor_col6:

        st.metric(
            "📳 Vibration",
            f'{sensor.get("vibration", 0)}'
        )

    with sensor_col7:

        st.metric(
            "⚠️ Failure Probability",
            f"{probability}%"
        )


    # ======================================
    # PREDICTION RESULT
    # ======================================

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        st.info(
            f"🤖 Prediction: **{prediction}**"
        )

    with result_col2:

        if risk == "NORMAL":

            st.success(
                "Recommended Action: Continue operation"
            )

        elif risk == "MONITOR":

            st.warning(
                "Recommended Action: Monitor machine"
            )

        else:

            st.error(
                "Recommended Action: Schedule maintenance"
            )


    if sensor.get("timestamp"):

        st.caption(
            f"Last sensor update: {sensor.get('timestamp')}"
        )


else:

    st.error(
        "Real-time API is not available. Make sure FastAPI is running."
    )


st.divider()


# ==========================================
# MANUAL PREDICTION
# ==========================================

st.header("🤖 Manual Machine Failure Prediction")

input_col, failure_col = st.columns(2)


# ==========================================
# MACHINE PARAMETERS
# ==========================================

with input_col:

    st.subheader("Machine Parameters")

    machine_type = st.selectbox(
        "Machine Type",
        ["L", "M", "H"]
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
# FAILURE INDICATORS
# ==========================================

with failure_col:

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

    type_mapping = {
        "L": 0,
        "M": 1,
        "H": 2
    }

    params = {

        "Type": type_mapping[machine_type],

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

        response = requests.post(
            f"{API_URL}/predict",
            params=params,
            timeout=10
        )


        if response.status_code == 200:

            result = response.json()

            st.success(
                "Prediction completed successfully!"
            )


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


    except Exception:

        st.error(
            "Could not connect to FastAPI backend."
        )


st.divider()


# ==========================================
# ANALYTICS
# ==========================================

st.header("📈 Maintenance Analytics")


if history:

    history_df = pd.DataFrame(history)


    # ======================================
    # RISK DISTRIBUTION
    # ======================================

    chart_col1, chart_col2 = st.columns(2)


    with chart_col1:

        st.subheader("Risk Distribution")

        risk_counts = (
            history_df["risk_status"]
            .value_counts()
        )

        st.bar_chart(
            risk_counts
        )


    # ======================================
    # FAILURE PROBABILITY
    # ======================================

    with chart_col2:

        st.subheader("Failure Probability")

        if "failure_probability" in history_df.columns:

            probability_df = history_df[
                ["id", "failure_probability"]
            ].copy()

            probability_df = probability_df.set_index(
                "id"
            )

            st.line_chart(
                probability_df
            )


else:

    st.info(
        "Analytics will appear after predictions are generated."
    )


st.divider()


# ==========================================
# PREDICTION HISTORY
# ==========================================

st.header("📋 Prediction History")


if history:

    history_df = pd.DataFrame(history)


    if "prediction" in history_df.columns:

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


# ==========================================
# REFRESH BUTTON
# ==========================================

st.divider()

if st.button(
    "🔄 Refresh Dashboard",
    use_container_width=True
):

    st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.caption(
    "Predictive Maintenance System | "
    "Machine Learning + FastAPI + SQLite + Real-Time Monitoring"
)