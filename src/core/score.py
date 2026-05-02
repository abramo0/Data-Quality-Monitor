class DataQualityScore:
    def __init__(self, results):
        self.results = results

    def compute(self):
        score = 100

        # --------------------
        # Missing penalty
        # --------------------
        missing_rate = self.results.get("missing_summary", {}).get("missing_rate", 0)
        score -= missing_rate * 0.5

        # --------------------
        # Outliers penalty
        # --------------------
        outliers = self.results.get("outliers", {})

        for col, val in outliers.items():
            ratio = val.get("outlier_ratio", 0)
            score -= ratio * 100 * 0.3   # convert to %

        # clamp
        score = max(0, round(score, 2))

        return score

    def status(self, score):
        if score >= 85:
            return "GOOD"
        elif score >= 60:
            return "WARNING"
        else:
            return "BAD"
