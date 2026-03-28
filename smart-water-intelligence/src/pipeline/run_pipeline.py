import os
from config import PROCESSED_DATA_PATH
from src.pipeline.extract import extract_all
from src.pipeline.transform import (
    build_water_stress_dataset,
    build_irrigation_dataset
)

def run():
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    extract_all()

    water_df = build_water_stress_dataset()
    water_df.to_csv(
        os.path.join(PROCESSED_DATA_PATH, "water_stress.csv"),
        index=False
    )

    irrigation_df = build_irrigation_dataset()
    irrigation_df.to_csv(
        os.path.join(PROCESSED_DATA_PATH, "irrigation_data.csv"),
        index=False
    )

    print("✅ Full pipeline completed successfully")

if __name__ == "__main__":
    run()
