CREATE DATABASE healthdb;
USE healthdb;

CREATE TABLE records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    bmi FLOAT,
    bp INT,
    glucose INT,
    heart_rate INT,
    risk INT
);
