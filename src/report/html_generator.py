import os


class HTMLReportGenerator:
    def __init__(self, results):
        self.results = results

    def generate(self, output_path="report.html"):
        html = f"""
        <html>
        <head>
            <title>Data Quality Report</title>
            <style>
                body {{
                    font-family: Arial;
                    margin: 40px;
                    background-color: #f5f5f5;
                }}
                .card {{
                    background: white;
                    padding: 20px;
                    margin-bottom: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
                }}
                .good {{ color: green; }}
                .warning {{ color: orange; }}
                .bad {{ color: red; }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #eee;
                }}
            </style>
        </head>
        <body>

        <h1>📊 Data Quality Report</h1>

        <div class="card">
            <h2>⭐ Score</h2>
            <h3>{self.results.get("final_score", "N/A")} / 100</h3>
            <h3 class="{self.results.get("final_status", "").lower()}">
                {self.results.get("final_status", "UNKNOWN")}
            </h3>
        </div>

        <div class="card">
            <h2>❌ Missing Values</h2>
            <table>
                <tr><th>Column</th><th>Missing</th><th>%</th></tr>
        """

        for col, val in self.results.get("missing", {}).items():
            html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{val['missing_count']}</td>
                    <td>{val['missing_percentage']}%</td>
                </tr>
            """

        html += """
            </table>
        </div>
        """

        html += """
        <div class="card">
            <h2>📊 Outliers</h2>
            <table>
                <tr><th>Column</th><th>Outliers</th><th>Ratio</th><th>Status</th></tr>
        """

        for col, val in self.results.get("outliers", {}).items():
            html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{val['outliers']}</td>
                    <td>{round(val['outlier_ratio'] * 100, 2)}%</td>
                    <td>{val['status']}</td>
                </tr>
            """

        html += """
            </table>
        </div>

        <div class="card">
            <h2>🧠 Schema</h2>
            <table>
                <tr><th>Column</th><th>Type</th><th>Numeric</th></tr>
        """

        for col, val in self.results.get("schema", {}).items():
            html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{val['dtype']}</td>
                    <td>{val['is_numeric']}</td>
                </tr>
            """

        html += """
            </table>
        </div>

        </body>
        </html>
        """

        with open(output_path, "w") as f:
            f.write(html)

        print(f"[INFO] HTML report generated at {output_path}")
