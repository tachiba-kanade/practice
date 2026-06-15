"""should be sorted before

[4, 7, 8, 12, 45, 99]

search: 45
5/2 = mid 2.5 ~ = 2

value at (2) = 8  is it = 45 no lower or upper?
now mid value is the upper bound

There is 3 ways to solve 
1. iterative
2. recursive
3. native

"""

#iterative method - best

pos = -1

def binary_search(list, n):

    lower_bound, upper_bound = 0, len(list)-1

    mid 

   

list = [3,5,6,7,8,9,19,29,45,78,89,90,98,101,1000,1234]
n= 101


if binary_search(list, n):
    print("Found at ",pos+1)
else:
    print("not found")


