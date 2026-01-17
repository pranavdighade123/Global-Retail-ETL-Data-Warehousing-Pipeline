# 📊 Global Retail Data Integration & Analytics Pipeline
🚀 Executive Summary
This project features a high-performance ETL (Extract, Transform, Load) Pipeline designed to ingest, process, and analyze 1.06 million rows of retail transaction data. By leveraging Python for orchestration and Oracle XE for the data warehouse, the system converts raw, messy CSV data into a structured, audit-logged Fact table ready for executive reporting.

🛠️ The Tech Stack
Orchestration: Python 3.x
Libraries: Pandas (Data Wrangling), Oracledb (Database Driver), Plotly (Visualization)
Database: Oracle Database XE (SQL & PL/SQL)
Dashboard: Streamlit (Web-based Analytics)
Environment: Linux/Git Bash

🏗️ Data Architecture & Workflow
The project follows a professional Staging-to-Fact (Medallion) architecture:

Extraction & Cleaning: A Python engine reads the 1M+ record dataset, handles missing values (NaN), and enforces data types to ensure Oracle compatibility.

High-Speed Ingestion: Utilized Bulk Insert (executemany) techniques to load data into the STG_RETAIL_DATA table, achieving high throughput for "Big Data" volumes.

PL/SQL Transformation: A dedicated stored procedure (SP_TRANSFORM_RETAIL_DATA) automates:

Currency/Revenue calculation (Quantity × Price).

Data validation (removing nulls and negative quantities).

Final migration to the FCT_RETAIL_SALES production table.

Governance & Audit: Every run is logged in an ETL_LOG_AUDIT table, capturing record counts, timestamps, and job status (SUCCESS/FAIL).

📈 Business Intelligence Dashboard
The final layer is a real-time Streamlit Dashboard that allows stakeholders to:

Track Key Performance Indicators (KPIs) like Total Revenue and Order Volume.

Analyze Market Penetration via interactive "Revenue by Country" bar charts.

Monitor Data Quality by viewing the latest ETL audit logs.

📂 Project Structure
├── data/               # Landing Zone (CSV files - ignored in Git)
├── scripts/
│   ├── main_etl.py     # Python Orchestrator
│   └── dashboard.py    # Streamlit Web App
├── sql/
│   ├── ddl_setup.sql   # Tables & Schema creation
│   └── procedures.sql  # PL/SQL Transformation logic
└── README.md           # Project Documentation

💡 Key Challenges Solved
Data Type Mismatch: Resolved DPY-3013 errors by implementing a robust Python cleaning layer to handle NaN values before database ingestion.

Memory Management: Optimized Pandas ingestion for 1M+ rows using low_memory=False and batch processing.

Transaction Integrity: Ensured ACID compliance by using database commits only after successful PL/SQL transformation.


