import pandas as pd


class OutlierCheck:
    def __init__(self, column: str, factor: float = 1.5):
        """
        Args:
            column (str): column to analyze
            factor (float): IQR multiplier (default 1.5)
        """
        self.column = column
        self.factor = factor

    def run(self, df: pd.DataFrame):
        """
        Returns:
            dict: result of outlier detection
        """

        if self.column not in df.columns:
            return {
                "check": "outliers",
                "column": self.column,
                "status": "FAIL",
                "reason": "column not found"
            }

        series = df[self.column].dropna()

        # ensure numeric (important for robustness)
        if not pd.api.types.is_numeric_dtype(series):
            return {
                "check": "outliers",
                "column": self.column,
                "status": "FAIL",
                "reason": "column is not numeric"
            }

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - self.factor * iqr
        upper_bound = q3 + self.factor * iqr

        outliers = series[(series < lower_bound) | (series > upper_bound)]

        total = len(series)
        outlier_count = len(outliers)
        outlier_ratio = outlier_count / total if total > 0 else 0

        return {
            "check": "outliers",
            "column": self.column,
            "status": "PASS" if outlier_ratio == 0 else "WARN",
            "total_values": total,
            "outliers": outlier_count,
            "outlier_ratio": round(outlier_ratio, 4),
            "lower_bound": lower_bound,
            "upper_bound": upper_bound
        }
