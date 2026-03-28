import os
import zipfile
from config import RAW_PATH, EXTRACTED_PATH

def extract_all():
    os.makedirs(EXTRACTED_PATH, exist_ok=True)

    for file in os.listdir(RAW_PATH):
        if file.endswith(".zip"):
            zip_path = os.path.join(RAW_PATH, file)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(EXTRACTED_PATH)
                print(f"✅ Extracted {file}")
