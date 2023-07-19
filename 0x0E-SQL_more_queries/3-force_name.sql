-- create new table
-- create new table that not accept null for name column
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
