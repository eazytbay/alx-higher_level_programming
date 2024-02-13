-- This is a script that converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0
   CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Effects changes in  the properties of a table in the database
USE hbtn_0c_0;
ALTER TABLE first_table
   CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
