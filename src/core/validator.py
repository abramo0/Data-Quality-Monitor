from src.metrics.missing import MissingChecker
from src.metrics.outliers import OutlierChecker
from src.metrics.schema import SchemaChecker
from src.core.score import DataQualityScore


def validate(df):

    results = {}

    # --------------------
    # METRICS
    # --------------------
    missing_checker = MissingValuesChecker(df)
    results["missing"] = missing_checker.analyze()
    results["missing_summary"] = missing_checker.summary()

    outlier_checker = OutlierChecker(df)
    results["outliers"] = outlier_checker.analyze()

    schema_checker = SchemaChecker(df)
    results["schema"] = schema_checker.analyze()

    # --------------------
    # SCORE
    # --------------------
    scorer = DataQualityScore(results)
    score = scorer.compute()

    results["score"] = score
    results["final_status"] = scorer.status(score)

    return results
