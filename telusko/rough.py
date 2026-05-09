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

""" TYPES OF ARGUMENTS : formal and acual
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

# there is a undefined number of arguments that we can pass to a function. for that we use variable length arguments. 
    # there are 2 types of variable length arguments :  
    # 1. *args - it is used to pass a variable number of non keyword arguments to a function. it is treated as a tuple inside the function.
    # 2. **kwargs - it is used to pass a variable number of keyword arguments to a function. it is treated as a dictionary inside the function.


def add(a, *b):
    c= a+b
    print(c)
add(5, 6, 7, 8) # so you defined a as 5 and b as (6, 7, 8) which is a tuple. 
# so when you add a and b, it will concatenate the integer 5 with the tuple (6, 7, 8) and it will give you the output as (5, 6, 7, 8)

