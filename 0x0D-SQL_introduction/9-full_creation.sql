-- script create new table that all values
-- statement create table
CREATE TABLE IF NOT EXISTS second_table (
	id int,
	name varchar(256),
	score int
);
-- add new rows to table
INSERT INTO
	second_table (id, name, score)
VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8)	
