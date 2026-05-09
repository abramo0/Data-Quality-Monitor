import pandas as pd
from src.core.validator import validate


def test_validation_pipeline():
    df = pd.DataFrame({
        "name": ["Alice", None, "Bob"],
        "salary": [10, 12, 1000]
    })

    results = validate(df)

    assert "missing" in results
    assert "outliers" in results
    assert "schema" in results
    assert "final_score" in results
