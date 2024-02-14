-- iHere is what this script does 
-- It creates both database hbtn_0d_usa and the table states 
-- respectivelty (in the database hbtn_0d_usa) on your M-- ySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id)
);
