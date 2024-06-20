DROP TABLE IF EXISTS silver.order;
CREATE TABLE silver.order AS
SELECT *
FROM bronze.order
WHERE status = 'FINISHED';
