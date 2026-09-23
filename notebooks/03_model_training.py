import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("data/predictive_maintenance.csv")

print("===== DATASET LOADED =====")
print("Shape:", df.shape)


# ==========================================
# DATA PREPROCESSING
# ==========================================

# Remove unnecessary columns
df = df.drop(columns=["UDI", "Product ID"])

# Convert machine Type to numerical values
df["Type"] = df["Type"].map({
    "L": 0,
    "M": 1,
    "H": 2
})


# ==========================================
# FEATURES AND TARGET
# ==========================================

X = df.drop(columns=["Machine failure"])
y = df["Machine failure"]

print("\n===== FEATURES =====")
print(X.columns.tolist())

print("\n===== TARGET =====")
print("Machine failure")


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

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


# ==========================================
# DEFINE MODELS
# ==========================================

models = {

    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    ),

    "Gradient Boosting": GradientBoostingClassifier(
        n_estimators=100,
        random_state=42
    )
}


# ==========================================
# TRAIN AND EVALUATE MODELS
# ==========================================

results = []

print("\n==========================================")
print("MODEL TRAINING STARTED")
print("==========================================")

for name, model in models.items():

    print("\nTraining:", name)

    # Train model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))


# ==========================================
# MODEL COMPARISON
# ==========================================

results_df = pd.DataFrame(results)

print("\n==========================================")
print("MODEL COMPARISON")
print("==========================================")

print(results_df)


# ==========================================
# SAVE MODEL COMPARISON
# ==========================================

results_df.to_csv(
    "reports/model_comparison.csv",
    index=False
)

print("\nModel comparison saved successfully.")


# ==========================================
# CONFUSION MATRIX - RANDOM FOREST
# ==========================================

rf_model = models["Random Forest"]

rf_predictions = rf_model.predict(X_test)

cm = confusion_matrix(
    y_test,
    rf_predictions
)

print("\n==========================================")
print("RANDOM FOREST CONFUSION MATRIX")
print("==========================================")

print(cm)


# ==========================================
# SAVE CONFUSION MATRIX GRAPH
# ==========================================

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No Failure", "Failure"]
)

disp.plot()

plt.title("Random Forest - Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "reports/random_forest_confusion_matrix.png",
    dpi=300
)

plt.close()

print("Confusion matrix graph saved successfully.")


# ==========================================
# MODEL TRAINING COMPLETED
# ==========================================

print("\n==========================================")
print("MODEL TRAINING COMPLETED SUCCESSFULLY")
print("==========================================")
# ==========================================
# SAVE BEST MODEL
# ==========================================

import joblib

best_model = models["Random Forest"]

joblib.dump(
    best_model,
    "models/predictive_maintenance_model.pkl"
)

print("\n==========================================")
print("BEST MODEL SAVED SUCCESSFULLY")
print("Model: Random Forest")
print("File: models/predictive_maintenance_model.pkl")
print("==========================================")