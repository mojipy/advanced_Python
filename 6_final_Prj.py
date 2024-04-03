"""



This code takes the car make and model (e.g., Hyundai Tucson) and the number of pages to search
It scrapes https://www.truecar.com/used-cars-for-sale/ to save records containing..
... the cars's type, year, mileage, number of owners and price, and save them in a database
Then it employs the sklearn classifier to train a model using year and mileage as features and price as target
It predicts the price for a sample car and then asks the user to enter a car's year and mileage to predict the price

********* DEVELOPED BY : MOJTABA HASSANZADEH  . . . .  email : mhzaadeh@gmail.com ******************


Author: Mojtaba Hassanzadeh
Date: April 3, 2024
"""



from bs4 import BeautifulSoup
from sklearn import tree
import requests
import re
import mysql.connector

# mySQL connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "moji",
    password = "1234"
)
# create database "mydatabase"
mycursor = mydb.cursor()
mycursor.execute(f"DROP DATABASE IF EXISTS {'mydatabase'}")
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# Initialization of car attributes
mileages = []
prices = []
years = []
types = []
owners = []

# take the car name
car = input('Enter Car Make and Model (Ex: Hyundai Tucson):')
make = car.split()[0].lower()
model = car.split()[1].lower()

# or car, make = input('Enter ...').split()

pgs = int(input('How many pages do you want to search?'))

for page in range (1,pgs+1): # pages range for scraping
    # defining the urls
    url = 'https://www.truecar.com/used-cars-for-sale/listings'+'/'+make+'/'+model+'/'+'?page='+ str(page)

    # request
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Finding mileage
    # <div class="truncate text-xs" data-test="vehicleMileage"><svg viewBox="0 0 24 24" class="icon icon-before icon-fill-default vehicle-card-icon" aria-hidden="true" style="width: 16px; height: 16px;"><use href="#speed"></use></svg>3,671 miles</div>
    mile_pattern = r'(\d+,*\d*)<!-- --> miles'
    mileages.append(re.findall(mile_pattern, r.text))

    # Finding price and year
    # <div class="linkable card card-shadow vehicle-card" aria-label="View details for 2022 Hyundai Tucson, SEL FWD - MSRP: $19,598" data-test="usedListing" data-test-item="5NMJB3AE0NH080823" data-test-dealerid="38634">
    price_matches = []
    year_matches = []
    price_pattern = r'\$\S+'
    year_pattern = r'\b\d{4}\b'
    price_elements = soup.find_all(class_="linkable card card-shadow vehicle-card")
    for i in range(len(price_elements)):
        aria_label = price_elements[i]['aria-label']
        price_matches.append(re.findall(price_pattern, aria_label))
        year_matches.append(re.findall(year_pattern, aria_label))

    prices.append([item[0] for item in price_matches])
    years.append([item[0] for item in year_matches])

    # Finding car type
    # <div class="truncate text-xs" data-test="vehicleCardTrim">Hybrid SEL Convenience AWD</div>
    car_type_elements = soup.find_all("div", class_="truncate text-xs", attrs={"data-test": "vehicleCardTrim"})
    types.append([element.text.strip() for element in car_type_elements])

    # Finding the number of owners
    # <div class="vehicle-card-location mt-1 text-xs" data-test="vehicleCardCondition"><svg viewBox="0 0 24 24" class="icon icon-before icon-fill-default vehicle-card-icon" aria-hidden="true" style="width: 16px; height: 16px;"><use href="#directions_car"></use></svg>No accidents reported, 0 Owners</div>
    owners_pattern = r'[No|\d]\saccident[s]* reported,\s(\d+)\sOwner[s]*'
    owners.append(re.findall(owners_pattern, r.text))

# converting the list-of-lists to lists
years = [item for sublist in years for item in sublist]
types = [item for sublist in types for item in sublist]
prices = [item for sublist in prices for item in sublist]
mileages = [item for sublist in mileages for item in sublist]
owners = [item for sublist in owners for item in sublist]

# insert data in the table "cars"
mycursor.execute("USE mydatabase")
mycursor.execute("CREATE TABLE cars (year VARCHAR(255), type VARCHAR(255), mileage VARCHAR(255), owners VARCHAR(255), price VARCHAR(255))")
insert_query = "INSERT INTO cars (year, type, mileage, owners, price) VALUES (%s, %s, %s, %s, %s)"

for j in range(len(prices)):
    insert_data = [years[j], types[j], mileages[j], owners[j], prices[j]]
    mycursor.execute(insert_query, insert_data)
    mydb.commit()

# show the table Records
# creating features and target for training
mycursor.execute("SELECT * FROM cars")
myresult = mycursor.fetchall()

x = []
y = []

print('***********************************************************')
print(f'SEARCH COMPLETED OVER {pgs} PAGES')
print(f'{len(prices)} RECORDS SAVED IN DATABASE')
print('***********************************************************')
# show the first 3 records
n = 1
for z in myresult[0:3]:
    print('\nRecord '+ str(n) + ':')
    print('   year:', z[0])
    print('   type:', z[1])
    print('   mileage:', z[2])
    print('   owners:', z[3])
    print('   price:', z[4])
    n += 1
print('.')
print('.')
print('.')
# show the last 3 records
n = len(prices)-2
for z in myresult[-3:]:
    print('\nRecord '+ str(n) + ':')
    print('   year:', z[0])
    print('   type:', z[1])
    print('   mileage:', z[2])
    print('   owners:', z[3])
    print('   price:', z[4])
    n += 1

    # features(x): [year, mileage]
    # target(y): [price]
    x.append([int(z[0]), int(z[2].replace(',', ''))])
    y.append(float(z[4].replace('$', '').replace(',', '')))

# train and fit    
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

print('***********************************************************')
print(f'MODEL TRAINED BY {len(years)} EPOCHs')
print('Features : year and mileage')
print('Target : price')
print('***********************************************************')

# predicting the price using fitted model 

new_data = [[2022, 122000]] # array of arrays
answer = clf.predict(new_data)
print(f'Predicted price for year = {new_data[0][0]} and mileage = {new_data[0][1]} is ${answer[0]}')

while input('Do you want to predict more? (y/n)') == 'y':
            year = input('Enter the year: ')
            mileage = input('Enter the mileage: ')
            new_data = [[year, mileage]] 
            answer = clf.predict(new_data)
            print(f'Predicted price for year = {new_data[0][0]} and mileage = {new_data[0][1]} is ${answer[0]}')
