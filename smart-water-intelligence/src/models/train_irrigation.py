import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from config import PROCESSED_DATA_PATH, MODEL_PATH

os.makedirs(MODEL_PATH, exist_ok=True)

df = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "irrigation_data.csv"))

# Create encoders
crop_encoder = LabelEncoder()
irrigation_encoder = LabelEncoder()

df["crop"] = crop_encoder.fit_transform(df["crop"])
df["irrigation_type"] = irrigation_encoder.fit_transform(df["irrigation_type"])

X = df[["crop", "water_use", "irrigation_type"]]
y = df["inefficiency"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# Save everything
joblib.dump(model, os.path.join(MODEL_PATH, "irrigation_model.pkl"))
joblib.dump(crop_encoder, os.path.join(MODEL_PATH, "crop_encoder.pkl"))
joblib.dump(irrigation_encoder, os.path.join(MODEL_PATH, "irrigation_encoder.pkl"))

print("✅ Irrigation model trained and encoders saved")
