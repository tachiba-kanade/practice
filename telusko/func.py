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

def update(lst):
    print(id(lst)) # this will print the memory address of the list lst
    lst[1]=7
    print(lst) 

lst = [1, 2, 3]
print(id(lst)) # this will print the memory address of the list lst
update(lst) # when we pass the list lst to the function update, we are passing the reference of the list lst to the function update meaning the address of the list lst is passed to the

#output :
# 4377187648
# 4377187648
# [1, 7, 3]


"""
Lists are passed by reference.

Integers, Strings are passed by value.

This is a simplification and is not how Python works.

The more accurate statement is:

Python passes object references to functions (sometimes called pass-by-object-reference or pass-by-sharing).
If the object is mutable (list, dictionary, set), modifying the object affects everyone referencing it.
If the object is immutable (int, float, string, tuple), you cannot modify the object. Any "change" creates a new object, so the caller sees no change.

Argument passed
        │
        ▼
Function parameter gets a reference
        │
        ▼
Can the object itself be modified?

YES (list, dict, set)
    ↓
Original object changes

NO (int, float, str, tuple)
    ↓
A new object is created instead

"""

""" TYPES OF ARGUMENTS : formal and actual
under actual there are 4 types of arguments :
    Positional arguments
    Keyword arguments
    Default arguments
    Variable length arguments
"""

# def add(a, b):
#     c= a + b
#     print(c)

# add(7,8) 

def person(name, age):
    print("Name:", name)
    print("Age:", age)

person("Sudha", 25)
# here "Sudha" and 25 are positional arguments because they are passed in the same order as the parameters name and age in the function definition
person(age=25, name="Sudha") 
# here name and age are keyword arguments because we are passing the arguments in the form of key=value pairs and we can pass the arguments in any order
person("Sudha")

def person(name, age=18): # here age is a default argument because it has a default value of 18. if we don't pass any value for age, then it will take the default value of 18 else override
    print("Name:", name)
    print("Age:", age)

person("Sudha")

"""Keyworded length variable arguments - **kwargs, *kwargs

 there is a undefined number of arguments that we can pass to a function. for that we use variable length arguments. 
     there are 2 types of variable length arguments :  
     1. *args - it is used to pass a variable number of non keyword arguments to a function. it is treated as a tuple inside the function.
     2. **kwargs - it is used to pass a variable number of keyword arguments to a function. it is treated as a dictionary inside the function. """


def add(a, *b):
    c= a+b
    print(c)
add(5, 6, 7, 8) # so you defined a as 5 and b as (6, 7, 8) which is a tuple. 
# so when you add a and b, it will concatenate the integer 5 with the tuple (6, 7, 8) and it will give you the output as (5, 6, 7, 8)

def add(a, *b):
    c = a
    for i in b:
        c += i
    print(c)

add(5, 6, 7, 8)

#**kwargs example - passing multiple args with keywords

def person(**data):
    for key, value in data.items():
        print(key,":", value)


person(name='sudha', age=25, state='odisha', job='python developer', pincode=751030) # here we are passing 4 arguments to the function person but we have not defined any parameters in the function person. so we can use **kwargs to handle this situation.

"""PASS LIST TO A FUNCTION
count even and odd numbers in a list"""

def count(lst):

    even = 0
    odd = 0 
    for i in lst:
            if i%2==0:
                even = even + 1
            else:
                odd = odd + 1  
    return even, odd

lst = [3,5,6,50,67,80,23,45,67,90,22]
even, odd = count(lst)
print(f"Even: {even} and odd: {odd}")


"""FIBONACCI SEQUENCE"""

def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

n = int(input("Enter the number you want to go: "))
fibonacci(n)


"""Factorial of a number

    Iterative / Normal Loop Version
    Instead of breaking the problem into smaller factorials,
    it directly multiplies numbers one by one.

    f = 1

    f = 1 * 1 = 1
    f = 1 * 2 = 2
    f = 2 * 3 = 6
    f = 6 * 4 = 24
    f = 24 * 5 = 120

    Uses constant memory
    Iterative

    Only keeps: f and i
    Much less memory.
"""

def factorial(n):
    f=1
    for i in range(1,n+1):
        f= f*i
        print(f)

n = int(input("Enter the number: "))
factorial(n)