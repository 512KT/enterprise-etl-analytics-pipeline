import pandas as pd
from sqlalchemy import create_engine

customers = pd.read_csv("data/customers.csv")
transactions = pd.read_csv("data/transactions.csv")
products = pd.read_csv("data/products.csv")

customers["email"] = customers["email"].fillna("missing@domain.com")
customers["country"] = customers["country"].fillna("Unknown")

transactions["amount"] = transactions["amount"].fillna(0)
products["price"] = products["price"].fillna(0)

def customer_quality(row):
    if row["email"] == "missing@domain.com":
        return "MISSING_EMAIL"
    if row["country"] == "Unknown":
        return "MISSING_COUNTRY"
    return "OK"

customers["data_quality_flag"] = customers.apply(customer_quality, axis=1)

def transaction_quality(row):
    if row["amount"] <= 0:
        return "INVALID_AMOUNT"
    return "OK"

transactions["data_quality_flag"] = transactions.apply(transaction_quality, axis=1)

def product_quality(row):
    if row["price"] <= 0:
        return "INVALID_PRICE"
    return "OK"

products["data_quality_flag"] = products.apply(product_quality, axis=1)

engine = create_engine("sqlite:///warehouse.db")

customers.to_sql("customers", engine, if_exists="replace", index=False)
transactions.to_sql("transactions", engine, if_exists="replace", index=False)
products.to_sql("products", engine, if_exists="replace", index=False)

print("ETL PIPELINE COMPLETE - DATA LOADED INTO WAREHOUSE")