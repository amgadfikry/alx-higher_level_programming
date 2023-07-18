-- list all records
-- list all records have name
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
