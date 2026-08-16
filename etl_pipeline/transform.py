import pandas as pd


def transform(customers, transactions, products):

    customers = customers.copy()
    transactions = transactions.copy()
    products = products.copy()

    customers = customers.drop_duplicates()
    transactions = transactions.drop_duplicates()
    products = products.drop_duplicates()

    customers["country"] = (
        customers["country"]
        .fillna("UNKNOWN")
        .astype(str)
        .str.strip()
        .str.upper()
    )

    customers["email_quality_flag"] = customers["email"].apply(
        lambda email:
        "OK"
        if isinstance(email, str) and "@" in email
        else "INVALID_EMAIL"
    )

    transactions["amount"] = pd.to_numeric(
        transactions["amount"],
        errors="coerce"
    )

    transactions["data_quality_flag"] = transactions["amount"].apply(
        lambda amount:
        "OK"
        if pd.notna(amount) and amount > 0
        else "INVALID_AMOUNT"
    )

    transactions["amount"] = transactions["amount"].fillna(0)

    products["price"] = pd.to_numeric(
        products["price"],
        errors="coerce"
    )

    products["data_quality_flag"] = products["price"].apply(
        lambda price:
        "OK"
        if pd.notna(price) and price > 0
        else "INVALID_PRICE"
    )

    products["price"] = products["price"].fillna(0)

    enriched_transactions = transactions.merge(
        customers[
            [
                "customer_id",
                "country",
                "email_quality_flag"
            ]
        ],
        on="customer_id",
        how="left"
    )

    return (
        customers,
        transactions,
        products,
        enriched_transactions
    )