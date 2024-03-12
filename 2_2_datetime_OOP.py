"""
Object Oriented Programming

This script get the birthdate as:
1995/02/03

and gives the age:

24


Author: Mojtaba Hassanzadeh
Date: March 11, 2024
"""
from datetime import datetime
class Birth:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        self.year = year
        self.month = month
        self.day = day

    def age(self, today):
        if self.year == today.year:
            return 1
        else:
            return today.year-self.year

def main():
    today = datetime.today() # or current_time = datetime.now()
    try:
        birth_date = datetime.strptime(input('Enter birth date (YYYY/MM/DD):'), '%Y/%m/%d')
        if birth_date>today:
           print("WRONG")
        else:
           birth_obj = Birth(birth_date.year, birth_date.month, birth_date.day)
           print(birth_obj.age(today))
    except ValueError:
         print("WRONG !!!")
main()


### This version uses a while True loop to keep asking for input until a valid date is provided. 
# def main():
#     today = datetime.today()
    
#     while True:
#         try:
#             birth_date = datetime.strptime(input('Enter birth date (YYYY/MM/DD): '), '%Y/%m/%d')
#             if birth_date > today:
#                 print("WRONG")
#             else:
#                 birth_obj = Birth(birth_date.year, birth_date.month, birth_date.day)
#                 print(birth_obj.age(today))
#                 break  # Break out of the loop if input is valid
#         except ValueError:
#             print("WRONG !!!")