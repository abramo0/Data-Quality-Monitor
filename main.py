import argparse

from src.core.loader import DataLoader
from src.core.validator import validate
from src.report.generator import ReportGenerator


def parse_args():
    parser = argparse.ArgumentParser(description="Data Quality Monitor")
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the CSV file"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    path = args.file

    # 1. Load data
    loader = DataLoader(path)
    df = loader.load_csv()

    if df is None:
        print("[ERROR] Data loading failed. Exiting...")
        return

    # 2. Validate data
    results = validate(df)

    # 3. Generate report
    generate_report(results)


if __name__ == "__main__":
    main()
