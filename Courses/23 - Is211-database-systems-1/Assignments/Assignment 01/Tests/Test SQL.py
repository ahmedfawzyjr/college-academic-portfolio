import sqlite3

def test_sql():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE Employees (emp_id INT, name TEXT, salary REAL, dept_id INT)')
    cursor.executemany('INSERT INTO Employees VALUES (?,?,?,?)', [
        (1, 'Alice', 75000, 10),
        (2, 'Bob', 60000, 10),
        (3, 'Charlie', 82000, 20)
    ])
    cursor.execute('SELECT dept_id, AVG(salary) FROM Employees GROUP BY dept_id')
    rows = cursor.fetchall()
    assert len(rows) == 2
    dept_map = dict(rows)
    assert dept_map[10] == 67500.0
    assert dept_map[20] == 82000.0
    print('Database Systems Assignment 01 Test Passed!')

if __name__ == '__main__':
    test_sql()
