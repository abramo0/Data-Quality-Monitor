import pandas as pd
from src.metrics.missing import MissingChecker


def test_missing_values():
    df = pd.DataFrame({
        "age": [10, None, 30]
    })

    checker = MissingChecker(df)
    result = checker.analyze()

    assert result["age"]["missing_count"] == 1
    assert result["age"]["missing_percentage"] > 0
