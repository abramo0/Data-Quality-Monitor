import pandas as pd


class SchemaChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        report = {}

        for col in self.df.columns:

            series = self.df[col]

            # --------------------------
            # Base metadata
            # --------------------------

            dtype = str(series.dtype)

            is_numeric = pd.api.types.is_numeric_dtype(series)

            status = "OK"

            # --------------------------
            # Rule 1:
            # Fully empty column
            # --------------------------

            if series.isnull().all():

                status = "BAD"

            # --------------------------
            # Rule 2:
            # Numeric-like object column
            # Example:
            # ["1", "2", "3"]
            # --------------------------

            elif dtype == "object":

                numeric_like_ratio = (
                    pd.to_numeric(
                        series,
                        errors="coerce"
                    )
                    .notnull()
                    .mean()
                )

                if numeric_like_ratio > 0.8:

                    status = "WARNING"

            # --------------------------
            # Store results
            # --------------------------

            report[col] = {
                "dtype": dtype,
                "is_numeric": is_numeric,
                "status": status
            }

        return report
