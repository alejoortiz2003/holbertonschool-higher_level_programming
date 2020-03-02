-- displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending)

SELECT city, AVG(values) AS avg_ temp FROM temperatures WHERE month=7 or month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
