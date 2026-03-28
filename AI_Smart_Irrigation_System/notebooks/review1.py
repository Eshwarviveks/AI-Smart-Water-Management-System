# =====================================================
# REVIEW 1 – DATA ENGINEERING, EDA & FEATURE ENGINEERING
# AI-Based Smart Irrigation System
# =====================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import StandardScaler, LabelEncoder # type: ignore

# SAFE PATH HANDLING
# -----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data", "raw")

# -----------------------------------------------------
# LOAD ALL DATASETS (AS PER YOUR FOLDER)
# -----------------------------------------------------
df_irrigation = pd.read_csv(os.path.join(DATA_DIR, "AutoIrrigationData.csv"))
df_demo = pd.read_csv(os.path.join(DATA_DIR, "demo1.csv"))
df_days = pd.read_csv(os.path.join(DATA_DIR, "moisture_days.csv"))
df_time = pd.read_csv(os.path.join(DATA_DIR, "moisture_time.csv"))
df_soil = pd.read_csv(os.path.join(DATA_DIR, "soil-moisture.csv"))

print("\nALL DATASETS LOADED SUCCESSFULLY\n")

# 3. DATA ENGINEERING & DATASET OVERVIEW

print("----- MAIN IRRIGATION DATASET (data.csv) -----")
print(df_irrigation.info(), "\n")

print("----- DEMO DATASET (demo1.csv) -----")
print(df_demo.info(), "\n")

print("----- MOISTURE vs DAYS -----")
print(df_days.info(), "\n")

print("----- MOISTURE vs TIME -----")
print(df_time.info(), "\n")

print("----- SOIL MOISTURE DATASET -----")
print(df_soil.info(), "\n")

# 3.6 DATA QUALITY ASSESSMENT

print("Missing Values – Irrigation Dataset")
print(df_irrigation.isnull().sum(), "\n")

# Handle missing values (safe method)
df_irrigation.ffill(inplace=True)


# 4. EXPLORATORY DATA ANALYSIS (EDA)

# 4.1 Statistical Summary
print("Statistical Summary – Irrigation Dataset")
print(df_irrigation.describe(), "\n")

# 4.2 Distribution Plot (Moisture)
plt.hist(df_irrigation["moisture"], bins=20)
plt.title("Moisture Distribution")
plt.xlabel("Moisture")
plt.ylabel("Frequency")
plt.show()

# 4.3 Feature Correlation (NUMERIC ONLY)
print("Feature Correlation (Numeric Columns Only)")
print(df_irrigation.select_dtypes(include="number").corr(), "\n")


# TIME-SERIES VISUALIZATION

plt.plot(df_days["days"], df_days["moisture"])
plt.title("Soil Moisture vs Days")
plt.xlabel("Days")
plt.ylabel("Moisture")
plt.show()

plt.plot(df_time["time"], df_time["Moisture"])
plt.title("Soil Moisture vs Time")
plt.xlabel("Time")
plt.ylabel("Moisture")
plt.show()

# =====================================================
# 5. FEATURE ENGINEERING
# =====================================================

# Encode categorical feature: crop
encoder = LabelEncoder()
df_irrigation["crop_encoded"] = encoder.fit_transform(df_irrigation["crop"])

# Feature set and target
X = df_irrigation[["crop_encoded", "moisture", "temp"]]
y = df_irrigation["pump"]   # TARGET (Irrigation ON/OFF)

# Train–Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Feature Engineering Completed Successfully")
print("X_train shape:", X_train_scaled.shape)
print("X_test shape:", X_test_scaled.shape)

print("\nREVIEW 1 EXECUTION COMPLETED SUCCESSFULLY")
