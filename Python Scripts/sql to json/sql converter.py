import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('towncraft.db')
cursor = conn.cursor()

# Execute a SQL query to retrieve data
cursor.execute('SELECT * FROM averagedistance')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Convert data to JSON format
data = []
for row in rows:
    data.append({
        'column1': row[0],
        'column2': row[1],
        # Add more columns as needed
    })

# Write JSON data to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Close the database connection
conn.close()
