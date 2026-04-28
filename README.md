# 📊 Data Quality Monitor

A lightweight Python tool to automatically detect data quality issues before they break your machine learning pipelines.

---

## 🚀 Overview

Data Quality Monitor is a data observability tool designed to evaluate and monitor the quality of datasets used in machine learning and data engineering workflows.

It detects common data issues such as missing values, outliers, schema inconsistencies, and data drift — ensuring datasets are reliable before entering production pipelines.

---

## 🎯 Why This Project Matters

Poor data quality is one of the leading causes of model failure in real-world systems.

This tool helps to:

- Detect data issues early  
- Prevent unreliable ML predictions  
- Standardize dataset validation workflows  
- Improve overall data reliability in pipelines  

---

## ⚙️ Features

- Missing values detection and summary reports  
- Outlier detection using statistical methods (IQR)  
- Schema validation (type consistency checks)  
- Basic data drift detection  
- Automated data quality report generation  

---

## 🧱 Architecture

CSV → Data Loader → Validation Engine → Metrics Engine → Report Generator → Output Report

Metrics Engine:
- Missing Values Check  
- Outlier Detection  
- Schema Validation  
- Drift Detection  

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/data-quality-monitor.git
cd data-quality-monitor
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
```

### 3. Activate the environment

Linux / Mac:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the project
```bash
python main.py
```

## ⚙️ How It Works

1. Load dataset from CSV file  
2. Run validation checks:
   - Missing values analysis  
   - Outlier detection (IQR method)  
   - Schema consistency validation  
   - Basic data drift detection  
3. Compute data quality metrics  
4. Generate a structured report  

---

## 📊 Example Output

DATA QUALITY REPORT  
-------------------  
Missing Values: OK  
Outliers: WARNING (2 columns affected)  
Schema: OK  
Drift: DETECTED  

Final Score: 78/100  
Status: ⚠️ Needs Attention  

---

## 📁 Project Structure

data-quality-monitor/

├── src/  
│   ├── core/  
│   │   ├── loader.py  
│   │   ├── validator.py  
│   │   ├── drift.py  
│  
│   ├── metrics/  
│   │   ├── missing.py  
│   │   ├── outliers.py  
│   │   ├── schema.py  
│  
│   ├── report/  
│   │   ├── generator.py  
│  
│   ├── utils/  
│       ├── config.py  
│       ├── logger.py  

├── data/  
│   ├── raw/  
│   └── processed/  

├── configs/  
│   └── config.yaml  

├── notebooks/  
│   └── exploration.ipynb  

├── tests/  

├── main.py  
├── requirements.txt  
└── README.md  

---

## 🛠️ Tech Stack

Core:
- Python  
- Pandas  
- NumPy  

Configuration:
- PyYAML  

---

## 🚀 Future Improvements

- Advanced drift detection (KS test, PSI)  
- Machine learning-based anomaly detection  
- Real-time data monitoring system  
- Web dashboard (Streamlit)  
- API layer using FastAPI  
- Integration with ETL pipelines  

---

## 🤝 Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

Copyright (c) 2026 Abramo Azer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

---

## 👨‍💻 Author

Abramo Azer  
Aspiring Data Engineer & AI Engineer  
Focused on building scalable data systems and machine learning pipelines  

---

## 📌 Status

In Development — core modules are currently being implemented
