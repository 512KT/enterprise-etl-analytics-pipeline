from etl_pipeline.extract import extract
from etl_pipeline.transform import transform


def test_extract():

    customers, transactions, products = extract()

    assert len(customers) > 0
    assert len(transactions) > 0
    assert len(products) > 0


def test_transform():

    customers, transactions, products = extract()

    customers_t, transactions_t, products_t, enriched = transform(
        customers,
        transactions,
        products
    )

    assert len(customers_t) > 0
    assert len(transactions_t) > 0
    assert len(products_t) > 0
    assert len(enriched) > 0


def test_transaction_amounts():

    customers, transactions, products = extract()

    assert transactions["amount"].notnull().all()


def test_product_prices():

    customers, transactions, products = extract()

    assert products["price"].notnull().all()