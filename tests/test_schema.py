import pandas as pd
from src.metrics.schema import SchemaChecker


def test_schema_detection():
    df = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [20, 30]
    })

    checker = SchemaChecker(df)
    result = checker.analyze()

    assert result["name"]["is_numeric"] is False
    assert result["age"]["is_numeric"] is True
