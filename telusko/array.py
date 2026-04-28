# array in python with no base size you can add as many elements as you want or remove but it should be of same type else same as list
"""INTRODUCTION TO ARRAY IN PYTHON"""
from array import *
import array as arr

from matplotlib.pylab import f

#type code
# 'i' for integer
# 'f' for float example arr1 = array('i', [1, 2, 3, 4, 5])


#list of type code
# 'b' - signed char -int - 1
# 'B' - unsigned char - int - 1
# 'u' - Unicode character - int - 2
# 'h' - signed short  - int - 2
# 'H' - unsigned short  - int - 2
# 'i' - signed int - int - 4
# 'I' - unsigned int - int - 4
# 'l' - signed long - int - 4
# 'L' - unsigned long - int - 4
# 'q' - signed long long - int - 8
# 'Q' - unsigned long long - int - 8
# 'f' - float - float - 4
# 'd' - double - float - 8

vals = array('i',[1,2,3,4,5]) #cant be -ve or decimal
print(vals)
print(vals.buffer_info()) # gives the address and size of the array
print(vals.typecode) # gives the type code of the array
vals.reverse() 



# for charecters array

vals1 = array('u',['a','b','c','d','e']) # cant be int or float

for e in vals1:
    print(e)

# suppose you donot know the type or values from vals1 then you can use type code to find the type of array and then you can use that type code to find the type of values in the array

vals = array('i',[1,2,3,4,5])
newArr = array(vals.typecode, [e for e in vals]) # one one values from vals and assign to the newArr
print(newArr)

""" 2. INSERTING AND DELETING ELEMENTS IN ARRAY AND SEARCHING ELEMENTS IN ARRAY """

# from user , we ask user to enter the number of elements in the array and then we ask user to enter the elements in the array and then we ask user to enter the element to be searched in the array and then we search for that element in the array and if found we print the index of that element in the array else we print element not found

from array import *
arr = array('i', [])
# so ask the user how many it wants in that array so that the loops run
n = int(input( "enter the length of the array: "))
#now when you ask for the next elements in 
for i in range(5):
    x = int(input("enter the element: "))
    arr.append(x) # append is used to add elements in the array
print(arr)