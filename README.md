# 📊 Data Quality Monitor

A lightweight Python CLI tool to automatically detect data quality issues in CSV datasets before they are used in data science and machine learning pipelines.

---

## 🚀 Overview

Data Quality Monitor is a simple but extensible data validation tool designed to analyze CSV datasets and generate structured quality reports directly in the terminal.

It helps ensure datasets are clean and usable before entering downstream data processing or ML pipelines.

---

## 🎯 Why This Project Matters

Poor data quality is one of the most common causes of failure in data pipelines and machine learning models.

This tool helps to:

- Detect missing data early  
- Standardize dataset validation workflows  
- Improve data reliability  
- Provide quick dataset insights via CLI  

---

## ⚙️ Features

- 📥 Load CSV datasets from local path or CLI input  
- ❌ Missing values detection per column  
- 📊 Validation pipeline structure  
- 🧾 Clean and readable console reports  
- 🧠 Modular architecture for future extensions  

---

## 🧱 Architecture

CSV → Data Loader → Validator → Report Generator → Console Output

Current validation layer:
- Missing Values Check  

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/abramo0/Data-Quality-Monitor
cd data-quality-monitor
```

---

### 2. Create a virtual environment
```bash
python3 -m venv venv
```

---

### 3. Activate the environment

Linux / Mac:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

---

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 5. Run the project

You must provide a CSV file path:

```bash
python main.py --file data/raw/data.csv
```

or:

```bash
python main.py --file /home/user/Desktop/file.csv
```

---

## 📊 Example Output

```
============================================================
📊 DATA QUALITY REPORT
============================================================

📌 MISSING VALUES
------------------------------------------------------------
Column         Missing   Percentage     Status
------------------------------------------------------------
name           0         0.0%           OK
age            1         33.33%         WARNING

------------------------------------------------------------
TOTAL MISSING VALUES: 1
OVERALL MISSING RATE: 16.67%
============================================================
```

---

## 📁 Project Structure

```
data-quality-monitor/
│
├── src/
│   ├── core/
│   │   ├── loader.py
│   │   ├── validator.py
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
│       ├── config.py
│       ├── logger.py
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
```

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- argparse (CLI handling)  

---

## 🚀 Future Improvements

- Outlier detection (IQR method)  
- Schema validation  
- Data drift detection  
- JSON / HTML report export  
- Streamlit dashboard  
- Data quality scoring system (0–100)  
- API layer with FastAPI  

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Abramo Azer  
Aspiring Data Engineer & AI Engineer  
Focused on building scalable data systems and ML pipelines  

---

## 📌 Status

Active development — core pipeline (loading → validation → reporting) is implemented
