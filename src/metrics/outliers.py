import pandas as pd

from src.utils.config_py import load_config


class OutlierChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        config = load_config()

        iqr_multiplier = config["outlier"]["iqr_multiplier"]
        warning_ratio = config["outlier"]["warning_ratio"]

        report = {}

        numeric_cols = self.df.select_dtypes(include=["number"]).columns

        for col in numeric_cols:

            series = self.df[col].dropna()

            if len(series) == 0:
                continue

            # --------------------------
            # IQR computation
            # --------------------------

            q1 = series.quantile(0.25)
            q3 = series.quantile(0.75)

            iqr = q3 - q1

            lower = q1 - (iqr_multiplier * iqr)
            upper = q3 + (iqr_multiplier * iqr)

            # --------------------------
            # Detect outliers
            # --------------------------

            outliers = series[
                (series < lower) |
                (series > upper)
            ]

            total = len(series)

            outlier_count = len(outliers)

            outlier_ratio = (
                outlier_count / total
                if total > 0 else 0
            )

            # --------------------------
            # Status
            # --------------------------

            status = (
                "PASS"
                if (outlier_ratio * 100) <= warning_ratio
                else "WARN"
            )

            # --------------------------
            # Report
            # --------------------------

            report[col] = {
                "check": "outliers",
                "column": col,
                "status": status,
                "total_values": total,
                "outliers": outlier_count,
                "outlier_ratio": round(outlier_ratio, 4),
                "lower_bound": round(lower, 2),
                "upper_bound": round(upper, 2)
            }

        return report
