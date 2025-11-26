# Write you from Queries
-- select query_name, 
-- Round(sum(rating/position)/count(*),2) as quality, 
-- Round(sum(case when rating < 3 then 1 else 0 end)* 100/count(*),2) as poor_query_percentage
-- from queries
-- order by query_name;

SELECT 
    query_name,
    ROUND(SUM(rating / position) / COUNT(*), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) 
        AS poor_query_percentage
FROM Queries
GROUP BY query_name;
