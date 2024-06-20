DROP TABLE IF EXISTS silver.order_item;
CREATE TABLE silver.order_item AS
SELECT *
FROM bronze.order_item
WHERE coupon_id IS NULL;
