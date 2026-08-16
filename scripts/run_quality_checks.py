import sqlite3
import pandas as pd
from data_quality.quality_checks import generate_quality_report

conn = sqlite3.connect("warehouse.db")

customers = pd.read_sql("SELECT * FROM dim_customers", conn)

transactions = pd.read_sql("SELECT * FROM fact_transactions", conn)

products = pd.read_sql("SELECT * FROM dim_products", conn)

conn.close()

report = generate_quality_report(
    customers,
    transactions,
    products
)

print(report)

report.to_csv(
    "output/data_quality_report.csv",
    index=False
)

print("Data quality report saved to output/data_quality_report.csv")