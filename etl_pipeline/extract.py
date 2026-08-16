import sqlite3
import pandas as pd

def extract():

    conn = sqlite3.connect("source.db")
    
    customers = pd.read_sql( "SELECT * FROM customers", conn)

    transactions = pd.read_sql("SELECT * FROM transactions", conn)

    products = pd.read_sql("SELECT * FROM products", conn)  

    conn.close()

    return customers, transactions, products