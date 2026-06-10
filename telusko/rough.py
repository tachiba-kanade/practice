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

# def print_list(lst):
    
#     for i in lst:
#         return i # loop stops after return 
    
# lst = [5,6,7,8]
# print(print_list(lst))

# from random import randint
# def arr_ran(x):
#     c = randint(0,9)
#     print(c)

# arr_ran(7)

# def add(a, *b):
    
#     print(type(a),type(b))

# add(5, 6, 7, 8)


# tup = (4,6)
# a,b = tup
# print(a,b)
# print(tup,type(tup))


# swapping 2 values using XOR
# a = 9
# b = 7
# print(a,b)
# a = a^b # 9 ^ 7
# b = a^b # (9 ^ 7) ^7 = 9
# a = a^b # (9 ^ 7) ^9 = 7
# print(a,b)

# class Student:

#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2

#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)

#         return s3
       
#     def __gt__(self, other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2

#         if r1 > r2:
#             return True
#         else:
#             return False
        
#     def __str__(self):
#         return self.m1, self.m2

# s1 = Student(34, 66)
# s2 = Student(45, 55)

# s3 = s1+s2 #TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
# print(s3.m1)
# # as the compiler doesnt know what to do

# if s1 > s2 :  # so if you want to perform any operations on the objects, you have define all these methods
#     print("s1 wins")
# else:
#     print("s2 wins")



# print(s1) #: __str__ returned non-string (type tuple)
# unlike a = 9 printing values object print address calls __str__ module address so here over riding the method works
# print(s1.__str__())
# so now s1 will give tupless(value) as method is defined
#

# class Menu:

#     def __init__(self):
#         self.nums = input('ENTER THE LIST OF NUMBERS TO OPERATE ON: ').split(',')
#         self.show_menu() 

#     def add(nums):
#         for i in range in nums:
#             i=+i
#         print("result: ", i)

#     def remove(nums):
#         lst =[]
#         lst = input("enter the numbers you want to remove , separted:").split(',')


#     def sort():
#         pass

#     def show_menu():
        
#         while True(): 
#             print("\n=== MAIN MENU ===")
#             print("1. ADD")
#             print("2. REMOVE")
#             print("3. SORT")
#             print("4. EXIT")

#             choice = input("Enter your choice (1-4): ")

#             if choice =='1':
#                 add()

#             elif choice =='2':
#                 remove()

#             elif choice == '3':
#                 sort()

#             elif choice == '4':
#                 print("YOU EXITED DON'T COME BACK")
#                 break
#             else:
#                 print("UH OHH, WRONG CHOICE BITCH, TRY AGAIN")

        

# m1 = Menu()
# m1.show_menu()


def min_calc():

    user_input = int(input("Enter the minutues to be converted: "))
    
    if user_input < 0:
        print("try again, wrong input")
    
    hours = 0
    mins = 0
    day = 0


    if user_input > 1440:
        day = user_input // 1440
        hours = (user_input % 1440)//60
        mins = hours % 60 


    total_seconds = user_input * 60

    print("days:", day)
    print("hours:", hours)
    print("mins", mins)
    print("total seconds", total_seconds)

min_calc()
