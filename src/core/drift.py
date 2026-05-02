class DriftDetector:
    def __init__(self, df):
        self.df = df

    def analyze(self):
        return {
            "columns": len(self.df.columns),
            "rows": len(self.df),
        }
