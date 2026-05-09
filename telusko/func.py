""" FUNCTIONS """


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


syntax:
Declaring a function

def function_name():
    codes
    codes
# Calling a function
function_name() 

"""


def update(x):# here x is a taking a different memory of a 
    x=8 # this will not change the value of x in the main function because x is immutable
    print("x =", x)

# when im calling a function and passing variable a to the function update, then a copy of a is created and passed to the function update. 
# So any changes made to x inside the function will not affect the original variable a outside the function because x is immutable. 
# This is called pass by value.

a=10  
update(a) # here im passing 10 not a. meaning im pasing the value and not the address of a. so a copy of 10 is created and passed to the function update.
print("a =", a) # a will still be 10 because x is immutable

""" pass by reference and pass by value
pass by value - when we pass a variable to a function, 
a copy of the variable is created and passed to the function. 
So any changes made to the variable inside the function will not affect the original variable outside the function.
This is the case with immutable types like int, float, string"""

# in pass by reference - when we pass a variable to a function, the reference of the variable is passed to the function meaning the address of the variable is passed to the function.
# So any changes made to the variable inside the function will affect the original variable outside the function
# This is the case with mutable types like list, dictionary, set


""" BUT PYTHON DOESN'T SUPPORT PASS BY REFERENCE OR PASS BY VALUE. 
IN PYTHON, EVERYTHING IS AN OBJECT AND VARIABLES ARE REFERENCES TO OBJECTS. 
SO WHEN WE PASS A VARIABLE TO A FUNCTION, WE ARE PASSING A REFERENCE TO THE OBJECT, 
NOT THE VALUE OF THE OBJECT. SO ANY CHANGES MADE TO THE OBJECT INSIDE THE FUNCTION 
WILL AFFECT THE ORIGINAL OBJECT OUTSIDE THE FUNCTION, 
REGARDLESS OF WHETHER THE OBJECT IS MUTABLE OR IMMUTABLE """




