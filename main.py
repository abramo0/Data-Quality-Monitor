import argparse

from src.core.loader import DataLoader
from src.core.validator import validate
from src.core.score import DataQualityScore

from src.report.generator import ReportGenerator
from src.report.html_generator import HTMLReportGenerator


def parse_args():
    parser = argparse.ArgumentParser(description="Data Quality Monitor")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the CSV file"
    )

    parser.add_argument(
        "--export",
        required=False,
        help="Export JSON report path (e.g. report.json)"
    )

    parser.add_argument(
        "--html",
        required=False,
        help="Export HTML report path (e.g. report.html)"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    # 1. LOAD DATA
    loader = DataLoader(args.file)
    df = loader.load_csv()

    if df is None:
        print("[ERROR] Failed to load dataset.")
        return

    # 2. VALIDATION
    results = validate(df)

    # 3. SCORE
    score_engine = DataQualityScore(results)
    score = score_engine.compute()
    status = score_engine.status(score)

    results["final_score"] = score
    results["final_status"] = status

    # 4. TERMINAL REPORT
    report = ReportGenerator(results)
    report.print_report()

    # 5. JSON EXPORT (optional)
    if args.export:
        report.export_json(args.export)

    # 6. HTML EXPORT (optional)
    if args.html:
        html_report = HTMLReportGenerator(results)
        html_report.generate(args.html)

    print("\n[INFO] Process completed successfully.")


if __name__ == "__main__":
    main()
