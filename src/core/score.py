class DataQualityScore:
    def __init__(self, results):
        self.results = results

    def compute(self):
        score = 100

        missing_rate = self.results.get("missing_summary", {}).get("missing_rate", 0)
        score -= missing_rate * 0.5

        outliers = self.results.get("outliers", {})

        for col, val in outliers.items():
            ratio = val.get("outlier_ratio", 0)
            score -= ratio * 100 * 0.3

        return max(0, round(score, 2))

    def status(self, score):
        if score >= 85:
            return "GOOD"
        elif score >= 60:
            return "WARNING"
        else:
            return "BAD"


# 👇 WRAPPER per compatibilità test
def compute_score(missing=0, outliers=0, schema_issues=0):
    score = 100
    score -= missing * 0.5
    score -= outliers * 0.3
    score -= schema_issues * 5

    return max(0, min(100, round(score, 2)))
