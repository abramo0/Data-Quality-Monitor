import pandas as pd
from src.utils.logger import get_logger

logger = get_logger()


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load_csv(self):
        try:
            self.data = pd.read_csv(
                self.file_path,
                skipinitialspace=True  # 🔥 FIX SPAZI COLONNE
            )

            # 🔥 NORMALIZZAZIONE COLONNE
            self.data.columns = self.data.columns.str.strip()

            # 🔥 LOG INFO
            logger.info(
                f"Dataset loaded successfully | shape={self.data.shape} | columns={list(self.data.columns)}"
            )

            return self.data

        except FileNotFoundError:
            logger.error(f"File not found: {self.file_path}")
            return None

        except pd.errors.EmptyDataError:
            logger.error("CSV file is empty")
            return None

        except pd.errors.ParserError:
            logger.error("Error parsing CSV file (check delimiter)")
            return None

        except Exception as e:
            logger.error(f"Unexpected error loading dataset: {e}")
            return None
