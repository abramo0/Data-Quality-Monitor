from src.metrics.missing import MissingValuesChecker
from src.metrics.outliers import OutlierChecker
from src.metrics.schema import SchemaChecker
from src.core.drift import DriftDetector


def validate(df):
    results = {}

    # Missing
    missing = MissingValuesChecker(df)
    results["missing"] = missing.analyze()
    results["missing_summary"] = missing.summary()

    # Outliers
    outliers = OutlierChecker(df)
    results["outliers"] = outliers.analyze()

    # Schema
    schema = SchemaChecker(df)
    results["schema"] = schema.analyze()

    # Drift
    drift = DriftDetector(df)
    results["drift"] = drift.analyze()

    return results
