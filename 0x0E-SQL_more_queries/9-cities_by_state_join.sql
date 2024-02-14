-- Here is what this script does
-- It lists all cities that are contained in the database hbtn_0d_usa JOINs
SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
        ON cities.state_id = states.id
    ORDER BY cities.id ASC;
