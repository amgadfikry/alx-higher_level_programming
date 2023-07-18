-- script max of temperature of state
-- statement get max of temperature in state
SELECT state, MAX(value) AS max_temp FROM temperatures
	GROUP BY state
	ORDER BY state;
