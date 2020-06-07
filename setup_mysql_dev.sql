-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS daily_dev_db;
CREATE USER IF NOT EXISTS 'covid_dev'@'localhost' IDENTIFIED BY 'covid19_dev';
GRANT ALL PRIVILEGES ON `daily_dev_db`.* TO 'covid_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'covid_dev'@'localhost';
GRANT USAGE ON *.*  TO 'covid_dev'@'localhost';
FLUSH PRIVILEGES;
