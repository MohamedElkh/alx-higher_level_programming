-- creates sql server with user user_0d_1
-- set a password for user_0d_1_pwd
DROP USER IF EXISTS 'user_0d_1'@'localhost';

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
