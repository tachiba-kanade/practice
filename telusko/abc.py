"""ABC MODULE - ABSTRACT BASE CLASSES

A class that only has declaration not a defination is called abstract method and the class which has abstract method  and 
you can't create the object of abstract

"""
from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod

    def process(self):
        pass

com1 = Computer() #TypeError: Can't instantiate abstract class Computer with abstract method process
com1.process()

