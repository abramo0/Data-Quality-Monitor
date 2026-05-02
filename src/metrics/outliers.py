import pandas as pd


class OutlierChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        report = {}

        numeric_cols = self.df.select_dtypes(include=["number"]).columns

        for col in numeric_cols:
            series = self.df[col].dropna()

            if len(series) == 0:
                continue

            q1 = series.quantile(0.25)
            q3 = series.quantile(0.75)
            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            outliers = series[(series < lower) | (series > upper)]

            report[col] = {
                "outlier_count": int(len(outliers)),
                "outlier_percentage": round(len(outliers) / len(series) * 100, 2)
            }

        return report
