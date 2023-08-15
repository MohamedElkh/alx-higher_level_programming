-- lists the num of records with the same score in table secondtable in sql server
-- records are ordered by descended count
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
