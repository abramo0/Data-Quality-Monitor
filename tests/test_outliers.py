import pandas as pd
from src.metrics.outliers import OutlierChecker


def test_outlier_detection():
    df = pd.DataFrame({
        "salary": [10, 12, 11, 1000]
    })

    checker = OutlierChecker(df)
    result = checker.analyze()

    assert "salary" in result
    assert result["salary"]["outliers"] == 1
