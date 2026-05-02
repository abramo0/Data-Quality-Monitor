class ReportGenerator:
    def __init__(self, results):
        self.results = results

    def print_report(self):
        print("\n" + "=" * 60)
        print("📊 DATA QUALITY REPORT")
        print("=" * 60)

        # MISSING
        print("\n📌 MISSING VALUES")
        print("-" * 60)

        print(f"{'Column':<15}{'Missing':<10}{'Percentage':<15}{'Status'}")
        print("-" * 60)

        for col, val in self.results["missing"].items():
            status = "OK" if val["missing_percentage"] == 0 else "WARNING"
            print(f"{col:<15}{val['missing_count']:<10}{val['missing_percentage']:<15}% {status}")

        m = self.results["missing_summary"]
        print("\nTOTAL:", m["total_missing_values"], " | RATE:", m["missing_rate"], "%")

        # OUTLIERS
        print("\n📌 OUTLIERS")
        print("-" * 60)

        for col, val in self.results["outliers"].items():
            status = val["status"]
            print(f"{col:<15}{val['outliers']:<10}{val['outlier_ratio']*100:.2f}% {status}")

        # DRIFT
        print("\n📌 DRIFT")
        print("-" * 60)

        for k, v in self.results["drift"].items():
            print(f"{k}: {v}")

        print("\n" + "=" * 60)

        # SCHEMA
        print("\n📌 SCHEMA\n" + "-" * 60)
        print(f"{'Column':<15}{'Type':<15}{'Numeric'}")
        print("-" * 60)
        
        for col, val in self.results["schema"].items():
            print(f"{col:<15}{val['dtype']:<15}{val['is_numeric']}")
