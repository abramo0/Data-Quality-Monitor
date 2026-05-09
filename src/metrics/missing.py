import pandas as pd


class MissingChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        missing_count = self.df.isnull().sum()
        missing_percentage = (missing_count / len(self.df)) * 100

        report = {}

        for col in self.df.columns:
            report[col] = {
                "missing_count": int(missing_count[col]),
                "missing_percentage": round(missing_percentage[col], 2)
            }

        return report

    def summary(self):
        total_missing = self.df.isnull().sum().sum()
        total_cells = self.df.shape[0] * self.df.shape[1]

        missing_rate = (total_missing / total_cells) * 100 if total_cells > 0 else 0

        return {
            "total_missing_values": int(total_missing),
            "missing_rate": round(missing_rate, 2)
        }
