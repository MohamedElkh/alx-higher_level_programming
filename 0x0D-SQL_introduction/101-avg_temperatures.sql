-- display the ave temp (in fahrenheit) by city orderd by descen temp
SELECT `city`, AVG(`value`) AS `avg_tempe`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_tempe` DESC;
