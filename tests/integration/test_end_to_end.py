import pandas as pd
from src.core.validator import validate


def test_end_to_end_clean_dataset():
    df = pd.read_csv("tests/data/clean/clean_dataset.csv")

    result = validate(df)

    assert result["final_status"] in ["GOOD", "OK"]
    assert 90 <= result["final_score"] <= 100
