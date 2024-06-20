DROP TABLE IF EXISTS silver.login_attempts;
CREATE TABLE silver.login_attempts AS
SELECT *
FROM bronze.login_attempts
