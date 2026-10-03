-- 01_university_schema.sql
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gpa DECIMAL(3,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

INSERT INTO Departments VALUES (1, 'Computer Science'), (2, 'Information Systems');
INSERT INTO Students VALUES (101, 'Ahmed', 'Fawzy', 3.85, 1), (102, 'Sara', 'Ali', 3.60, 2);

SELECT s.student_id, s.first_name, s.last_name, d.dept_name, s.gpa
FROM Students s
JOIN Departments d ON s.dept_id = d.dept_id
WHERE s.gpa >= 3.50;
