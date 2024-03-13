"""
Working with database
SQL



Author: Mojtaba Hassanzadeh
Date: March 13, 2024
"""
import re
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "moji",
    password = "1234",
    ssl_disabled = True  # Disable SSL  ... Details at the end
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

email_pattern = "^[a-zA-Z0-9_%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$" # RegEX

# take the username(email)
email = input("email: ")
while not re.match(email_pattern, email):
    print("ENTER A STANDARD EMAIL AS: expression@string.string")
    email = input("email: ")

# take the password
passw = input("pass: ")

# select database
mycursor.execute("USE mydatabase")
# create table
mycursor.execute("CREATE TABLE account (username VARCHAR(255), password VARCHAR(255))")
# insert data 
insert_query = "INSERT INTO account (username, password) VALUES (%s, %s)"
insert_data = [
    (email, passw)
]
mycursor.executemany(insert_query, insert_data)

mydb.commit()

# show created table
mycursor.execute("SHOW TABLES")
print('\nTable Name: ')
for x in mycursor:
  print(x)

mycursor.execute("SHOW TABLES FROM mydatabase")

print('\nTable Name: ')
for x in mycursor:
    print(x)



# show the table Records
mycursor.execute("SELECT * FROM account")
myresult = mycursor.fetchall()
print('\nTable Records: ')
for x in myresult:
    print(x,'\n')
    print('\nusername:', x[0])
    print('password:', x[1])




# raise NotSupportedError("Python installation has no SSL support")
# mysql.connector.errors.NotSupportedError: Python installation has no SSL support

# This error occurs because the MySQL connector is trying to establish a secure connection using SSL, 
# but your Python installation doesn't have SSL support enabled.
# you have a few options:
# - Enable SSL Support:
# - connect to MySQL without SSL. To do this, you can specify ssl_disabled=True in