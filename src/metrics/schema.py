import pandas as pd


class SchemaChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        report = {}
        issues = 0

        for col in self.df.columns:

            series = self.df[col]

            dtype = str(series.dtype)
            is_numeric = pd.api.types.is_numeric_dtype(series)

            # --------------------------
            # QUALITY RULES (basic)
            # --------------------------
            status = "OK"

            # column completely empty
            if series.isnull().all():
                status = "BAD"
                issues += 1

            # mixed / unexpected types (heuristic)
            elif series.dtype == "object":
                # try detect numeric-like strings
                numeric_like = pd.to_numeric(series, errors="coerce").notnull().mean()

                if numeric_like > 0.8:
                    status = "WARNING"
                    issues += 1

            report[col] = {
                "dtype": dtype,
                "is_numeric": is_numeric,
                "status": status
            }

        return {
            "columns": report,
            "issues": issues,
            "total_columns": len(self.df.columns)
        }
