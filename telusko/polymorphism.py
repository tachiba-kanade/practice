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

class Laptop:

    def code(self, ide):
        ide.execute() # now can call the method in another class

ide = Pycharm() #create object of pycharm
lap1 = Laptop()# pass explicit arg in obj of another to access
lap1.code(ide)