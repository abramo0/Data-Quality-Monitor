import pandas as pd
from src.utils.config import load_config


class MissingChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        config = load_config()

        threshold = config["missing_threshold"]

        missing_count = self.df.isnull().sum()
        missing_percentage = (missing_count / len(self.df)) * 100

        report = {}

        for column in self.df.columns:

            percentage = round(missing_percentage[column], 2)

            status = (
                "OK"
                if percentage <= threshold
                else "WARNING"
            )

            report[column] = {
                "missing_count": int(missing_count[column]),
                "missing_percentage": percentage,
                "status": status
            }

        return report

    def summary(self):
        total_missing = self.df.isnull().sum().sum()

        total_cells = self.df.shape[0] * self.df.shape[1]

        missing_rate = (
            (total_missing / total_cells) * 100
            if total_cells > 0 else 0
        )

        return {
            "total_missing_values": int(total_missing),
            "missing_rate": round(missing_rate, 2)
        }
