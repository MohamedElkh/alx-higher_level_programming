-- lists all records in the table secondtable with score in sql server
-- records are ordered by descended score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
