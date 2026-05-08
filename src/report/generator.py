import json


class ReportGenerator:
    def __init__(self, results):
        self.results = results

    def print_report(self):
        print("\n" + "=" * 60)
        print("📊 DATA QUALITY REPORT")
        print("=" * 60)

        # --------------------
        # MISSING VALUES
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

            print(f"{col:<15}{count:<10}{str(perc) + '%':<15}{status}")

        summary = self.results.get("missing_summary", {})

        print("-" * 60)
        print(f"TOTAL MISSING VALUES: {summary.get('total_missing_values', 0)}")
        print(f"OVERALL MISSING RATE: {summary.get('missing_rate', 0)}%")

        # --------------------
        # OUTLIERS
        # --------------------
        print("\n📌 OUTLIERS")
        print("-" * 60)

        print(f"{'Column':<15}{'Outliers':<12}{'Ratio':<12}{'Status'}")
        print("-" * 60)

        outliers = self.results.get("outliers", {})

        for col, val in outliers.items():
            count = val.get("outliers", 0)
            ratio = val.get("outlier_ratio", 0)
            status = val.get("status", "UNKNOWN")

            print(f"{col:<15}{count:<12}{ratio*100:.2f}%{'':<6}{status}")

        # --------------------
        # SCHEMA
        # --------------------
        print("\n📌 SCHEMA")
        print("-" * 60)

        print(f"{'Column':<15}{'Type':<15}{'Numeric'}")
        print("-" * 60)

        schema = self.results.get("schema", {})

        for col, val in schema.items():
            dtype = val.get("dtype", "unknown")
            is_numeric = val.get("is_numeric", False)

            print(f"{col:<15}{dtype:<15}{is_numeric}")

        # --------------------
        # DRIFT
        # --------------------
        print("\n📌 DRIFT")
        print("-" * 60)

        drift = self.results.get("drift", {})

        for key, value in drift.items():
            print(f"{key}: {value}")

        # --------------------
        # FINAL SCORE
        # --------------------
        score = self.results.get("final_score", "N/A")
        status = self.results.get("final_status", "UNKNOWN")

        print("\n" + "=" * 60)
        print(f"⭐ FINAL SCORE: {score}/100")
        print(f"📊 STATUS: {status}")
        print("=" * 60)

    def export_json(self, output_path):
        try:
            with open(output_path, "w") as f:
                json.dump(self.results, f, indent=4)

            print(f"\n✅ JSON report exported to: {output_path}")

        except Exception as e:
            print(f"\n❌ Failed to export JSON report: {e}")
