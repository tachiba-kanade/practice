""" Decorators """

from importlib import abc


def div(a,b):
    return a/b

div(4,2)
# Decorator is a function that takes another function as an argument and extends the behavior of that function without explicitly modifying it.

# so whats the difference between passing function as a parameter and decorator
# it just decorates things, makes it pretty


def smart_div(func):

    def smaller_div(a,b):
        if a<b:
            a,b = b,a

        return func(a,b)
    return smaller_div

div = smart_div(div)
div(2,4)


#example 

def simple_decorator(func):
    def wrapper(name):
        print("Before the function call")
        # Call the original function and store the result
        say = func(name)
        print("After the function call")
        # Return the result
        return say
    return wrapper

@simple_decorator
def say_hello(name):
    print("Function being excuted")
    return f"Hello {name}!"

# Call the decorated function
print(say_hello('Babuska'))
