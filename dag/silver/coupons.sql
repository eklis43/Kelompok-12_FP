DROP TABLE IF EXISTS silver.coupons;
CREATE TABLE silver.coupons AS
SELECT *
FROM bronze.coupons;
