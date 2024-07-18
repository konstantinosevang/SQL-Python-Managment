import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    city TEXT
)
''')

# Insert sample data
cursor.execute('''
INSERT INTO employees (first_name, last_name, age, city)
VALUES
    ('John', 'Doe', 30, 'New York'),
    ('Jane', 'Doe', 25, 'Los Angeles'),
    ('Mike', 'Smith', 40, 'Chicago')
''')

# Commit the changes
conn.commit()

# Query the data
df = pd.read_sql_query('SELECT * FROM employees', conn)
print(df)

# Close the connection
conn.close()
