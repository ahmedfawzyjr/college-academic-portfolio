CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    dept_id INT
);

INSERT INTO Employees VALUES (1, 'Alice', 75000), (2, 'Bob', 60000), (3, 'Charlie', 82000);

SELECT dept_id, AVG(salary) AS avg_salary, COUNT(*) AS total_employees
FROM Employees
GROUP BY dept_id
HAVING AVG(salary) > 50000;
