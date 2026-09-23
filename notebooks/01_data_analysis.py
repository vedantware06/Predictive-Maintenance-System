import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/predictive_maintenance.csv")

# ==============================
# BASIC DATA ANALYSIS
# ==============================

print("===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# ==============================
# FAILURE BY MACHINE TYPE
# ==============================

print("\n===== FAILURE BY MACHINE TYPE =====")
print(pd.crosstab(df["Type"], df["Machine failure"]))

print("\n===== FAILURE RATE BY MACHINE TYPE (%) =====")

failure_rate = df.groupby("Type")["Machine failure"].mean() * 100
print(failure_rate)


# ==============================
# SENSOR STATISTICS
# ==============================

print("\n===== SENSOR STATISTICS =====")

sensor_columns = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

print(df[sensor_columns].describe())


# ==============================
# NORMAL VS FAILURE COMPARISON
# ==============================

print("\n===== SENSOR COMPARISON: NORMAL vs FAILURE =====")

comparison = df.groupby("Machine failure")[sensor_columns].mean()

print(comparison)


# ==============================
# CORRELATION
# ==============================

print("\n===== CORRELATION WITH MACHINE FAILURE =====")

numeric_columns = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Machine failure"
]

correlation = df[numeric_columns].corr()["Machine failure"].sort_values(
    ascending=False
)

print(correlation)


# ==============================
# GRAPH 1: FAILURE DISTRIBUTION
# ==============================

print("\n===== FAILURE DISTRIBUTION =====")

failure_counts = df["Machine failure"].value_counts()

plt.figure(figsize=(6, 4))

plt.bar(
    ["No Failure", "Failure"],
    failure_counts.reindex([0, 1])
)

plt.title("Machine Failure Distribution")
plt.xlabel("Machine Status")
plt.ylabel("Number of Machines")
plt.tight_layout()

plt.savefig(
    "reports/failure_distribution.png",
    dpi=300
)

plt.close()

print("Failure distribution graph saved successfully.")


# ==============================
# GRAPH 2: MACHINE TYPE VS FAILURE
# ==============================

print("\n===== MACHINE TYPE VS FAILURE =====")

failure_by_type = pd.crosstab(
    df["Type"],
    df["Machine failure"]
)

plt.figure(figsize=(7, 5))

failure_by_type.plot(
    kind="bar",
    ax=plt.gca()
)

plt.title("Machine Failure by Machine Type")
plt.xlabel("Machine Type")
plt.ylabel("Number of Machines")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "reports/failure_by_machine_type.png",
    dpi=300
)

plt.close()

print("Machine type vs failure graph saved successfully.")


# ==============================
# ANALYSIS COMPLETED
# ==============================

print("\n====================================")
print("DATA ANALYSIS COMPLETED SUCCESSFULLY")
print("====================================")