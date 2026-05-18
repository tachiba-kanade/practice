"""What is a Module
A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.
import a function from a modile and rename it.

in-builts like os , sys

1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
2. Write a function which returns an array of seven random numbers in a range of 0-9. 
All the numbers must be unique.

Using random.sample()
If we don't want to modify the original list then use random.sample() to generate a shuffled copy. This method returns a new list with shuffled elements.


"""

# from random import shuffle
""" 
from random import random, shuffle 
def shuffle_list(lst): 
    return random.shuffle(lst)

lst =[2,3,4,5,6,7,5,4] 
print(shuffle_list(lst))

i imported random as a function, not as the random module.
random   # a function that gives a random float
shuffle  # a function that shuffles a list

So i should have called:
shuffle(lst)

not:
random.shuffle(lst)

Also, shuffle() modifies the list in place and returns None.
So this:
return shuffle(lst)

will still print:
None

because shuffle() does not return the shuffled list.

"""

import random

def shuffle_list(lst): 
    
    return random.shuffle(lst) 
    # its returning random not shuffle(lst)
    # so now return gives a random float amd doesnt return the shuffle

lst =[2,3,4,5,6,7,5,4]
print(shuffle_list(lst))

# correct version
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

lst = [2, 3, 4, 5, 6, 7, 5, 4]
print(shuffle_list(lst))


#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
from random import randint
def arr_ran(x):
    res =[]
    while len(res) < x:
        n = randint(0, 9)

        if n not in res:
            res.append(n) # adding only if it doesnt exsist

    return res

print(arr_ran(7))