-- Here is what this script does 
-- It creates a table called "unique_id"
-- This table has a unique id attribute
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
