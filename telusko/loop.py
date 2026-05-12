"""Loops for Everyone

EXTRAS HERE:
if / elif / else
for loop
while loop
break
continue
for...else
while...else
nested loops
range()
enumerate()
logical operators: and, or, not
membership operators: in, not in
comparison operators
truthy / falsy values
match-case
list comprehension

"""

#1. While Loop - it's conditional
i = 0
while i < 5:
    print(i)
    i=i+1

# Output:
# 0
# 1
# 2
# 3
# 4



#2. For Loop - it's Iterative for sequences for list, tuple, string
# range() creates a sequence of numbers.
# This loop starts from 11, stops before 20, and jumps by 2.
for i in range(11, 20, 2):
    print(i)


# Output:
# 11
# 13
# 15
# 17
# 19

