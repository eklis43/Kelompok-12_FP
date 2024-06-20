DROP TABLE IF EXISTS gold.login_by_user;
CREATE TABLE gold.login_by_user AS
SELECT 
  first_name || ' ' || last_name AS fullname,
  la.attempted_at
FROM silver.login_attempts la
JOIN silver.customer c ON la.customer_id = c.id
ORDER BY fullname, la.attempted_at;
