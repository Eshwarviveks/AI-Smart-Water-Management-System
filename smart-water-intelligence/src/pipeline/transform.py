from src.pipeline.clean import load_csv

def build_water_stress_dataset():
    df = load_csv("Dynamic_2017_2_0.csv")

    df = df.rename(columns={
        "name of district": "district",
        "total annual ground water recharge": "recharge",
        "total current annual ground water extraction": "extraction",
        "stage of ground water extraction (%)": "extraction_stage"
    })

    df = df[["district", "recharge", "extraction", "extraction_stage"]]

    df["water_stress"] = df["extraction_stage"].apply(
        lambda x: "High" if x > 100 else (
                  "Medium" if x > 70 else "Low")
    )

    return df


def build_irrigation_dataset():
    df = load_csv("agricultural_water_footprint.csv")

    # Normalize all column names safely
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("(", "")
        .str.replace(")", "")
        .str.replace("%", "")
        .str.replace("/", "_")
    )

    print("Normalized columns:")
    print(df.columns.tolist())

    # Now manually map correct columns
    df = df.rename(columns={
        "water_use_mâ³_kg": "water_use",
        "irrigation_type": "irrigation_type",
        "irrigation_efficiency_": "efficiency"
    })

    # Select required columns
    df = df[["crop", "water_use", "irrigation_type", "efficiency"]]

    # Create inefficiency label
    df["inefficiency"] = df["efficiency"].apply(
        lambda x: "Inefficient" if x < 60 else "Efficient"
    )

    return df
