"""ABC MODULE - ABSTRACT BASE CLASSES

A class that only has declaration not a defination is called abstract method and the class which has abstract method  and 
you can't create the object of abstract

"""
from abc import ABC, abstractmethod
from multiprocessing import process

class Computer(ABC):

    @abstractmethod

    def process(self):
        pass

class Laptop(Computer):

    # pass

    def process(self):
        print("it is running")

class Programmer:

    def work(self, com):
        print("solving bugs")
        com.process()

# com = Computer() #TypeError: Can't instantiate abstract class Computer with abstract method process
# com.process()

com1 = Laptop() #TypeError: Can't instantiate abstract class Laptop with abstract method process as there is no method of laptop on it own


prog1 = Programmer()
prog1.work(com1)

