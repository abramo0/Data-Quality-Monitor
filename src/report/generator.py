def generate_report(results):
    print("\n=== DATA QUALITY REPORT ===\n")

    # Missing values
    print("Missing Values:")
    for col, val in results["missing"].items():
        status = "OK" if val == 0 else "WARNING"
        print(f" - {col}: {val*100}% [{status}]")

    print("\n===========================\n")
