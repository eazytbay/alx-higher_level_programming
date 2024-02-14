-- Here is what this script does 
-- It Display records from two tables with a matching field
SELECT s.name
    FROM tv_genres s
    INNER JOIN tv_show_genres b
        ON s.id = b.genre_id
    INNER JOIN tv_shows c
        ON c.id = b.show_id
    WHERE c.title = 'Dexter'
    ORDER BY s.name ASC;
