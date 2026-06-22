# Oracle ETL Automation Pipeline

## Project Overview

This project demonstrates an automated ETL (Extract, Transform, Load) pipeline using Python, Oracle Database, PL/SQL, and Oracle Scheduler.

The solution extracts account information from an Excel file, loads it into an Oracle master table, and archives historical records into a history table using a stored procedure.

The project simulates a real-world data engineering workflow involving data ingestion, database automation, and historical data management.

---

## Business Problem

Organizations often receive account updates through Excel files. Maintaining both current and historical records is important for auditing, reporting, and tracking changes over time.

This project addresses that requirement by:

* Loading account data from Excel into Oracle Database
* Maintaining current records in a master table
* Archiving processed records into a history table
* Automating archival using Oracle Scheduler

---

## Technology Stack

| Technology         | Purpose                      |
| ------------------ | ---------------------------- |
| Python             | ETL Development              |
| Pandas             | Excel Processing             |
| Oracle Database XE | Data Storage                 |
| SQL                | Database Operations          |
| PL/SQL             | Stored Procedure Development |
| Oracle Scheduler   | Job Automation               |
| OpenPyXL           | Excel Integration            |

---

## ETL Workflow

### Extract

Read account information from:

```text
master.xlsx
```

### Transform

Validate and prepare data for insertion into Oracle Database.

### Load

Insert records into:

```text
MASTER_TABLE
```

### Archive

Move records from:

```text
MASTER_TABLE → HISTORY_TABLE
```

using the `MOVE_TO_HISTORY` stored procedure.

---

## Solution Architecture

```text
master.xlsx
      |
      v
load_master.py
      |
      v
MASTER_TABLE
      |
      v
MOVE_TO_HISTORY Procedure
      |
      v
HISTORY_TABLE
      ^
      |
Oracle Scheduler (12 PM Daily)
```

---

## Database Objects

### MASTER_TABLE

Stores the latest account information received from Excel.

### HISTORY_TABLE

Stores historical account records for auditing and tracking purposes.

### MOVE_TO_HISTORY Procedure

Responsibilities:

* Copy records from MASTER_TABLE
* Insert records into HISTORY_TABLE
* Delete processed records from MASTER_TABLE
* Commit the transaction

### MOVE_HISTORY_JOB

Oracle Scheduler job that automatically executes the archival procedure every day at 12 PM.

---

## Project Structure

```text
oracle-etl-automation-pipeline
│
├── load_master.py
├── master.xlsx
├── requirements.txt
├── README.md
│
├── sql
│   ├── create_master_table.sql
│   ├── create_history_table.sql
│   ├── move_to_history.sql
│   └── scheduler_job.sql
```

---

## Key Features

* Excel to Oracle ETL Pipeline
* Python Database Integration
* Oracle SQL and PL/SQL Development
* Automated Data Archival
* Historical Data Tracking
* Scheduler-Based Automation
* Real-World ETL Workflow

---

## Skills Demonstrated

* Data Engineering Fundamentals
* ETL Pipeline Development
* Oracle Database Administration
* SQL and PL/SQL Programming
* Python Automation
* Data Archival Strategy
* Scheduler-Based Automation

---

## Future Enhancements

* Automated Excel File Detection
* Email Notifications
* Logging Framework
* Error Handling and Monitoring
* Power BI Dashboard Integration

---

## Author

Nithya Sree

Aspiring Data Scientist | Python | SQL | Oracle Database
