# Global Retail Data Integration & Analytics Pipeline
High-Performance ETL Orchestration: Python, Oracle XE, and PL/SQL
📖 Executive Summary
This repository contains a robust, end-to-end Data Engineering pipeline designed to process and analyze a large-scale retail dataset consisting of 1.06 million transactions. The architecture demonstrates the transition of raw "Bronze" layer data into a refined "Gold" layer Data Warehouse, ensuring high data integrity, auditability, and executive-level visualization.

🏗️ System Architecture & Engineering Patterns
1. Data Extraction & Ingestion (The Orchestrator)
The ingestion engine is built with Python, utilizing the oracledb driver and Pandas.
Performance Optimization: Implemented Bulk-Loading techniques (executemany) to handle high-volume ingestion, reducing the overhead of individual row commits.
Data Sanitization: A proactive transformation layer handles schema enforcement, null-value imputation (addressing NaN issues), and type casting to maintain database consistency.

2. Data Warehousing & Modeling (The Core)
The solution utilizes Oracle Database XE with a structured Staging-to-Fact design pattern.
Staging Layer (STG): A landing zone designed for rapid ingestion without constraints, minimizing source-system lock time.
Production Layer (FCT): An ACID-compliant Fact table optimized for analytical queries and downstream reporting.

3. Business Logic & Transformation (The Processor)
Rather than performing heavy computation in Python, this project follows the ELT (Extract, Load, Transform) philosophy:
PL/SQL Stored Procedures: All business logic—including revenue calculation, multi-column validation, and data migration—is encapsulated within the database for maximum performance and security.
Audit & Governance: An automated Audit Logging System tracks every pipeline execution, recording job status, timestamps, and processed record counts to ensure data lineage and reliability.

4. Analytical Insights (The Delivery)
A real-time Streamlit Web Application serves as the consumption layer, providing:
Executive KPIs: Instant visibility into Total Revenue, Global Order Volume, and Top Performing Markets.
Geospatial & Trend Analysis: Interactive visualizations built with Plotly to identify regional sales distributions and outliers.

🛠️ Key Technical Competencies
ETL/ELT Pipeline Design: Architecting data flows from flat-files to relational warehouses.
Database Programming: Advanced PL/SQL for stored procedures, views, and DDL management.
Performance Tuning: Handling million-row datasets via batch processing and optimized data types.
Full-Stack Data Delivery: Bridging the gap between raw backend data and frontend business insights.

📂 Repository Structure
/scripts: Python orchestrators for ETL execution and Dashboard hosting.
/sql: Schema definitions, DDL, and PL/SQL transformation logic.
/docs: (Optional) Architectural diagrams and project documentation.
