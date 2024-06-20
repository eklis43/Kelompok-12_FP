DROP TABLE IF EXISTS silver.product_category;
CREATE TABLE silver.product_category AS
SELECT *
FROM bronze.product_category
