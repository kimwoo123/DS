SELECT 
    DATE_TRUNC('month', event_time) AS month,
    COUNT(*) AS purchase_count
FROM customers
WHERE event_type='purchase'
GROUP BY month;