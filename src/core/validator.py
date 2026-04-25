from src.metrics.missing import check_missing

def validate(df):
    results = {}

    # Missing values
    results["missing"] = check_missing(df)

    return results
