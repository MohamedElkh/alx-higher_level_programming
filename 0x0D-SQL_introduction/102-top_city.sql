-- display 3 cities with highest avg temp between month 7 and 8
SELECT `city`, AVG(`value`) AS `avg_tempe`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_tempe` DESC
LIMIT 3;
