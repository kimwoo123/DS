CREATE TABLE IF NOT EXISTS customers AS 
WITH combined_data AS (
    SELECT * FROM data_2022_dec
    UNION ALL
    SELECT * FROM data_2022_nov
    UNION ALL
    SELECT * FROM data_2022_oct
    UNION ALL
    SELECT * FROM data_2023_feb
    UNION ALL
    SELECT * FROM data_2023_jan
)
SELECT * FROM combined_data;