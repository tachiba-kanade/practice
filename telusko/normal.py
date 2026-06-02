# x = input("Enter 1st number: ")
# y = input("Enter 2nd number: ")

# z = int(x) + int(y)
# print(z)

# import sys
# ch = input("Enter a character: ")[0]
# print("result: " + ch)


#EXTRAS - TUPPLE DESTRUCTURING
# tup = (4,6)
# a,b = tup
# print(a,b)
# print(tup,type(tup))


#HOW TO MAKE A SINGLE VALUE BE REPRESENTED AS TUPLE

# tup = (4,)
#this will be no longer inteded as intenger



"""Age calculator only with functions and condition
user input with date month year dd/mm/yyyy  
time in hours and mins - in the format  output should be exact 25 years 6 months data till milliseconds """

from datetime import *

def calculator():
    dob = input("Enter DOB (dd/mm/yyyy): ")

    birth_date = datetime.strptime(dob, "%d/%m/%Y")
    current_date = datetime.now()

    # Total difference
    diff = current_date - birth_date

    # Years, months, days (approximate)
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12

    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    milliseconds = diff.microseconds // 1000

    print(f"\nAge:")
    print(f"{years} years {months} months {days} days")
    print(f"{hours} hours {minutes} minutes {seconds} seconds {milliseconds} milliseconds")

    



