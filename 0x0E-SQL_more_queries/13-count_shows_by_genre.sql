-- lists all geners from database
SELECT g.`name` AS `genre`,
	COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS g
	INNER JOIN `tv_show_genres` AS tt
	ON g.`id` = tt.`genre_id`
GROUP BY g.`name`
ORDER BY `number_of_shows` DESC;
