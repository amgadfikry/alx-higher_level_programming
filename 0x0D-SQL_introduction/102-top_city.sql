-- script get average of temperature of city in specific months
-- statement get average of temperature in specific months
SELECT city, AVG(value) AS avg_temp FROM temperatures
	GROUP BY city
	HAVING month = 7 AND month = 8
	ORDER BY avg_temp DESC
	LIMIT 3;
