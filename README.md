# Global Retail Data Integration & Analytics Pipeline
### High-Performance ETL Orchestration: Python, Oracle XE, and PL/SQL

## 📖 Project Executive Summary
This repository contains a robust, end-to-end Data Engineering pipeline designed to process and analyze a global retail dataset consisting of **1.06 million transactions**. The architecture demonstrates a professional transition of raw "Bronze" layer data into a refined "Gold" layer **Star Schema Data Warehouse**, ensuring high data integrity, auditability, and executive-level visualization.

---

## 🏗️ System Architecture & Engineering Patterns

### 1. Data Extraction & Ingestion (The Orchestrator)
[cite_start]The ingestion engine is built with **Python**, utilizing the `oracledb` driver and **Pandas** for high-speed data handling[cite: 1].
* **Performance Optimization:** Implemented batch processing to handle high-volume ingestion, significantly reducing database overhead.
* **Data Sanitization:** A proactive transformation layer handles schema enforcement, null-value imputation (addressing Customer ID and Description gaps), and type casting to maintain database consistency.
* **Automation:** A Bash-based "File Watcher" script (`file_check.sh`) manages environment readiness and ensures idempotent pipeline runs.

### 2. Data Warehousing & Dimensional Modeling
[cite_start]The solution utilizes **Oracle Database XE** with a structured Staging-to-Fact design pattern[cite: 1]:
* **Staging Layer (STG):** A landing zone designed for rapid ingestion without constraints, minimizing source-system lock time.
* **Production Layer (Fact/Dimension):** An ACID-compliant Star Schema consisting of `DIM_PRODUCT`, `DIM_CUSTOMER`, `DIM_GEO_LOCATION`, and `DIM_DATE` tables, optimized for analytical queries.

### 3. Business Logic & PL/SQL Transformation
Following the **ELT (Extract, Load, Transform)** philosophy, all heavy-duty business logic is encapsulated within the database:
* **Stored Procedures:** PL/SQL logic manages the migration from Staging to Fact tables, handling revenue calculation and multi-column validation.
* **Audit & Governance:** An automated logging system tracks every pipeline execution, recording job status, timestamps, and processed record counts to ensure data lineage.

---

## 📊 Analytical Insights & Delivery
A real-time **Python-based Web Application** serves as the consumption layer, providing:
* **Executive KPIs:** Instant visibility into Total Revenue, Global Order Volume, and Top Performing Markets.
* **Trend Analysis:** Interactive visualizations to identify regional sales distributions, monthly trends, and outliers.

---

## 🛠️ Key Technical Competencies
* **ETL/ELT Pipeline Design:** Architecting data flows from flat-files (1M+ rows) to relational warehouses.
* **Database Programming:** Advanced SQL and PL/SQL for stored procedures and DDL management.
* **Data Quality:** Implementing logic to handle returns (negative quantities) and invalid customer data.
* **Full-Stack Data Delivery:** Bridging the gap between raw backend data and frontend business insights via Dash/Streamlit.

---

## 📂 Repository Structure
* **/scripts:** Python orchestrators for ETL execution (`main_etl.py`) and Dashboard hosting (`dashboard.py`).
* **/sql:** Schema definitions, DDL, and PL/SQL transformation logic.
* **/shell:** Bash scripts for workflow automation (`file_check.sh`).
* **/docs:** Project report and architectural documentation.

---
**Developer:** [Your Name]  
**Status:** Validated & Production-Ready
