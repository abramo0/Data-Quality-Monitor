import jason

class ReportGenerator:
    def __init__(self, results):
        self.results = results

    def print_report(self):
        print("\n" + "=" * 60)
        print("📊 DATA QUALITY REPORT")
        print("=" * 60)

        # --------------------------
        # MISSING VALUES
        # --------------------------
        print("\n📌 MISSING VALUES")
        print("-" * 60)

        print(f"{'Column':<15}{'Missing':<10}{'Percentage':<15}{'Status'}")
        print("-" * 60)

        for col, val in self.results.get("missing", {}).items():
            count = val.get("missing_count", 0)
            perc = val.get("missing_percentage", 0.0)
            status = "OK" if perc == 0 else "WARNING"

            print(f"{col:<15}{count:<10}{perc:<15}% {status}")

        m = self.results.get("missing_summary", {})
        print("\nTOTAL:", m.get("total_missing_values", 0),
              " | RATE:", m.get("missing_rate", 0), "%")

        # --------------------------
        # OUTLIERS
        # --------------------------
        print("\n📌 OUTLIERS")
        print("-" * 60)

        outliers = self.results.get("outliers", {})

        for col, val in outliers.items():
            status = val.get("status", "UNKNOWN")
            count = val.get("outliers", 0)
            ratio = val.get("outlier_ratio", 0) * 100

            print(f"{col:<15}{count:<10}{ratio:.2f}% {status}")

        # --------------------------
        # SCHEMA
        # --------------------------
        print("\n📌 SCHEMA")
        print("-" * 60)
        print(f"{'Column':<15}{'Type':<15}{'Numeric':<10}{'Status'}")
        print("-" * 60)

        schema = self.results.get("schema", {}).get("columns", {})

        for col, val in schema.items():
            dtype = val.get("dtype", "unknown")
            is_numeric = val.get("is_numeric", False)
            status = val.get("status", "OK")

            print(f"{col:<15}{dtype:<15}{str(is_numeric):<10}{status}")

        # --------------------------
        # DRIFT
        # --------------------------
        print("\n📌 DRIFT")
        print("-" * 60)

        drift = self.results.get("drift", {})

        for k, v in drift.items():
            print(f"{k}: {v}")

        # --------------------------
        # SCORE
        # --------------------------
        print("\n📌 FINAL SCORE")
        print("-" * 60)

        score = self.results.get("final_score", 0)
        status = self.results.get("final_status", "UNKNOWN")

        print(f"SCORE: {score}")
        print(f"STATUS: {status}")

        print("\n" + "=" * 60)
