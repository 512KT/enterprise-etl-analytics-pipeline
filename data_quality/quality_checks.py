import pandas as pd


def check_nulls(df, table_name):

    results = []

    for column in df.columns:

        null_count = df[column].isnull().sum()

        results.append({
            "table": table_name,
            "check": "NULL_CHECK",
            "column": column,
            "failed_records": int(null_count),
            "status": "PASS" if null_count == 0 else "FAIL"
        })

    return results


def check_duplicates(df, table_name):

    duplicate_count = df.duplicated().sum()

    return [{
        "table": table_name,
        "check": "DUPLICATE_CHECK",
        "column": "ALL",
        "failed_records": int(duplicate_count),
        "status": "PASS" if duplicate_count == 0 else "FAIL"
    }]


def check_transaction_amounts(df):

    invalid_count = (df["amount"] <= 0).sum()

    return [{
        "table": "transactions",
        "check": "AMOUNT_CHECK",
        "column": "amount",
        "failed_records": int(invalid_count),
        "status": "PASS" if invalid_count == 0 else "FAIL"
    }]


def check_product_prices(df):

    invalid_count = (df["price"] <= 0).sum()

    return [{
        "table": "products",
        "check": "PRICE_CHECK",
        "column": "price",
        "failed_records": int(invalid_count),
        "status": "PASS" if invalid_count == 0 else "FAIL"
    }]


def generate_quality_report(customers, transactions, products):

    results = []

    results.extend(check_nulls(customers, "customers"))
    results.extend(check_duplicates(customers, "customers"))

    results.extend(check_nulls(transactions, "transactions"))
    results.extend(check_duplicates(transactions, "transactions"))
    results.extend(check_transaction_amounts(transactions))

    results.extend(check_nulls(products, "products"))
    results.extend(check_duplicates(products, "products"))
    results.extend(check_product_prices(products))

    return pd.DataFrame(results)