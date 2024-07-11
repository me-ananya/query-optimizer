import sqlite3
import time

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
''')

# Insert sample data
employees = [
    (1, 'Alice', 'HR', 60000),
    (2, 'Bob', 'Engineering', 75000),
    (3, 'Charlie', 'Sales', 50000),
    (4, 'David', 'Engineering', 80000),
    (5, 'Eve', 'HR', 65000)
]
for i in range(6, 10006):
    department = 'Engineering' if i % 2 == 0 else 'HR'
    salary = 60000 + (i % 1000)
    employees.append((i, f'Employee{i}', department, salary))

cursor.executemany('''
INSERT OR IGNORE INTO employees (id, name, department, salary)
VALUES (?, ?, ?, ?)
''', employees)

conn.commit()

# Function to execute and time a query
def execute_query(query):
    start_time = time.time()
    cursor.execute(query)
    results = cursor.fetchall()
    end_time = time.time()
    return results, end_time - start_time

# Example of an unoptimized query
unoptimized_query = '''
SELECT name FROM employees
WHERE department = 'Engineering'
'''
results, duration = execute_query(unoptimized_query)
print(f"Unoptimized Query Duration: {duration:.6f} seconds")

# Adding an index to optimize the query
cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_department ON employees (department)
''')

conn.commit()

# Example of an optimized query
optimized_query = '''
SELECT name FROM employees
WHERE department = 'Engineering'
'''
results, duration = execute_query(optimized_query)
print(f"Optimized Query Duration: {duration:.6f} seconds")

# Clean up
conn.close()
