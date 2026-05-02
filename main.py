import argparse

from src.core.loader import DataLoader
from src.core.validator import validate
from src.report.generator import ReportGenerator


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    loader = DataLoader(args.file)
    df = loader.load_csv()

    if df is None:
        print("[ERROR] Loading failed")
        return

    results = validate(df)

    report = ReportGenerator(results)
    report.print_report()


if __name__ == "__main__":
    main()import argparse

from src.core.loader import DataLoader
from src.core.engine import run_checks
from src.config.loader import load_config
from src.report.generator import ReportGenerator


def parse_args():
    parser = argparse.ArgumentParser(description="Data Quality Monitor")
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the CSV file"
    )
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to YAML/JSON config file"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # 1. Load data
    loader = DataLoader(args.file)
    df = loader.load_data()

    if df is None:
        print("[ERROR] Data loading failed. Exiting...")
        return

    # 2. Load config (NEW)
    config = load_config(args.config)

    # 3. Run DQ engine (NEW CORE CHANGE)
    results = run_checks(df, config)

    # 4. Generate report
    report = ReportGenerator(results)
    report.print_report()


if __name__ == "__main__":
    main()
