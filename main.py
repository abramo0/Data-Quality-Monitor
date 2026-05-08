import argparse
from src.utils.logger import get_logger

from src.core.loader import DataLoader
from src.core.validator import validate
from src.core.score import DataQualityScore
from src.report.generator import ReportGenerator

logger = get_logger()


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file", required=True)

    parser.add_argument(
        "--export",
        required=False,
        help="Export report to JSON file"
    )

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

    # SCORE
    score_engine = DataQualityScore(results)
    score = score_engine.compute()
    status = score_engine.status(score)

    results["final_score"] = score
    results["final_status"] = status

    # REPORT
    report = ReportGenerator(results)
    report.print_report()

    # EXPORT JSON
    if args.export:
        report.export_json(args.export)
        logger.info(f"Report exported to {args.export}")

    logger.info("Execution completed successfully")


if __name__ == "__main__":
    main()
