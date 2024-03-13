"""
Working with database
SQL



Author: Mojtaba Hassanzadeh
Date: March 13, 2024
"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "moji",
    password = "1234",
    ssl_disabled = True  # Disable SSL  ... Details at the end
)

mycursor = mydb.cursor()

mycursor.execute(f"DROP DATABASE IF EXISTS {'mydatabase'}")
# OR mycursor.execute('DROP DATABASE IF EXISTS mydatabase')
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("USE mydatabase")

mycursor.execute("CREATE TABLE staff (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), Weight INT, Height INT)")
# sql_query = "CREATE TABLE tablename (column1 datatype, column2 datatype, ...)"

insert_query = "INSERT INTO staff (name, Weight, Height) VALUES (%s, %s, %s)"
# VALUES (%s, %s, %s): This part specifies the values to be inserted into the respective columns. 
# The %s placeholders are parameterized placeholders indicating that the actual values will be supplied later using a tuple or list.
# even though %s is traditionally associated with strings, in the context of database interfaces like MySQL connector in Python, it's a generic placeholder for any type of data.

insert_data = [
    ('Amin', 75, 180),
    ('Mahdi', 90, 190),
    ('Mohammad', 75, 175),
    ('Ahmad', 60, 175)
]
mycursor.executemany(insert_query, insert_data)

mydb.commit()

# The commit() method is used to save the changes made to the database. 
# Executing SQL INSERT, UPDATE, DELETE, or CREATE statements, changes are not immediately applied to the database. 
# Instead, they are held in memory until you explicitly commit them using the commit() method.


# show the table
# fetching all records from the "staff" table
mycursor.execute("SELECT * FROM staff")
myresult = mycursor.fetchall()
print("\nBefore sorting:")
for x in myresult:
    print(x)

# Sort by Height (descending), then Weight (ascending)
# fetching all records from the "staff" table and order by ...
mycursor.execute("SELECT * FROM staff ORDER BY Height DESC, Weight ASC")
myresult = mycursor.fetchall()
# print("\nSorted result:")
for x in myresult:
    print(x[1], x[3], x[2])



# raise NotSupportedError("Python installation has no SSL support")
# mysql.connector.errors.NotSupportedError: Python installation has no SSL support

# This error occurs because the MySQL connector is trying to establish a secure connection using SSL, 
# but your Python installation doesn't have SSL support enabled.
# you have a few options:
# - Enable SSL Support:
# - connect to MySQL without SSL. To do this, you can specify ssl_disabled=True in