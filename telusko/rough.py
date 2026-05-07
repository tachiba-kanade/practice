from numpy import *


""" 1. FUNCTIONS - Introduction"""


def greet():
    print("Hellow")
    print("Welcome to Python")

greet() # calling the function

""" functions are of 2 types 
1. functions which performs a task
2. functions which returns a value """

def add(a, b): # a and b are parameters/ arguments
    c = a + b
    # print(c)
    return c # return is used to return the value from the function to the caller

add(5, 3) # 5 and 3 are arguments/ actual parameters

# result = add(5, 3)
# print(result)


""" 2. FUNCTIONS - Arguments
       Mutatable and Immutable 

   @modularity - breaking a program into small functions so that it is easy to understand and maintain and debug and also it is easy to reuse the code 
"""