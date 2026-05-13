
""" Filter, map, reduce"""
def is_even(n):
    return n%2==0

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(is_even,nums))
print(evens)



# Using lambda function

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda n: n%2 ==0, nums))
print(evens)

from functools import reduce
def double(n):
    return n*2
doubles = list(map(double, nums))

sum = reduce(lambda a, b: a+b, nums)