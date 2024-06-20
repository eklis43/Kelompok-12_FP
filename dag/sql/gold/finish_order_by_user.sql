DROP TABLE IF EXISTS gold.finish_order_by_user;
CREATE TABLE gold.finish_order_by_user AS
SELECT 
    c.id AS customer_id,
    c.first_name || ' ' || c.last_name AS fullname,
    c.gender,
    c.address,
    c.zip_code,
    o.id AS order_id,
    o.status,
    o.created_at,
    oi.id AS order_item_id,
    oi.product_id,
    oi.amount,
    oi.coupon_id
FROM 
    silver.customer c
JOIN 
    silver.order o ON c.id = o.customer_id
JOIN 
    silver.order_item oi ON o.id = oi.order_id;
