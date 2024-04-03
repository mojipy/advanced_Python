"""
Web Scraping 2

This program retrieves the price and mileage of the first 20 people selling a desired car (the car's name is provided as input) 
from the Truecar website and stores it in a desired database.


Author: Mojtaba Hassanzadeh
Date: March 16, 2024
"""
from bs4 import BeautifulSoup
import requests
import re
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "moji",
    password = "1234"
)
# create database "mydatabase"
mycursor = mydb.cursor()
mycursor.execute(f"DROP DATABASE IF EXISTS {'mydatabase'}")
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# take the car name and define the url
car = input('Enter Car Make and Model (Ex: Hyundai Tucson):')
make = car.split()[0].lower()
model = car.split()[1].lower()
url = 'https://www.truecar.com/used-cars-for-sale/listings'+'/'+make+'/'+model+'/'

# request
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#find top 20 cars mileages
mile_pattern = r'(\d+,\d+)<!-- --> miles'
mile_matches = re.findall(mile_pattern, r.text)


# find top 20 cars prices
price_matches = []
price_pattern = r'\$\S+'
price_elements = soup.find_all(class_="vehicle-card")
for i in range(20):
    aria_label = price_elements[i]['aria-label']
    price_matches.append(re.findall(price_pattern, aria_label))

# insert data in the table "cars"
mycursor.execute("USE mydatabase")
mycursor.execute("CREATE TABLE cars (price VARCHAR(255), mileage VARCHAR(255))")
insert_query = "INSERT INTO cars (price, mileage) VALUES (%s, %s)"
for i in range(20):
    insert_data = [price_matches[i][0], mile_matches[i]]
    mycursor.execute(insert_query, insert_data)
    mydb.commit()

# show the table Records
print('\nTop 20 Used'+' '+ make + ' ' + model + ':')

mycursor.execute("SELECT * FROM cars")
myresult = mycursor.fetchall()
for x in myresult:
    print('\nprice:', x[0])
    print('mileage:', x[1])