import pandas as pd
import os
from config import EXTRACTED_PATH

def load_csv(filename):
    path = os.path.join(EXTRACTED_PATH, filename)
    df = pd.read_csv(path, encoding="latin1")
    df.columns = df.columns.str.lower().str.strip()
    df = df.dropna()
    return df
