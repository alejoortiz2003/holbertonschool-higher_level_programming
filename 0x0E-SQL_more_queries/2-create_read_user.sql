-- creates the database hbtn_0d_2 and the user user_0d_2.

CREATE DATABASE IF NOT EXISTS hbtn_02_d
CREATE USER IF NOT EXISTS 'user_02_d'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.*
TO 'user_02_d'@'localhost';
FLUSH PRIVILEGES;