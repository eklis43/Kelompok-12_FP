DROP TABLE IF EXISTS silver.supplier;
CREATE TABLE silver.supplier AS
SELECT *
FROM bronze.supplier
