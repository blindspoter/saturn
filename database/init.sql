/*create test dababase user */;
GRANT USAGE ON *.* TO 'saturn'@'localhost' IDENTIFIED BY 'saturn' WITH GRANT OPTION;
GRANT USAGE ON *.* TO 'saturn'@'%' IDENTIFIED BY 'saturn' WITH GRANT OPTION;

FLUSH PRIVILEGES;

/*create dababase */;
DROP DATABASE IF EXISTS `saturn`;
CREATE DATABASE `saturn`;

GRANT ALL privileges ON athena.* to 'saturn'@'%';
GRANT ALL privileges ON athena.* to 'saturn'@'localhost';
FLUSH PRIVILEGES;
