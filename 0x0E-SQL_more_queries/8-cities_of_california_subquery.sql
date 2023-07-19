-- list all citiesof california
-- list all cities without join
SELECT * FROM cities WHERE state_id = (
	SELECT id FROM states WHERE name = 'California');
