import pandas as pd
from src.core.loader import DataLoader


def test_load_csv_success(tmp_path):
    file = tmp_path / "test.csv"

    file.write_text("name,age\nAlice,20\nBob,30")

    loader = DataLoader(str(file))
    df = loader.load_csv()

    assert df is not None
    assert df.shape == (2, 2)
    assert list(df.columns) == ["name", "age"]
