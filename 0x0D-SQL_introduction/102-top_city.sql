-- script get average of temperature of city in specific months
-- statement get average of temperature in specific months
SELECT city, AVG(value) AS avg_temp FROM temperatures
	GROUP BY city
	HAVING month = July AND month = August
	ORDER BY avg_temp DESC;
