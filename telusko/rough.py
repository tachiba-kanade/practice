from matplotlib.pylab import f

# def fibonacci(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)

# n = int(input("Enter the number you want to go: "))
# fibonacci(n)


# """Factorial of a number"""

# def factorial(n):
#     f=1
#     for i in range(1,n+1):
#         f= f*i
#         print(f)

# n = int(input("Enter the number: "))
# factorial(n)



#limit of recursion
# import sys

# i=0 #global variable
# print(sys.getrecursionlimit())  # can set the limit more than 1000

# def greet():

#     global i
#     i=i+1
#     print("Hellow" , i)
#     #TypeError: can only concatenate str (not "int") to str
#     greet() 
#     # this will call the function greet again and again and it will create an infinite loop and it will give a error called maximum recursion depth exceeded

# greet() # calling the function

