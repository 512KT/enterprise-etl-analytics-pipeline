import logging

from etl_pipeline.extract import extract
from etl_pipeline.transform import transform
from etl_pipeline.load import load


logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():

    logging.info("ETL pipeline started")

    customers, transactions, products = extract()

    logging.info(
        f"Extracted {len(customers)} customers, "
        f"{len(transactions)} transactions, "
        f"{len(products)} products"
    )

    customers_t, transactions_t, products_t, enriched = transform(
        customers,
        transactions,
        products
    )

    logging.info("Transformation completed")

    load(
        customers_t,
        transactions_t,
        products_t,
        enriched
    )

    logging.info("Warehouse load completed")

    logging.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()