CREATE DATABASE source_db;

USE source_db;

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);

INSERT INTO employees (name, age, department)
VALUES
    ('Alice', 30, 'HR'),
    ('Bob', 25, 'Engineering'),
    ('Charlie', 28, 'Marketing');
