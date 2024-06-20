DROP TABLE IF EXISTS silver.product;
CREATE TABLE silver.product AS
SELECT *,
  CASE
    WHEN price BETWEEN 0 AND 15 THEN 'Cheap'
    WHEN price BETWEEN 16 AND 50 THEN 'Medium'
    WHEN price > 50 THEN 'expensive'
  END AS price_label
FROM bronze.product;
