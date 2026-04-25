from src.core.loader import load_data
from src.core.validator import validate
from src.report.generator import generate_report


def main():
    path = "data/raw/data.csv"  # cambia con il tuo file

    # 1. Load data
    df = load_data(path)

    # 2. Validate data
    results = validate(df)

    # 3. Generate report
    generate_report(results)


if __name__ == "__main__":
    main()
