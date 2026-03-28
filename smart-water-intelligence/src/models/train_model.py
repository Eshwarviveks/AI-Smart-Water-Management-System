import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from config import PROCESSED_DATA_PATH, MODEL_PATH

os.makedirs(MODEL_PATH, exist_ok=True)

df = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "water_stress.csv"))

X = df[["recharge", "extraction", "extraction_stage"]]
y = df["water_stress"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=300)
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(MODEL_PATH, "water_stress_model.pkl"))

print("✅ Model trained and saved")
