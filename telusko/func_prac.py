"""Exercises: Level 1
1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.

2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

6. Write a function called calculate_slope which return the slope of a linear equation

7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]

10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

Exercises: Level 2

16. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
17. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
18. Call your function is_empty, it takes a parameter and it checks if it is empty or not
19. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
20. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
21. Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny

Exercises: Level 3

22. Write a function called is_prime, which checks if a number is prime.
23. Write a functions which checks if all items are unique in the list.
24. Write a function which checks if all the items of the list are of the same data type.
25. Write a function which check if provided variable is a valid python variable
26. Go to the data folder and access the countries-data.py file.
27. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
28. Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order. """ 


#1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.
from calendar import month


def add_two_numbers(a,b):
    return a+b

print(add_two_numbers(5, 10))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14 * r ** 2
area = area_of_circle(5)
print("area of the circle is :", area)

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for i in args:
        if type(i) ==int or type(i) == float:
            sum = sum + i
        else:
            print(i, "is not a number")
    return sum

print(add_all_nums(1, 2, 3, 4, 5.4, "hello", [1, 2, 3]))

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temp_f = convert_celsius_to_fahrenheit(25)
print("Temperature in Fahrenheit is :", temp_f)

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(m):
    m = m.capitalize() # this will capitalize the first letter of the month and make the rest of the letters lowercase. so if the user enters "september" or "SEPTEMBER" or "SePteMBeR", it will be converted to "September" and it will match with the list of months in the if condition.  
    if m in ["September", "October", "November"]:
        return "Autumn"
    elif m in ["December", "January", "February"]:
        return "Winter"
    elif m in ["March", "April", "May"]:
        return "Spring"
    elif m in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Invalid month"

    
month = input("Enter the month: ")
season = check_season(month)
print("Season is :", season) 

# 6. Write a function called calculate_slope which return the slope of a linear equation
"""(\(y = mx + b\)), where \(m\) is the slope. 
Alternatively, use the formula \(m = \frac{y_2 - y_1}{x_2 - x_1}\) with two points \((x_1, y_1)\) and \((x_2, y_2)\) on the line"""

def cal_slope():
    pass

user = input("Enter the linear equation in the form y = mx + b: ")
slope = cal_slope(user)








