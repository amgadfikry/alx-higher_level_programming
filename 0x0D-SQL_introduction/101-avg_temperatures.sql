-- script get average of temperature of city
-- statement get average of temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC;
