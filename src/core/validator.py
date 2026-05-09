from src.metrics.missing import MissingChecker
from src.metrics.schema import SchemaChecker
from src.metrics.outliers import OutlierChecker
from src.core.drift import DriftDetector


def validate(df):
    """
    Central validation pipeline.
    Returns a unified results dictionary (data contract).
    """

    results = {
        "missing": {},
        "outliers": {},
        "schema": {},
        "drift": {},
        "final_score": None,
        "final_status": None
    }

    # --------------------------
    # 1. MISSING VALUES
    # --------------------------
    missing_checker = MissingChecker(df)
    results["missing"] = missing_checker.analyze()
    results["missing_summary"] = missing_checker.summary()

    # --------------------------
    # OUTLIERS
    # --------------------------
    outlier_checker = OutlierChecker(df)
    results["outliers"] = outlier_checker.analyze()
    
    for col in df.select_dtypes(include=["number"]).columns:
        checker = OutlierChecker(df)
        results["outliers"] = checker.analyze()
    # --------------------------
    # 3. SCHEMA VALIDATION
    # --------------------------
    schema_checker = SchemaChecker(df)
    results["schema"] = schema_checker.analyze()

    # --------------------------
    # 4. DRIFT (basic version)
    # --------------------------
    drift_detector = DriftDetector(df)
    results["drift"] = drift_detector.analyze()

    return results
