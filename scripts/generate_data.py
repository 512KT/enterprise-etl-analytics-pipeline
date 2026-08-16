import sqlite3
import random
from datetime import datetime, timedelta

random.seed(42)

conn = sqlite3.connect("source.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS transactions")
cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    country TEXT,
    data_quality_flag TEXT
)
""")

cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL,
    data_quality_flag TEXT
)
""")

cursor.execute("""
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    amount REAL,
    currency TEXT,
    status TEXT,
    transaction_date TEXT,
    data_quality_flag TEXT
)
""")

countries = ["USA", "UK", "Canada", "Germany", "Australia"]

first_names = [
    "John", "Jane", "Mark", "Sara", "Tom",
    "Alex", "Maria", "David", "Emily", "Chris"
]

last_names = [
    "Smith", "Johnson", "Brown", "Lee", "Kim",
    "Davis", "Wilson", "Taylor", "Martin", "Clark"
]

for customer_id in range(1, 501):
    name = random.choice(first_names) + " " + random.choice(last_names)
    email = name.lower().replace(" ", ".") + "@example.com"
    country = random.choice(countries)
    quality = "OK"

    if customer_id % 97 == 0:
        email = ""
        quality = "MISSING_EMAIL"

    if customer_id % 113 == 0:
        country = ""
        quality = "MISSING_COUNTRY"

    cursor.execute(
        """
        INSERT INTO customers
        VALUES (?, ?, ?, ?, ?)
        """,
        (customer_id, name, email, country, quality)
    )

categories = ["Electronics", "Furniture", "Office", "Accessories"]

for product_id in range(1, 51):
    category = random.choice(categories)
    product_name = f"{category} Product {product_id}"
    price = round(random.uniform(25, 2500), 2)
    quality = "OK"

    if product_id % 23 == 0:
        price = 0
        quality = "INVALID_PRICE"

    cursor.execute(
        """
        INSERT INTO products
        VALUES (?, ?, ?, ?, ?)
        """,
        (product_id, product_name, category, price, quality)
    )

statuses = ["completed", "completed", "completed", "pending", "failed"]
start_date = datetime(2026, 1, 1)

for transaction_id in range(1, 2001):
    customer_id = random.randint(1, 500)
    product_id = random.randint(1, 50)
    amount = round(random.uniform(25, 2500), 2)
    currency = "USD"
    status = random.choice(statuses)
    transaction_date = start_date + timedelta(
        days=random.randint(0, 364)
    )
    quality = "OK"

    if transaction_id % 89 == 0:
        amount = 0
        quality = "INVALID_AMOUNT"

    cursor.execute(
        """
        INSERT INTO transactions
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            transaction_id,
            customer_id,
            product_id,
            amount,
            currency,
            status,
            transaction_date.strftime("%Y-%m-%d"),
            quality
        )
    )

conn.commit()
conn.close()

print("Synthetic source data generated successfully.")