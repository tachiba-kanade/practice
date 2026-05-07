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