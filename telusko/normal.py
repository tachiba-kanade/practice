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

def leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if leap(year) else 28

    if month in [4, 6, 9, 11]:
        return 30
    return 31
    
def cal_dob():
    dob = input( "Enter the DOB in format dd/mm/yyyy: ").split('/')
    dob_day = int(dob[0])
    dob_month = int(dob[1])
    dob_year = int(dob[2])

    now = datetime.now()
    current_day = now.day
    current_month = now.month
    current_year = now.year

    if current_day < dob_day:
        current_month -= 1

        if current_month == 0:
            current_month = 12
            current_year -= 1

        current_day += days_in_month(current_month, current_year)

    diff_day = current_day - dob_day

    # Borrow months if needed
    if current_month < dob_month:
        current_month += 12
        current_year -= 1

    diff_month = current_month - dob_month

    diff_year = current_year - dob_year 


    print(f"current_age is: {diff_day}/{diff_month}/{diff_year}")

    
    

cal_dob()



"""
Python Practice Question Set
Topic: Functions, Conditions, Loops, Dictionaries, Date/Time, Basic Maths
Question 1: Exact Age Calculator

Write a Python program that takes the user’s date of birth in this format:

dd/mm/yyyy

Calculate the exact age till the current date and time.

Your output should show:

Years
Months
Days
Hours
Minutes
Seconds
Milliseconds

Example output:

You are 25 years 6 months 12 days 4 hours 30 minutes 20 seconds 450 milliseconds old.

Requirements:

Use functions.
Use strptime() to convert the DOB string into a datetime object.
Use current date and time.
Use conditions to check if the DOB is in the future.
Display proper error messages for invalid input.
-----------------------------------------------------------------------------------------

Question 2: Time Converter
Write a Python program that takes total minutes as input and converts it into:

Days
Hours
Minutes
Seconds

Example:
Input: 1500

Output:
1 day 1 hour 0 minutes
90000 seconds

Requirements:

Use a function.
Use floor division //.
Use modulus %.
Reject negative input using conditions."""

def min_calc():

    user_input = input("Enter the minutues to be converted")
    
    if user_input < 0:
        print("try again, wrong input")


    if user_input > 1440:

        day = user_input // 1440
        mins = user_input % 1440
        if mins > 60:
            hours = mins//60
            remaining_mins = mins%60

    total_seconds = user_input * 60

    print("days:", day)
    print("hours:", hours)
    print("mins", mins)
    print("total seconds", total_seconds)

min_calc()




"""Question 3: Simple Interest Calculator

Write a Python program that takes:

Principal amount
Rate of interest
Time in years

Calculate simple interest using:

SI = (P * R * T) / 100

Also calculate the final amount:

Final Amount = Principal + Simple Interest

Example output:

Principal: ₹10000
Interest: ₹1500
Final Amount: ₹11500

Requirements:

Use a function named calculate_interest.
Use conditions to reject negative values.
Round the result to 2 decimal places.
Question 4: Electricity Bill Calculator

Write a Python program that takes the number of electricity units consumed.

Calculate the bill using this rule:

0 - 100 units      ₹5 per unit
101 - 200 units    ₹7 per unit
Above 200 units    ₹10 per unit

Add a fixed charge of ₹200 to the final bill.

Example:

Input: 250 units
Output: ₹1900

Requirements:

Use functions.
Use conditions.
Reject negative unit input.
Show bill breakdown.
Question 5: Marks Report Card

Write a Python program that takes marks for 5 subjects:

Maths
Science
English
Computer
Social

Store the marks in a dictionary.

Calculate:

Total marks
Average marks
Grade
Pass/Fail result

Grade rules:

90 and above = A
75 to 89 = B
60 to 74 = C
40 to 59 = D
Below 40 = Fail

Requirements:

Use a dictionary.
Use a loop to take marks input.
Use a function to calculate grade.
If any subject mark is below 40, final result should be Fail.
Question 6: Number Analyzer

Write a Python program that takes one number as input.

Check and display whether the number is:

Positive, negative, or zero
Even or odd
Divisible by 3
Divisible by 5
Prime or not prime

Example:

Input: 15

Output:
Positive number
Odd number
Divisible by 3
Divisible by 5
Not a prime number

Requirements:

Use separate functions:
is_even()
is_prime()
is_divisible()
Use conditions.
Handle zero and negative numbers correctly.
Question 7: Shopping Cart Calculator

Write a Python program that asks the user how many items they want to buy.

For each item, take:

Item name
Price
Quantity

Store the item details in a dictionary.

Calculate:

Subtotal for each item
Total amount
Discount
Final amount

Discount rules:

Total above ₹1000 = 10% discount
Total above ₹500 = 5% discount
Otherwise = No discount

Example output:

Rice x 2 = ₹120
Milk x 3 = ₹90

Total = ₹210
Discount = ₹0
Final Amount = ₹210

Requirements:

Use dictionary.
Use loop.
Use function for discount calculation.
Reject negative price or quantity.
Question 8: Password Strength Checker

Write a Python program that takes a password from the user.

Check if the password contains:

At least 8 characters
At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character

Example:

Input: hello123

Output:
Weak Password
Missing: uppercase letter, special character

Requirements:

Use loop.
Use conditions.
Use dictionary to store checks.

Example dictionary:

checks = {
    "uppercase": False,
    "lowercase": False,
    "digit": False,
    "special": False
}
Question 9: ATM Withdrawal System

Write a Python program to create a simple ATM system.

Start with this balance:

balance = 10000

Show this menu repeatedly:

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Rules:

Deposit amount must be positive.
Withdrawal amount must be positive.
Withdrawal amount must not be greater than balance.
Withdrawal amount must be a multiple of 100.
Exit should stop the program.

Requirements:

Use loop.
Use functions:
check_balance()
deposit()
withdraw()
Use conditions.
Display updated balance after deposit or withdrawal.
Question 10: Daily Expense Tracker

Write a Python program that asks the user how many expenses they want to enter.

For each expense, take:

Category
Amount

Example input:

food 200
travel 100
food 150
shopping 500

Store the total amount category-wise using a dictionary.

Example output:

Food: ₹350
Travel: ₹100
Shopping: ₹500

Total Expense: ₹950
Highest Expense Category: Shopping

Requirements:

Use dictionary.
Use loop.
Use function to calculate total expense.
Reject negative amounts.
Find the category with highest expense.
Practice Order

Solve in this order:

1. Time Converter
2. Simple Interest Calculator
3. Number Analyzer
4. Electricity Bill Calculator
5. Marks Report Card
6. Shopping Cart Calculator
7. Daily Expense Tracker
8. Password Strength Checker
9. ATM Withdrawal System



"""