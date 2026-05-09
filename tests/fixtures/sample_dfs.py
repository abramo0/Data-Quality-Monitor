import pandas as pd


def clean_df():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["A", "B", "C"],
        "age": [20, 30, 40]
    })


def missing_df():
    return pd.DataFrame({
        "name": ["A", None, "C"],
        "age": [20, None, 40]
    })


def outlier_df():
    return pd.DataFrame({
        "value": [10, 12, 11, 1000]
    })
