"""calling a function inside itself is called recursion"""


#limit of recursion
import sys

i=0 #global variable
print(sys.getrecursionlimit())  # can set the limit more than 1000

def greet():

    global i
    i=i+1
    print("Hellow" ,i)
    greet() 
    # this will call the function greet again and again and it will create an infinite loop and it will give a error called maximum recursion depth exceeded

greet() # calling the function


"""Factorial of a number using recursion 

    n!=nx(n-1)!
    This creates a call stack in memory.

    this resolves backwords:
        
        factorial(5)
        waits for factorial(4)

        factorial(4)
        waits for factorial(3)

        Stores pending calls:

            5 * factorial(4)
            4 * factorial(3)
            3 * factorial(2)
"""

def factorial(n):
    
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) # this is the recursive call