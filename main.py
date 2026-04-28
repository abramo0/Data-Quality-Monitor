from src.core.loader import DataLoader
from src.core.validator import validate
from src.report.generator import generate_report


def main():
    path = "data/raw/data.csv"

    # 1. Load data
    loader = DataLoader(path)
    df = loader.load_csv()

    # sicurezza
    if df is None:
        print("[ERROR] Data loading failed. Exiting...")
        return

    # 2. Validate data
    results = validate(df)

    # 3. Generate report
    generate_report(results)


if __name__ == "__main__":
    main()
