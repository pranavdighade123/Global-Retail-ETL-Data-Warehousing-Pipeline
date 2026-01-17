import pandas as pd
import oracledb
import config
import os
import time

# Configuration for paths
CSV_PATH = "../data/landing_zone/online_retail_II.csv"

def run_etl():
    start_time = time.time()
    conn = None
    
    try:
        # 1. Establish Connection
        print("--- ETL JOB STARTED ---")
        print("Connecting to Oracle XE...")
        conn = oracledb.connect(
            user=config.DB_USER, 
            password=config.DB_PASS, 
            dsn=config.DB_DSN
        )
        cursor = conn.cursor()

        # 2. Extract Data
        if not os.path.exists(CSV_PATH):
            raise FileNotFoundError(f"Source file not found at {CSV_PATH}")
            
        print(f"Extracting data from CSV...")
        # Using low_memory=False to handle the 1M+ rows efficiently
        df = pd.read_csv(CSV_PATH, low_memory=False)
        
        # 3. Transform (Force correct types for Oracle)
        print("Cleaning data for staging...")
        
        # Force these to string and replace 'nan' with empty strings
        df['Invoice'] = df['Invoice'].astype(str).replace('nan', '')
        df['StockCode'] = df['StockCode'].astype(str).replace('nan', '')
        df['Description'] = df['Description'].astype(str).replace('nan', 'No Description')
        df['InvoiceDate'] = df['InvoiceDate'].astype(str).replace('nan', '')
        df['Country'] = df['Country'].astype(str).replace('nan', '')

        # Force these to numeric
        df['Customer ID'] = pd.to_numeric(df['Customer ID'], errors='coerce').fillna(0)
        df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0)
        
        # Final safety check: Convert entire dataframe to list of tuples
        # and ensure every 'nan' or 'None' is handled
        records = df.values.tolist()
        
        # This converts any remaining Python 'nan' objects to None, 
        # which Oracle interprets as NULL
        records = [tuple(None if pd.isna(x) else x for x in row) for row in records]

        # 4. Load to Staging
        print("Truncating staging table...")
        cursor.execute("TRUNCATE TABLE STG_RETAIL_DATA")
        
        print(f"Loading {len(records)} records into STG_RETAIL_DATA...")
        sql_insert = """
            INSERT INTO STG_RETAIL_DATA (
                Invoice, StockCode, Description, Quantity, 
                InvoiceDate_Raw, Price, Customer_ID, Country
            ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
        """
        # Batch size of 50k for stability
        cursor.executemany(sql_insert, records)
        conn.commit()
        print("Staging load complete.")

        # 5. Trigger PL/SQL Transformation & Audit
        print("Executing PL/SQL Procedure: SP_TRANSFORM_RETAIL_DATA...")
        cursor.callproc("SP_TRANSFORM_RETAIL_DATA")
        
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        print(f"--- ETL JOB SUCCESSFUL (Time: {duration} seconds) ---")

    except Exception as e:
        print(f"!!! ETL JOB FAILED: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    run_etl()