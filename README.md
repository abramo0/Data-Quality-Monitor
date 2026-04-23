# 📊 Data Quality Monitor

## 🚀 Overview

Data Quality Monitor is a Python-based data observability tool designed to evaluate and monitor the quality of datasets used in machine learning and data engineering workflows.

It detects common data issues such as missing values, outliers, schema inconsistencies, and basic data drift, helping ensure reliable and clean datasets before they are used in ML pipelines.

---

## 🎯 Problem Statement

In real-world data science and machine learning systems, poor data quality is one of the main causes of model degradation and unreliable predictions.

This project addresses the need for:
- Automated dataset validation
- Early detection of data issues
- Reliable preprocessing workflows before model training

---

## ⚙️ Features

- Missing values detection and summary report  
- Outlier detection using statistical methods (IQR)  
- Schema validation (column type and consistency checks)  
- Basic data drift detection (distribution comparison)  
- Automated data quality report generation  

---

## 🧱 Project Architecture

CSV Dataset → Data Loader → Validation Engine → Metrics Engine → Report Generator → Final Data Quality Report

Metrics Engine includes:
- Missing Values Check  
- Outlier Detection  
- Schema Validation  
- Drift Detection  

---

## 🛠️ Tech Stack

Core:
- Python  
- Pandas  
- NumPy  

Configuration:
- PyYAML  

---

## 📁 Project Structure

data-quality-monitor/
│
├── src/
│   ├── core/
│   │   ├── loader.py
│   │   ├── validator.py
│   │   ├── drift.py
│   │
│   ├── metrics/
│   │   ├── missing.py
│   │   ├── outliers.py
│   │   ├── schema.py
│   │
│   ├── report/
│   │   ├── generator.py
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── logger.py
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
│
├── main.py
├── requirements.txt
└── README.md

---

## ⚙️ How It Works

1. Load dataset (CSV file)  
2. Run validation checks:
   - Missing values analysis  
   - Outlier detection  
   - Schema consistency checks  
   - Basic drift detection  
3. Compute data quality metrics  
4. Generate structured report  

---

## 📊 Example Output

DATA QUALITY REPORT
--------------------
Missing Values: OK  
Outliers: WARNING (2 columns affected)  
Schema: OK  
Drift: DETECTED  

Final Score: 78/100  
Status: ⚠️ NEEDS ATTENTION  

---

## 🚀 Future Improvements

- Machine learning-based anomaly detection  
- Real-time data monitoring system  
- Advanced drift detection (KS test, PSI)  
- Web dashboard (Streamlit)  
- API layer using FastAPI  
- Integration with data pipelines (ETL systems)  

---

## 🧠 Key Learnings

This project demonstrates:

- Data quality validation techniques used in production systems  
- Modular Python architecture design  
- Data engineering pipeline thinking  
- Early-stage data observability concepts  
- Preparation for real-world ML systems  

---

## 👨‍💻 Author

Abramo Azer  
Aspiring Data Engineer & AI Engineer  
Focused on building scalable data systems and machine learning pipelines  

---

## 📌 Status

In Development — core modules being implemented
