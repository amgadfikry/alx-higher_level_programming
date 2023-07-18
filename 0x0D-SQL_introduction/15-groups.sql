-- script caalculate the dublication
-- statement that get all dublicated score
SELECT score, COUNT(score) AS number FROM second_table
	GROUP BY score
	ORDER BY number DESC;

