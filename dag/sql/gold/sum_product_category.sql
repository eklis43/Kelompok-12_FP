DROP TABLE IF EXISTS gold.sum_product_category;
CREATE TABLE gold.sum_product_category AS
SELECT 
    pc.name AS category_name,
    p.id AS product_id,
    p.name AS product_name,
    p.price,
    p.price_label,
    COUNT(*) OVER (PARTITION BY pc.name) AS product_count
FROM 
    silver.product p
JOIN 
    bronze.product_category pc
ON 
    p.category_id = pc.id
ORDER BY 
    pc.name, 
    p.price;
