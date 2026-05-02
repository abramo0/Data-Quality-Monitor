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
    return parser.parse_args()


def main():
    args = parse_args()

    logger.info("Starting Data Quality Monitor...")

    # Load
    loader = DataLoader(args.file)
    df = loader.load_csv()

    if df is None:
        logger.error("Loading failed. Exiting...")
        return

    # Validate
    results = validate(df)

    # Score (QUI è la novità)
    score_engine = DataQualityScore(results)
    score = score_engine.compute()
    status = score_engine.status(score)

    # Report
    report = ReportGenerator(results)
    report.print_report()

    # Output finale
    print(f"\n⭐ FINAL SCORE: {score}/100")
    print(f"📊 STATUS: {status}")

    logger.info("Execution completed successfully")


if __name__ == "__main__":
    main()
