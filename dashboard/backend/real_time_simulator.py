import random
import time
from datetime import datetime


def generate_sensor_data():
    """Generate simulated real-time machine sensor data."""

    air_temperature = round(random.uniform(298, 305), 2)
    process_temperature = round(
        air_temperature + random.uniform(8, 12), 2
    )

    rotational_speed = random.randint(1300, 1700)

    torque = round(random.uniform(35, 55), 2)

    tool_wear = random.randint(50, 200)

    vibration = round(random.uniform(1.0, 5.0), 2)

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "air_temperature": air_temperature,
        "process_temperature": process_temperature,
        "rotational_speed": rotational_speed,
        "torque": torque,
        "tool_wear": tool_wear,
        "vibration": vibration
    }


if __name__ == "__main__":

    print("===================================")
    print(" Real-Time Machine Sensor Simulator")
    print("===================================")
    print("Press CTRL+C to stop\n")

    try:
        while True:

            sensor_data = generate_sensor_data()

            print(
                f"[{sensor_data['timestamp']}] "
                f"Temperature: {sensor_data['air_temperature']} K | "
                f"Process: {sensor_data['process_temperature']} K | "
                f"RPM: {sensor_data['rotational_speed']} | "
                f"Torque: {sensor_data['torque']} Nm | "
                f"Tool Wear: {sensor_data['tool_wear']} min | "
                f"Vibration: {sensor_data['vibration']} g"
            )

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nSimulator stopped.")