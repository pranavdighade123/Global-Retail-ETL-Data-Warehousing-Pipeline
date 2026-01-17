#!/bin/bash
# ETL File Arrival Check Script

# Define paths
LANDING_DIR="../data/landing_zone"
LOG_FILE="../logs/process.log"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

echo "[$TIMESTAMP] Starting file arrival check..." >> $LOG_FILE

# Check if the specific CSV exists
if [ -f "$LANDING_DIR/online_retail_II.csv" ]; then
    echo "[$TIMESTAMP] SUCCESS: online_retail_II.csv found." >> $LOG_FILE
    echo "File detected. Ready for ETL."
else
    echo "[$TIMESTAMP] ERROR: File not found in landing zone." >> $LOG_FILE
    echo "File missing. Check logs."
    exit 1
fi