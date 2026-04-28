import pandas as pd


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path    # Path to the input CSV file
        self.data = None        # Placeholder for the loaded dataset

    def load_csv(self):
        """
        Loads a CSV file into a Pandas DataFrame.

        Returns:
            pd.DataFrame: Loaded dataset if successful.
            None: If loading fails.
        """
        try:
            self.data = pd.read_csv(self.file_path)                # Read CSV file into a Pandas DataFrame
            print(f"[INFO] Dataset loaded successfully with shape: {self.data.shape}")                # Log dataset shape (rows, columns)
            return self.data

        except Exception as e:
            print(f"[ERROR] Failed to load dataset: {e}")    # Handle any error occurring during file loading
            return None
