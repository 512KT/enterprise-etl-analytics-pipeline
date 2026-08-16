# Enterprise ETL & Analytics Pipeline

## Overview

Built an end-to-end enterprise-style ETL and analytics pipeline using Python, Pandas, SQL, SQLite, Pytest, and Matplotlib.

The project demonstrates how raw operational data can be extracted, transformed, validated, enriched, loaded into a structured data warehouse, tested, and converted into business-oriented analytics.

The pipeline processes intentionally generated synthetic enterprise data containing:

- 500 customers
- 2,000 transactions
- 50 products
- 2,000 enriched transaction records

The source data intentionally contains data-quality issues so the pipeline can demonstrate automated detection, validation, and reporting.

---

## Architecture

    Synthetic Source Data
            |
            v
       Data Extraction
            |
            v
       Data Transformation
            |
            v
     Data Quality Validation
            |
            v
     SQLite Data Warehouse
            |
       +----+----+
       |         |
       v         v
    Testing   Analytics
                 |
            +----+----+
            |         |
            v         v
           KPIs   Visualization

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | ETL pipeline development and automation |
| Pandas | Data transformation and analysis |
| SQL | Data querying and analytical calculations |
| SQLite | Source database and data warehouse |
| Pytest | Automated testing |
| Matplotlib | Data visualization |
| Git/GitHub | Version control and project documentation |

---

## Project Structure

    enterprise_etl_project/
    |
    ├── data_quality/
    |   └── quality_checks.py
    |
    ├── etl_pipeline/
    |   ├── extract.py
    |   ├── transform.py
    |   ├── load.py
    |   └── run_pipeline.py
    |
    ├── scripts/
    |   ├── generate_data.py
    |   ├── run_quality_checks.py
    |   ├── kpi_dashboard.py
    |   └── data_visualization.py
    |
    ├── tests/
    |   └── test_pipeline.py
    |
    ├── output/
    |   ├── data_quality_report.csv
    |   └── transaction_quality.png
    |
    ├── logs/
    |   └── pipeline.log
    |
    ├── source.db
    ├── warehouse.db
    └── README.md

---

## ETL Pipeline

### Extract

The extraction layer reads customer, transaction, and product data from SQLite into Pandas DataFrames.

The pipeline separates data extraction from downstream transformation and loading, allowing each stage of the ETL process to be developed and tested independently.

### Transform

The transformation layer prepares source data for analytics and data warehousing.

Transformations include:

- Data validation
- Data cleaning
- Data-quality indicator creation
- Transaction enrichment
- Customer and product joins
- Preparation of analytics-ready datasets

Transaction records are enriched with related customer and product information to create a combined analytical dataset.

### Load

The loading layer writes transformed datasets into a structured SQLite data warehouse.

The warehouse contains staging, dimension, and fact tables.

#### Staging Tables

- stg_customers
- stg_transactions
- stg_products

#### Dimension Tables

- dim_customers
- dim_products

#### Fact Tables

- fact_transactions
- fact_transaction_customer

This structure demonstrates fundamental data-warehouse concepts by separating staging data from analytical dimensions and transactional facts.

---

## Data Quality Framework

The project includes an automated data-quality framework designed to identify problematic records before they are used for analysis.

Automated validation checks include:

- NULL value detection
- Duplicate record detection
- Invalid transaction amount detection
- Invalid product price detection

The generated source data intentionally contains invalid records.

The quality framework identified:

- 22 transactions with invalid amounts
- 2 products with invalid prices

The pipeline reports these issues rather than silently removing the records, allowing data-quality problems to be identified and investigated.

Quality results are exported to:

    output/data_quality_report.csv

---

## Automated Testing

The project uses Pytest to validate important parts of the pipeline.

Tests cover:

- Transformation output
- Transaction data
- Product data

The automated test suite helps verify that core pipeline outputs meet expected conditions.

Run the tests with:

    python3 -m pytest

---

## SQL & Analytics

SQL is used throughout the project to query source and warehouse data and support analytical workflows.

The project supports analysis including:

- Customer counts
- Transaction counts
- Revenue calculations
- Average transaction value
- Data-quality analysis
- Product analysis
- Transaction-status analysis

The warehouse structure provides organized staging, dimension, and fact tables for analytical queries.

---

## KPI Reporting

The project includes a Python-based KPI reporting script that generates business-oriented metrics from the data.

Reported KPIs include:

- Total customers
- Total transactions
- Valid transactions
- Invalid transactions
- Total revenue
- Average transaction value
- Total products

Run the KPI report with:

    python3 scripts/kpi_dashboard.py

---

## Data Visualization

The project uses Matplotlib to generate analytical visualizations from the processed data.

The current visualization output is saved to:

    output/transaction_quality.png

The visualization demonstrates the ability to convert processed data into a visual analytical output for easier interpretation.

---

## Logging

The ETL pipeline includes execution logging.

Pipeline events are recorded in:

    logs/pipeline.log

The log records major execution stages including:

- Pipeline start
- Data extraction
- Transformation completion
- Warehouse loading
- Pipeline completion

Logging provides basic operational visibility into pipeline execution and helps identify where failures occur.

---

## Data Warehouse

The SQLite warehouse stores the processed datasets used for downstream analytics.

The warehouse contains:

- 500 customers
- 2,000 transactions
- 50 products
- 2,000 enriched transaction records

The warehouse design separates operational staging data from analytical dimensions and facts, providing a foundation for downstream reporting and analysis.

---

## Reproducibility

The project includes a synthetic data-generation script so the pipeline can be rerun using a controlled dataset.

### Generate Source Data

    python3 scripts/generate_data.py

### Run the ETL Pipeline

    python3 -m etl_pipeline.run_pipeline

### Run Data-Quality Checks

    python3 -m scripts.run_quality_checks

### Run Automated Tests

    python3 -m pytest

### Generate KPI Report

    python3 scripts/kpi_dashboard.py

### Generate Visualization

    python3 scripts/data_visualization.py

---

## Key Skills Demonstrated

### Data Engineering

- ETL pipeline development
- Data extraction
- Data transformation
- Data enrichment
- Data validation
- Data warehousing
- Staging tables
- Dimension tables
- Fact tables
- Pipeline automation

### Python

- Python programming
- Pandas
- DataFrame operations
- Modular Python development
- Functions
- Database interaction
- Pipeline scripting

### SQL & Databases

- SQL querying
- SQLite
- Relational data modeling
- Filtering
- Aggregations
- Grouping
- Joins
- Data warehouse table design

### Data Quality

- NULL validation
- Duplicate detection
- Business-rule validation
- Invalid-record detection
- Automated quality reporting

### Analytics

- KPI development
- Revenue analysis
- Customer analysis
- Product analysis
- Transaction analysis
- Data visualization

### Software Engineering Practices

- Automated testing with Pytest
- Pipeline logging
- Modular project structure
- Reproducible execution
- Git/GitHub version control

---

## Project Outcome

This project demonstrates an end-to-end data engineering and analytics workflow, from synthetic source-data generation and extraction through transformation, validation, enrichment, warehouse loading, automated testing, KPI reporting, and visualization.

The result is a reproducible enterprise-style pipeline that transforms raw operational data into validated, structured, and analytics-ready data.

The project provides practical experience across:

- Data engineering
- Python development
- SQL
- Data quality
- Data warehousing
- Automated testing
- Business analytics
- Data visualization