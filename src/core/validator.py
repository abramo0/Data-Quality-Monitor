from src.metrics.missing import MissingValuesChecker
from src.metrics.outliers import OutlierCheck
from src.core.drift import DriftDetector


def validate(df):
    results = {}

    # Missing
    missing = MissingValuesChecker(df)
    results["missing"] = missing.analyze()
    results["missing_summary"] = missing.summary()

    # Outliers (multi-column fix)
    outlier_results = {}

    for col in df.select_dtypes(include="number").columns:
        checker = OutlierCheck(col)
        outlier_results[col] = checker.run(df)

    results["outliers"] = outlier_results

    # Drift
    drift = DriftDetector(df)
    results["drift"] = drift.analyze()

    return results
