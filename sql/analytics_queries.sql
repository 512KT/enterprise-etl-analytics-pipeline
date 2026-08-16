SELECT COUNT(*) AS total_customers
FROM customers;

SELECT country,
COUNT(*) AS customer_count
FROM customers
GROUP BY country;

SELECT SUM(amount) AS total_revenue
FROM transactions
WHERE data_quality_flag='OK';

SELECT *
FROM transactions
WHERE data_quality_flag='INVALID_AMOUNT';

SELECT *
FROM products
WHERE data_quality_flag='INVALID_PRICE';