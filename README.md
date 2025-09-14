# 💰 Curly-Memory: Personal Finance Tracker  

A Python application that consolidates my personal financial data from multiple sources into a single, easy-to-analyze 
database. Generates automated **Excel reports with charts** to track **net worth, assets, liabilities, and 
investments** over time.  

I originally built this in 2021 to simplify my monthly financial check-ins — and I still use it today.  

---

## 🚀 Features  

- **Data Ingestion**: Import statements from CSV, JSON, PDF, and HTML.  
- **Data Cleaning**: Standardize messy inputs from banks, stocks, loans, insurance, and mutual funds.  
- **Database**: Store and query consolidated financial data.  
- **Automated Reporting**: Generate Excel workbooks with summary tables and charts.  
- **Visualization**:  
  - Assets vs Liabilities  
  - Net worth over time  
  - Asset allocation breakdown  
  - Stock and mutual fund performances  

---

## 🛠️ Tech Stack  

- **Python**  
- **Pandas / PDF Plumber / Beautiful Soup** for data ingestion and cleaning  
- **SQLite** for storage  
- **Matplotlib** for visualization  
- **Openpyxl** for Excel export  
- **Pytest** for unit testing  

---

## 📊 Example Output  

**Summaries of my assets and liabilities**

<p align="left">
    <img src="assets/01 - summary.jpg" height="75" width="128"/>
    <img src="assets/02 - assets.jpg" height="75" width="128"/>
    <img src="assets/03 - liabilities.jpg" height="75" width="128"/> 
</p>

**Total assets, liabilities and net worth over time**

<img src="assets/04 - saln chart.jpg" height="75" width="128"/> 

**Asset allocation**

<p align="left">
    <img src="assets/05 - summaries.jpg" height="75" width="128"/> 
    <img src="assets/06 - cash vs loan amount.jpg" height="75" width="128"/> 
    <img src="assets/07 - portfolio allocation.jpg" height="75" width="128"/> 
</p>

**Stock, Portfolio and Funds' Performances**

<p align="left">
    <img src="assets/08 - profitability.jpg" height="75" width="128"/> 
    <img src="assets/09 - portfolio performance.jpg" height="75" width="128"/> 
    <img src="assets/10 - fund performance.jpg" height="75" width="128"/> 
</p>

*(See `assets/sample_output.xlsx` for full report.)*  

---

## ✅ Why This Matters  

- **Real-World Utility** → Not just a demo; I’ve used it monthly for several years.  
- **Demonstrates Data Skills** → Cleaning, transforming, and visualizing real-world financial data.  
- **End-to-End Project** → From ingestion → storage → analysis → reporting.  

---

## 📂 Project Structure  

    curly-memory/
    │── assets/ # screenshots and sample report
    │── charts/ # Create visualisations
    |── extractors/# Extract data from CSV, JSON, PDF, HTML
    │── main/ # Main modules of the application's sub-apps
    │── models/ # SQLite data access layer
    │── parsers # Standardizes extracted data
    │── tests/ # Unit tests
    │── financial_stmt_generator.py # Main module of the application
    │── README.md
    
---

This project shows my ability to **turn messy, multi-source data into actionable insights** — the same foundation 
that powers my work in **data analytics and reporting**.  
