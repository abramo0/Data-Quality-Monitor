# 📊 Data Quality Monitor

A lightweight Python CLI tool that automatically detects data quality issues in CSV datasets before they are used in data science and machine learning pipelines.

## 🚀 Overview

Data Quality Monitor is a modular and extensible data validation tool designed to analyze CSV datasets and generate structured quality reports either in the terminal or as exported JSON/HTML files.

It ensures datasets are clean, consistent, and reliable before being used in downstream data engineering or machine learning workflows.

## 🎯 Why this project matters

Poor data quality is one of the most common causes of failure in data pipelines and machine learning systems.

This project helps to:

- Detect missing or inconsistent data early  
- Improve dataset reliability  
- Standardize validation workflows  
- Identify anomalies before production  
- Generate automated quality reports  

## ⚙️ Features

- CSV dataset loading from CLI  
- Missing values detection (MissingChecker)  
- Outlier detection (IQR method)  
- Schema validation (dtype + numeric detection)  
- Basic data drift analysis  
- Data quality scoring system (0–100)  
- Structured console reports  
- JSON report export  
- HTML report generation  
- Logging system  
- Unit + integration testing support  
- Modular architecture  

## 🧱 Architecture

CSV  
↓  
Data Loader  
↓  
Validator  
├── MissingChecker  
├── OutlierChecker  
├── SchemaChecker  
└── Drift Analysis (optional)  
↓  
Scoring Engine  
↓  
Report Generator  
↓  
Console Output / JSON Export / HTML Export  

## 🚀 Quick Start

### 1. Clone repository

git clone https://github.com/abramo0/Data-Quality-Monitor.git  
cd Data-Quality-Monitor  

### 2. Create virtual environment

python3 -m venv venv  

### 3. Activate environment

Linux / Mac:  
source venv/bin/activate  

Windows:  
venv\Scripts\activate  

### 4. Install dependencies

pip install -r requirements.txt  

### 5. Run project

Basic execution:  
python3 main.py --file data/raw/data.csv  

Export JSON:  
python3 main.py --file data/raw/data.csv --export report.json  

Export HTML:  
python3 main.py --file data/raw/data.csv --export report.json --html report.html  

## 📊 Example Output

============================================================  
📊 DATA QUALITY REPORT  
============================================================  

MISSING VALUES  
name   0   0.0%   OK  
age    1   33.33%  WARNING  

OUTLIERS  
salary 2   5.20%  WARN  

SCHEMA  
name   object   False  
salary int64    True  

DRIFT  
columns: 2  
rows: 100  

FINAL SCORE: 87.4 / 100  
STATUS: GOOD  

============================================================  

## 📁 Project Structure

data-quality-monitor/  
├── src/  
│   ├── core/  
│   │   ├── loader.py  
│   │   ├── validator.py  
│   │   ├── drift.py  
│   │   └── score.py  
│   ├── metrics/  
│   │   ├── missing.py  
│   │   ├── outliers.py  
│   │   └── schema.py  
│   ├── report/  
│   │   ├── generator.py  
│   │   └── html_generator.py  
│   ├── utils/  
│   │   ├── config.py  
│   │   └── logger.py  
├── data/  
│   ├── raw/  
│   └── processed/  
├── configs/  
│   └── config.yaml  
├── tests/  
│   ├── integration/  
│   ├── unit/  
│   ├── regression/  
│   ├── fixtures/  
│   └── conftest.py  
├── main.py  
├── requirements.txt  
└── README.md  

## 🛠️ Tech Stack

- Python  
- Pandas  
- argparse  
- logging  
- pytest  

## 🧪 Running Tests

pytest  

## 🚀 Future Improvements

- Streamlit dashboard  
- Interactive HTML reports  
- Advanced drift detection (PSI, KS test)  
- Configurable thresholds (YAML-based)  
- FastAPI integration  
- Docker support  
- CI/CD pipeline (GitHub Actions)  

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

## 📄 License

MIT License

## 👨‍💻 Author

Abramo Azer  
Aspiring Data Engineer & AI Engineer  
Focused on building scalable data systems and ML pipelines

## 📌 Status

Active development — modular validation pipeline and scoring system implemented.
