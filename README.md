# SQLite Query Optimization

This project demonstrates the impact of adding an index to optimize SQL queries in an SQLite database. The example compares the performance of an unoptimized query with an optimized query using an index on a sample dataset.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Explanation](#explanation)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/sqlite-query-optimization.git
   cd sqlite-query-optimization
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install required packages:**

   There are no additional packages required for this project as it uses Python's built-in `sqlite3` module.

## Usage

1. **Run the script:**

   ```bash
   python optimize.py
   ```

2. **Observe the output in the console:**

   The script will print the duration for both unoptimized and optimized queries.

## Example Output

When you run the script, you might see output similar to the following:

```bash
Unoptimized Query Duration: 0.003000 seconds
Optimized Query Duration: 0.001000 seconds
```

Note: The actual times may vary depending on your system and the state of the database.

## Explanation

### Database Setup

The script creates an SQLite database named `example.db` and a table called `employees` with the following schema:

```sql
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
```

### Sample Data

The script inserts 10,005 sample employee records into the `employees` table. The departments are alternated between 'Engineering' and 'HR', and the salaries are set with a varying pattern.

### Query Execution

The script executes two queries:
1. **Unoptimized Query:**
   ```sql
   SELECT name FROM employees WHERE department = 'Engineering'
   ```
   This query is executed without any indexing.

2. **Optimized Query:**
   An index is created on the `department` column to optimize the query:
   ```sql
   CREATE INDEX IF NOT EXISTS idx_department ON employees (department)
   ```
   The same query is then executed with the index applied.

### Timing

The time taken to execute each query is measured and printed to the console. This demonstrates the performance improvement gained by using an index.
