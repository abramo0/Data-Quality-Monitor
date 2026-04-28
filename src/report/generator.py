def generate_report(results):
    print("\n=== DATA QUALITY REPORT ===\n")

    # Missing values
    print("Missing Values:")
    for col, val in results["missing"].items():
        percentage = val["missing_percentage"]
        status = "OK" if percentage == 0 else "WARNING"

        print(f" - {col}: {percentage}% [{status}]")

    print("\n===========================\n")def generate_report(results):
    print("\n=== DATA QUALITY REPORT ===\n")

    # Missing values
    print("Missing Values:")
    for col, val in results["missing"].items():
        status = "OK" if val == 0 else "WARNING"
        print(f" - {col}: {val*100}% [{status}]")

    print("\n===========================\n")
