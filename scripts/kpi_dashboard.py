import sqlite3
import pandas as pd

conn = sqlite3.connect("warehouse.db")

customers = pd.read_sql(
    "SELECT * FROM dim_customers",
    conn
)

transactions = pd.read_sql(
    "SELECT * FROM fact_transactions",
    conn
)

products = pd.read_sql(
    "SELECT * FROM dim_products",
    conn
)

conn.close()

valid_transactions = transactions[
    transactions["amount"] > 0
]

total_revenue = valid_transactions["amount"].sum()

average_transaction_value = valid_transactions["amount"].mean()

print("===================================")
print("ENTERPRISE ETL KPI REPORT")
print("===================================")
print(f"Total Customers: {len(customers)}")
print(f"Total Transactions: {len(transactions)}")
print(f"Valid Transactions: {len(valid_transactions)}")
print(f"Invalid Transactions: {len(transactions) - len(valid_transactions)}")
print(f"Total Revenue: {total_revenue:.2f}")
print(f"Average Transaction Value: {average_transaction_value:.2f}")
print(f"Total Products: {len(products)}")
print("===================================")