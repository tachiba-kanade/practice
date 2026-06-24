"""INHERITANCE - use the existing features of one class in another

1. Single level A ---> B
2. Multilevel  A ---> B ---> C
3. Multiple  (A,B) ---> C


a. contructor in inheritance
b. MRO - method resolution order
"""


class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("FEATURE 1 - A WORKING")
        
    def feature2(self):
        print("FEATURE 2 WORKING")


""" But what if we want B to call init of BOTH A and B , keyword super is used"""

class B():

    def __init__(self): 
        # when you call the object of Subclass it will call init of Subclass first
        # if you have call Super then it will call init of Superclass first and then call the init of Subclass
        super().__init__()

        print("In B init")
    

    def feature1(self):
        print("FEATURE 1 - B WORKING")

    def feature3(self):
        print("FEATURE 3 WORKING")

    def feature4(self):
        print("FEATURE 4 WORKING")

class C(A,B):
    def __init__(self):
        super().__init__() # MRO ORDER GOES FROM LEFT TO RIGHT ONCE IT SEARCHES For INIT IN C so it will show A as A is at left.
        print("In C init")

    def feat(self):
        super().feature2()
        
# a1 = A()
# b1 = B() # the object of B will still call
#if you create an obj of B (Sub class) first it will try to find the init in B if not then it inherits A' init (Super class)

c1 = C()
c1.feature1()
c1.feat()


# OUTPUT
# In A init
# In C init
# FEATURE 1 - A WORKING


""" 
DOUBT!!!!!!!
if you still have B as subclass of A and try to have multiple inheritance as c it will show the following error:

TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B

"""
