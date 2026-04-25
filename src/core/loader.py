import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"[INFO] Dataset loaded successfully: {path}")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}")
        raise
    except Exception as e:
        print(f"[ERROR] Failed to load dataset: {e}")
        raise
