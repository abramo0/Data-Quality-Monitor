class DriftDetector:
    def __init__(self, df):
        self.df = df

    def analyze(self):
        return {
            "rows": len(self.df),
            "columns": len(self.df.columns)
        }
