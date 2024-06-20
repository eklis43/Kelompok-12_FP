DROP TABLE IF EXISTS gold.gender_product_category;
CREATE TABLE gold.gender_product_category AS
WITH customer_product_category AS (
    SELECT 
        c.gender,
        pc.name AS product_category
    FROM 
        silver.customer c
    JOIN 
        bronze.order o ON c.id = o.customer_id
    JOIN 
        bronze.order_item oi ON o.id = oi.order_id
    JOIN 
        silver.product p ON oi.product_id = p.id
    JOIN 
        bronze.product_category pc ON p.category_id = pc.id
)
SELECT
    product_category,
    gender,
    COUNT(*) AS product_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY product_category), 2) AS proportion
FROM
    customer_product_category
GROUP BY
    product_category, gender
ORDER BY
    product_category, gender;
