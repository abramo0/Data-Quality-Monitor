class ReportGenerator:
    def __init__(self, results):
        self.results = results

    def print_report(self):
        print("\n" + "=" * 60)
        print("📊 DATA QUALITY REPORT")
        print("=" * 60)

        # --------------------
        # MISSING
        # --------------------
        print("\n📌 MISSING VALUES")
        print("-" * 60)

        print(f"{'Column':<15}{'Missing':<10}{'Percentage':<15}{'Status'}")
        print("-" * 60)

        missing = self.results.get("missing", {})

        for col, val in missing.items():
            count = val.get("missing_count", 0)
            perc = val.get("missing_percentage", 0)
            status = "OK" if perc == 0 else "WARNING"

            print(f"{col:<15}{count:<10}{perc:<15}% {status}")

        m = self.results.get("missing_summary", {})
        print("\nTOTAL:", m.get("total_missing_values", 0), " | RATE:", m.get("missing_rate", 0), "%")

        # --------------------
        # OUTLIERS
        # --------------------
        print("\n📌 OUTLIERS")
        print("-" * 60)

        outliers = self.results.get("outliers", {})

        for col, val in outliers.items():
            count = val.get("outliers", 0)
            ratio = val.get("outlier_ratio", 0)
            status = val.get("status", "UNKNOWN")

            print(f"{col:<15}{count:<10}{ratio*100:.2f}% {status}")

        # --------------------
        # DRIFT
        # --------------------
        print("\n📌 DRIFT")
        print("-" * 60)

        drift = self.results.get("drift", {})

        for k, v in drift.items():
            print(f"{k}: {v}")

        # --------------------
        # SCHEMA
        # --------------------
        print("\n📌 SCHEMA")
        print("-" * 60)

        print(f"{'Column':<15}{'Type':<15}{'Numeric'}")

        schema = self.results.get("schema", {})

        for col, val in schema.items():
            dtype = val.get("dtype", "unknown")
            is_num = val.get("is_numeric", False)

            print(f"{col:<15}{dtype:<15}{is_num}")

        print("\n" + "=" * 60)
