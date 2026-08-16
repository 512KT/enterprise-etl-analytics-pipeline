import sqlite3


def load(customers, transactions, products, enriched_transactions):

    conn = sqlite3.connect("warehouse.db")

    customers.to_sql(
        "stg_customers",
        conn,
        if_exists="replace",
        index=False
    )

    transactions.to_sql(
        "stg_transactions",
        conn,
        if_exists="replace",
        index=False
    )

    products.to_sql(
        "stg_products",
        conn,
        if_exists="replace",
        index=False
    )

    customers.to_sql(
        "dim_customers",
        conn,
        if_exists="replace",
        index=False
    )

    products.to_sql(
        "dim_products",
        conn,
        if_exists="replace",
        index=False
    )

    transactions.to_sql(
        "fact_transactions",
        conn,
        if_exists="replace",
        index=False
    )

    enriched_transactions.to_sql(
        "fact_transaction_customer",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()