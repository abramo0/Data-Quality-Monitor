import pandas as pd


class MissingValuesChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df            # Input dataset to be analyzed

    def analyze(self):
        """
        Computes missing values statistics for each column.

        Returns:
            dict: A dictionary containing missing value count and percentage per column.
        """

        missing_count = self.df.isnull().sum()            # Count missing values per column
        missing_percentage = (missing_count / len(self.df)) * 100            # Compute missing value percentage per column
        report = {}            # Dictionary to store per-column results

        # Build structured report for each column
        for column in self.df.columns:
            report[column] = {
                "missing_count": int(missing_count[column]),
                "missing_percentage": round(missing_percentage[column], 2)
            }

        return report

    def summary(self):
        """
        Computes overall missing values statistics for the entire dataset.

        Returns:
            dict: Total missing values and overall missing rate.
        """

        total_missing = self.df.isnull().sum().sum()            # Total number of missing values in the dataset
        total_cells = self.df.shape[0] * self.df.shape[1]            # Total number of cells in the dataset
        missing_rate = (total_missing / total_cells) * 100 if total_cells > 0 else 0            # Overall missing rate
        
        return {
            "total_missing_values": int(total_missing),
            "missing_rate": round(missing_rate, 2)
        }
