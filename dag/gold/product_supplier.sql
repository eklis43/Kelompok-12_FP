DROP TABLE IF EXISTS gold.product_supplier;
CREATE TABLE gold.product_supplier AS
WITH product_count AS (
    SELECT 
        s.name AS supplier_name,
        p.price_label,
        COUNT(*) AS product_count
    FROM 
        silver.product p
    JOIN 
        bronze.supplier s
    ON 
        p.supplier_id = s.id
    GROUP BY 
        s.name, p.price_label
)
SELECT 
    supplier_name,
    MAX(CASE WHEN price_label = 'Cheap' THEN product_count ELSE 0 END) AS cheap_count,
    MAX(CASE WHEN price_label = 'Medium' THEN product_count ELSE 0 END) AS medium_count,
    MAX(CASE WHEN price_label = 'expensive' THEN product_count ELSE 0 END) AS expensive_count
FROM 
    product_count
GROUP BY 
    supplier_name
ORDER BY 
    supplier_name;
