from src.metrics.missing import MissingValuesChecker

def validate(df):
    results = {}

    # Missing values
    missing_checker = MissingValuesChecker(df)
    results["missing"] = missing_checker.analyze()
    results["missing_summary"] = missing_checker.summary()

    return results
