-- List all genres
SELECT tv_genres.name as g, COUNT(tv_show_genres.show_id) as number_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
HAVING number_shows > 0
ORDER BY number_shows DESC;