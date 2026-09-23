import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/predictive_maintenance.csv")

print("===== ORIGINAL DATA =====")
print("Shape:", df.shape)

# Remove unnecessary columns
df = df.drop(columns=["UDI", "Product ID"])

# Convert machine Type into numerical values
df["Type"] = df["Type"].map({
    "L": 0,
    "M": 1,
    "H": 2
})

print("\n===== AFTER PREPROCESSING =====")
print(df.head())

print("\nShape:", df.shape)

# Features and target
X = df.drop(columns=["Machine failure"])
y = df["Machine failure"]

print("\n===== FEATURES =====")
print(X.columns.tolist())

print("\n===== TARGET =====")
print(y.name)

print("\n===== TARGET DISTRIBUTION =====")
print(y.value_counts())

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n===== TRAIN TEST SPLIT =====")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

print("\n===== PREPROCESSING COMPLETED =====")