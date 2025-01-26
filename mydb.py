import mysql.connector

# Connect to the MySQL server
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

# Create a cursor object
cursorObject = database.cursor()

# Execute the SQL query to create the database
cursorObject.execute("CREATE DATABASE elderco")

# Commit the changes
database.commit()

# Print success message

print("Database created successfully")
