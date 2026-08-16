import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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

revenue_by_country = (
    transactions
    .merge(
        customers[["customer_id", "country"]],
        on="customer_id",
        how="left"
    )
    .query("amount > 0")
    .groupby("country")["amount"]
    .sum()
    .sort_values(ascending=False)
)

transaction_status = transactions["status"].value_counts()

revenue_by_category = (
    transactions
    .merge(
        customers[["customer_id", "country"]],
        on="customer_id",
        how="left"
    )
    .merge(
        products[["product_id", "category"]],
        on="product_id",
        how="left"
    )
    .query("amount > 0")
    .groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

top_customers = (
    transactions
    .query("amount > 0")
    .groupby("customer_id")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

revenue_by_country.plot(
    kind="bar",
    ax=axes[0, 0]
)

axes[0, 0].set_title("Revenue by Country")
axes[0, 0].set_xlabel("Country")
axes[0, 0].set_ylabel("Revenue")

transaction_status.plot(
    kind="bar",
    ax=axes[0, 1]
)

axes[0, 1].set_title("Transaction Status")
axes[0, 1].set_xlabel("Status")
axes[0, 1].set_ylabel("Transactions")

revenue_by_category.plot(
    kind="bar",
    ax=axes[1, 0]
)

axes[1, 0].set_title("Revenue by Product Category")
axes[1, 0].set_xlabel("Category")
axes[1, 0].set_ylabel("Revenue")

top_customers.plot(
    kind="barh",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Top 10 Customers by Revenue")
axes[1, 1].set_xlabel("Revenue")
axes[1, 1].set_ylabel("Customer ID")

plt.tight_layout()

plt.savefig(
    "output/enterprise_analytics_dashboard.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()