import argparse
from src.utils.logger import get_logger

from src.core.loader import DataLoader
from src.core.validator import validate
from src.report.generator import ReportGenerator
from src.core.score import DataQualityScore

logger = get_logger()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    logger.info("Starting Data Quality Monitor...")

    loader = DataLoader(args.file)
    df = loader.load_csv()

    if df is None:
        logger.error("Loading failed. Exiting...")
        return

    results = validate(df)

    report = ReportGenerator(results)
    report.print_report()

    logger.info("Execution completed successfully")


if __name__ == "__main__":
    main()
