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
time in hours and mins - in the format  output should be exact 25 years 6 months data till milliseconds 


strftime()- Returns a string representation of the DateTime object with the given format

strptime()- Returns a DateTime object corresponding to the date string

Concept
Take DOB from the user.
Get the current date and time.
Calculate the difference between current date-time and DOB.
Convert the difference into:
Years
Months
Days
Hours
Minutes
Seconds
Milliseconds
Display the result.

"""

from datetime import *

    
def cal_dob():
    dob = input( "Enter the DOB in format dd/mm/yyyy: ").split('/')
    dob_day = int(dob[0])
    dob_month = int(dob[1])
    dob_year = int(dob[2])

    now = datetime.now()
    current_day = now.day
    current_month = now.month
    current_year = now.year

    diff_year = current_year - dob_year 
    if current_month - dob_month>0:
        diff_month = current_month - dob_month
    else:
        diff_month=+12
    
    if current_day - dob_day>0:
        diff_day = current_day - dob_day
    else:
        diff_day=+30

    print(f"current_age is: {diff_day}/{diff_month}/{diff_year}")
    

cal_dob()



