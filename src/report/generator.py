class ReportGenerator:
    def __init__(self, results):
        self.results = results

    def print_report(self):
        print("\n" + "=" * 60)
        print("📊 DATA QUALITY REPORT")
        print("=" * 60)

        print("\n📌 MISSING VALUES\n" + "-" * 60)
        print(f"{'Column':<15}{'Missing':<10}{'Percentage':<15}{'Status'}")
        print("-" * 60)

        for col, val in self.results["missing"].items():
            count = val["missing_count"]
            perc = val["missing_percentage"]

            status = "OK" if perc == 0 else "WARNING"

            print(f"{col:<15}{count:<10}{perc:<15}% {status}")

        summary = self.results["missing_summary"]

        print("\n" + "-" * 60)
        print(f"TOTAL MISSING VALUES: {summary['total_missing_values']}")
        print(f"OVERALL MISSING RATE: {summary['missing_rate']}%")
        print("=" * 60 + "\n")
