DROP TABLE IF EXISTS silver.customer;
CREATE TABLE silver.customer AS
SELECT *
FROM bronze.customer
