"""
Types of Error 
1. Logical - wrong output
2. Compile time - mostly syntax errors
3. Run time - user input

lets make try exception and finally 
"""

from typing import final


a = 4
b = 2 

try:
    print("resource start")
    print(a/b)
    k = int(input("enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("hey you cant divide a num by 0", e)

except ValueError as e:
    print("invalid input")

except Exception as e:
    print("Something went wrong")

finally:
    print("resourced stop") #executes with or without exception occuring

    