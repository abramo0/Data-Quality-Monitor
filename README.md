# 📊 Data Quality Monitor

A lightweight Python CLI tool to automatically detect data quality issues in CSV datasets before they are used in data science and machine learning pipelines.

---

# 🚀 Overview

Data Quality Monitor is a modular and extensible data validation tool designed to analyze CSV datasets and generate structured quality reports directly in the terminal or exported as JSON reports.

It helps ensure datasets are clean, consistent, and reliable before entering downstream data engineering or machine learning workflows.

---

# 🎯 Why This Project Matters

Poor data quality is one of the most common causes of failure in data pipelines and machine learning systems.

This project helps to:

- Detect missing or inconsistent data early
- Improve dataset reliability
- Standardize validation workflows
- Identify anomalies before production
- Generate automated quality reports

---

# ⚙️ Features

- 📥 CSV dataset loading from CLI
- ❌ Missing values detection
- 📊 Outlier detection using IQR
- 🧠 Schema validation
- 📈 Basic drift analysis
- ⭐ Data quality scoring system (0–100)
- 🧾 Structured console reports
- 📄 JSON report export
- 🪵 Logging system
- 🧪 Unit testing support
- 🧱 Modular architecture

---

# 🧱 Architecture

```text
CSV
 ↓
Data Loader
 ↓
Validator
 ├── Missing Values Check
 ├── Outlier Detection
 ├── Schema Validation
 └── Drift Analysis
 ↓
Scoring Engine
 ↓
Report Generator
 ↓
Console Output / JSON Export
```

---

# 🚀 Quick Start

## 1. Clone the repository

```bash
git clone https://github.com/abramo0/Data-Quality-Monitor.git
cd Data-Quality-Monitor
```

---

## 2. Create a virtual environment

```bash
python3 -m venv venv
```

---

## 3. Activate the environment

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the project

### Analyze a dataset

```bash
python3 main.py --file data/raw/data.csv
```

### Analyze a dataset and export JSON report

```bash
python3 main.py --file data/raw/data.csv --export report.json
```

---

# 📊 Example Output

```text
============================================================
📊 DATA QUALITY REPORT
============================================================

📌 MISSING VALUES
------------------------------------------------------------
Column         Missing   Percentage     Status
------------------------------------------------------------
name           0         0.0%           OK
age            1         33.33%         WARNING

📌 OUTLIERS
------------------------------------------------------------
Column         Outliers  Ratio          Status
------------------------------------------------------------
salary         2         5.20%          WARN

📌 SCHEMA
------------------------------------------------------------
Column         Type            Numeric
------------------------------------------------------------
name           object          False
salary         int64           True

📌 DRIFT
------------------------------------------------------------
columns: 2
rows: 100

============================================================
⭐ FINAL SCORE: 87.4/100
📊 STATUS: GOOD
============================================================
```

---

# 📁 Project Structure

```text
data-quality-monitor/
│
├── src/
│   ├── core/
│   │   ├── loader.py
│   │   ├── validator.py
│   │   ├── drift.py
│   │   └── score.py
│   │
│   ├── metrics/
│   │   ├── missing.py
│   │   ├── outliers.py
│   │   └── schema.py
│   │
│   ├── report/
│   │   └── generator.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   └── logger.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── configs/
│   └── config.yaml
│
├── notebooks/
│   └── exploration.ipynb
│
├── tests/
│   ├── test_loader.py
│   ├── test_missing.py
│   ├── test_outliers.py
│   └── test_validator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

- Python
- Pandas
- argparse
- logging
- pytest

---

# 🧪 Running Tests

Run all tests using:

```bash
pytest
```

---

# 🚀 Future Improvements

- HTML report export
- Interactive Streamlit dashboard
- Configurable validation thresholds
- Advanced drift detection
- FastAPI integration
- Docker support
- CI/CD with GitHub Actions

---

# 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

Abramo Azer  
Aspiring Data Engineer & AI Engineer  
Focused on building scalable data systems and machine learning pipelines.

---

# 📌 Status

Active development — modular validation pipeline and scoring system implemented.
