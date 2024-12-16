import pyodbc




def saveToDatabase(query, data):


# Define your connection string
connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=your_server;'
    'DATABASE=your_database;'
    'UID=your_username;'
    'PWD=your_password'
)

# Connect to the SQL Server
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Define the SQL insert statement
sql_insert = """
INSERT INTO your_table (column1, column2, column3)
VALUES (?, ?, ?)
"""

# Sample data to be inserted
data = [
    ('value1_1', 'value2_1', 'value3_1'),
    ('value1_2', 'value2_2', 'value3_2'),
    ('value1_3', 'value2_3', 'value3_3'),
    # Add more rows as needed
]

try:
    # Execute the batch insert
    cursor.executemany(sql_insert, data)
    conn.commit()  # Commit the transaction
    print("Batch insert successful.")
except Exception as e:
    print(f"Error occurred: {e}")
    conn.rollback()  # Rollback the transaction in case of error
finally:
    cursor.close()
    conn.close()
