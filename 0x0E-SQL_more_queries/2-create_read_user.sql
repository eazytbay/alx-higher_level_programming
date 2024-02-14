-- Database created in the server
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- This Creates a specific user that has SELECT privileges only
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
