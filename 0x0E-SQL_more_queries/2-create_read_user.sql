-- creates the database hbtn_0c_0 in your MySQL server if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the MySQL server user user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant all priviliges to user user_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
