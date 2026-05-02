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

            total = len(series)
            outlier_count = len(outliers)
            outlier_ratio = outlier_count / total if total > 0 else 0

            report[col] = {
                "check": "outliers",
                "column": col,
                "status": "PASS" if outlier_ratio == 0 else "WARN",
                "total_values": total,
                "outliers": outlier_count,
                "outlier_ratio": round(outlier_ratio, 4),
                "lower_bound": lower,
                "upper_bound": upper
            }

        return report
