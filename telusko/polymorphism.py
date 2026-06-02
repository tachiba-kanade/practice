"""OBJECTS WITH MULTIPLE BEHAVIOR - MANY FORMS

- Loose Coupling
- Dependency Injection
- interface

4 ways to implement ploymorphisim

> DUCK TYPING
> OPERATOR OVERLOADING
> METHOD OVERLOADING
> METHOD OVERINDING

"""


# DUCK TYPING - WALKS LIKE DUCK, QUACKS LIKE DUCK, SWIMS LIKE A DUCK ?
# DOESNT MATTER IF ITS ANOTHER BIRD BUT IT BEHAVE LIKE DUCK --- IT IS A DUCK!!!!! ITS THE DUCK TEST

x = 5 # we have the dynamic typing here memory type <int> 

# theres a obj of type integer named X - just name theres not type of x, the value it is refered to has a type here its int

x = 'Sudha' # here memory type <string>


class Pycharm:

    def execute(self):
        print("COMPILING")
        print("RUNNNING")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
class Laptop:

    def code(self, ide):
        ide.execute() # now can call the method in another class

ide = Pycharm() #create object of pycharm
lap1 = Laptop()# pass explicit arg in obj of another to access
lap1.code(ide)



""" OVERLOADING """

a = 7
b = 8 
print(a+b)
print(int.__add__(a,b))

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3
       
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{}{}'.format(self.m1, self.m2) # we convert it to string now by changing the format


s1 = Student(34, 66)
s2 = Student(45, 55)

s3 = s1+s2 #TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
print(s3.m1)
# as the compiler doesnt know what to do

if s1 > s2 :  # so if you want to perform any operations on the objects, you have define all these methods
    print("s1 wins")
else:
    print("s2 wins")

print(s1) # unlike a = 9 printing values object print address calls __str__ module address so here over riding the method works
print(s1.__str__())
# so now s1 will give tupless(value) as method is defined
# operators same but operand different thats overloading, same method name but args are diff
 

"""OVERIDDING"""

class A:

    def show(self):
        print("in A show")
class B(A):
    
    def show(self):
        print("in B show") # now it will print this not a one. thats overidding

a1 = B()
a1.show() # in A show. It inherited as it didnt have its own show()





