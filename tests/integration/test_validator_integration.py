import pandas as pd
from src.core.validator import validate


def test_validator_pipeline_runs():
    df = pd.read_csv("tests/data/clean/clean_dataset.csv")

    result = validate(df)

    assert "missing" in result
    assert "outliers" in result
    assert "schema" in result
