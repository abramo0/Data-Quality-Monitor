def generate_report(results):
    print("\n=== DATA QUALITY REPORT ===\n")

    print("Missing Values:")
    for col, val in results["missing"].items():

        percentage = val["missing_percentage"]
        status = "OK" if percentage == 0 else "WARNING"

        print(f" - {col}: {percentage}% [{status}]")

    print("\n===========================\n")
