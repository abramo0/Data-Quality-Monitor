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
            <h3 class="{str(self.results.get("final_status", "")).lower()}">
                {self.results.get("final_status", "UNKNOWN")}
            </h3>
        </div>
        """

        # --------------------------
        # MISSING VALUES
        # --------------------------
        html += """
        <div class="card">
            <h2>❌ Missing Values</h2>
            <table>
                <tr><th>Column</th><th>Missing</th><th>%</th></tr>
        """

        for col, val in self.results.get("missing", {}).items():
            html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{val.get('missing_count', 0)}</td>
                    <td>{val.get('missing_percentage', 0)}%</td>
                </tr>
            """

        html += """
            </table>
        </div>
        """

        # --------------------------
        # OUTLIERS
        # --------------------------
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
                    <td>{val.get('outliers', 0)}</td>
                    <td>{round(val.get('outlier_ratio', 0) * 100, 2)}%</td>
                    <td>{val.get('status', 'UNKNOWN')}</td>
                </tr>
            """

        html += """
            </table>
        </div>
        """

        # --------------------------
        # SCHEMA (FIX IMPORTANTISSIMO)
        # --------------------------
        html += """
        <div class="card">
            <h2>🧠 Schema</h2>
            <table>
                <tr><th>Column</th><th>Type</th><th>Numeric</th></tr>
        """

        schema = self.results.get("schema", {}).get("columns", {})

        for col, val in schema.items():
            html += f"""
                <tr>
                    <td>{col}</td>
                    <td>{val.get('dtype', 'unknown')}</td>
                    <td>{val.get('is_numeric', False)}</td>
                </tr>
            """

        html += """
            </table>
        </div>
        """

        # --------------------------
        # SAVE FILE
        # --------------------------
        html += """
        </body>
        </html>
        """

        with open(output_path, "w") as f:
            f.write(html)

        print(f"[INFO] HTML report generated at {output_path}")
