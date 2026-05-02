import pandas as pd


class SchemaChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self):
        report = {}

        for col in self.df.columns:
            dtype = str(self.df[col].dtype)

            report[col] = {
                "dtype": dtype,
                "is_numeric": pd.api.types.is_numeric_dtype(self.df[col])
            }

        return report
