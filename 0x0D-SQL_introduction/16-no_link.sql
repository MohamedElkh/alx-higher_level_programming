-- lists all records of the table secondtable have name value in sql server
-- records are ordered by descended score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
