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
    main()
