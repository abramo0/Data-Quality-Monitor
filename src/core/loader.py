import pandas as pd
from src.utils.logger import get_logger

logger = get_logger()


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load_csv(self):
        try:
            self.data = pd.read_csv(self.file_path)
            logger.info(f"Dataset loaded successfully with shape: {self.data.shape}")
            return self.data

        except Exception as e:
            logger.error(f"Failed to load dataset: {e}")
            return None
