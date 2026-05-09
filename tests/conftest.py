import pytest
import pandas as pd


@pytest.fixture
def clean_dataset():
    return pd.read_csv("tests/data/clean/clean_dataset.csv")
