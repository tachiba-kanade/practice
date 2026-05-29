"""python supports oop, functinal and procedural oriented programming

object will have some attribute( properties and data,- as object i know something )  and behaviors( the actions - object i do something)
store something in a object - variables
define the behavior - methods(funcs in oop is called)

object
class
encapsulation
Abstraction
Polymorphisim


so as telsuko said - manifactureres arent imp but the place it is designed is - hence the class is the design the object

class is design (blueprint)
object is the instance (factory the real stuff)

"""

class Computer:
    #we can have attributes - varibales, datas and behaviors- methods
    def config(self):
        print("i5 machine 16gb ram")
    
a = '5' # we used to assign before but we cant do that with com1 as it doesnt have a type , its object of a computer or known as contructutor
com1 = Computer()
print(type(com1)) #<class '__main__.Computer'>
print(type(a)) #<class '__main__.Computer' and class str and its inbuild>

Computer.config() # class name and method TypeError: Computer.config() missing 1 required positional argument: 'self'

# config will change its behavior according to the object

Computer.config(com1)

"""
The logic in creating Classes and its objects are similar to how we work with functions.
·      Remember when we create a function, we 1st define it with a keyword, 2nd assign it with arguments, 3rd give the logic/conditions (we know these as statements) 
        4th return the values and 5th call the function to execute it. 
        In the aforementioned process we have ( : ) colon, which indicates that it's a function and followed by its appropriate 
        indentations.
·      In Classes we have a similar process of syntax, 1st, we create the class by using the keyword class to indicate it's a class,
        2nd followed by the keyword (the name of the class/design) and again the use of ( : )  to indicate that 3rd, 
        it will follow a METHOD (remember from Tutorial 48, Functions in an Object Oriented Programming are called METHODS), 
        4th,  followed by its logic or the condition/statements of the METHOD, i.e. what is it that the METHOD should do?(the actions), 
        5th, after which we CREATE THE VARIABLE (The object) that will be used as the argument in the METHOD of the  CLASS,
        and 6th lastly CALL the Class's Method for execution.
·      For example, we are creating a METHOD through CLASS and assigning HUMANS as variables and when each human is CALLED 
        it will step forward and shout, Hello Sir!

        
        class human(): # Here we have created the CLASS by using the keyword, which is an OBJECT called human
        
            def shout(self): 
            # Here we have defined its METHOD of which the object HUMAN is going to BEHAVE (function), 
            in this example when called they will say Hello Sir!
            ans self is the object you are passing

        print('Hello Sir!') # The statement, i.e. what the VARIABLES are supposed to do when called upon
            ed=human() # Here we created new VARIABLES and assigned them as HUMAN
            dan=human()
            jon=human()

        human.shout(ed) 
        # Here we are calling the CLASS by using its METHOD to pass the ARGUMENT to trigger the ACTION of saying Hello Sir! 
        In other words we are saying; Hey Human, shout Hello Sir, you Ed
        human.shout(dan)
        human.shout(jon)

        jon.shout() 
        # this is another way (a more common way) of CALLING  the CLASS, as you can see we are simply saying -  
        # VARIABLE (ed) followed by the METHOD (shout) the ACTION of Hello Sir! 
        ed.shout()
        dan.shout()

"""


# __init__ special method initialise variable. kind of contructor and it is called for every object

# def __init__(self, *args, **kwargs):
#     print("in init")

class Computer :
    
    def __init__(self, cpu, ram): #now here 3 args are passing (com1,i5,16) com1 passed automatically,
        #now cpu and ram are just vars/args
        print("in init") # will be printed for every object
        self.cpu = cpu
        self.ram =ram

        # now each object will have will have its own cpu and own ram - for both com1 and com2
    def config(self):
        # print("i5, 16 GB RAM, 1 TB")
        print("config", self.cpu, self.ram)

com1 = Computer('i5', 16) #passing 2 variables/ args
com2 = Computer('Ryzen 3', 8 )

com1.cpu = "" # we can change from 1 object to different object

com1.config()
# Computer.config(com1) - another way to call throigh object


"""
CONSTRUCTOR AND SELF

Every time you create an object it will take different memory space(we have heap memory)
the size of the object depends on types of variables number of variables
and who allocates the size of the object - contructor

"""

class Computer:

    def __int__(self):
        self.name = "Sudha"
        self.age = 25

    def update(self):
        self.age = 30

    def compare(self, other): #here self is c1 and other is c2 can be other way around c1 is callling c2
        # the one who is calling it and whom to compare
        if self.age == other.age:
            return True
        else:
            return False

    
c1 = Computer()
c2 = Computer()

#how to compare

if c1.compare(c2):
    print("they are the same")

c1.update()

"""TYPE OF VARIABLES
1. Instance variable
2. class variable (static variable)

"""

#namespace - where you store all instance varibales and class varibales
class Car:
    wheels = 4 #this is a class variable, common for all objects you can use object name and car name
    def __init__(self):
        self.comp= "bmv"
        self.mil= 23.5
        self.eng = "vols"       
# 2 different objects and different varibles these are called instance varibales, they changes according to the object

c1=Car()
c2 = Car()

print(c1.com, c1.mil, c1.wheels)

"""TYPES OF METHOD

1. INSTANCE TYPES - ACCESSOR AND MUTATORS
2. CLASS
3. STATIC

"""

class Student:

    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #INSTANCE METHOD cause we are passing self meaning it belongs to a particular object, so it works with the object(with self keyword)
    # now its 2 types = Accesors and mutators
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self):
        return self.m1
    def set_m1(self, value):
        self.m1 = value
        
    #CLASS METHOD - to work with class variables(work with class keywords)

    @classmethod #decorators

    def info(cls):
        return cls.school
    # STATIC METHOD nothing to vars or class or instance, 

    @staticmethod
    def get_school_name():
        print("this is student class in abc module")

s1 = Student(34, 67, 33)
s2 = Student(45, 56, 89)

#so for calling avg we have to call it like this
s1.avg()
s2.avg()

print(Student.info())

print(Student.get_school_name())

# we cant say Student.avg() as we are not using object there

""" INNER CLASS """

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    
    def show(self):
        print(self.name, self.rollno)



s1 = Student('Babushka', 67)
s2 = Student( 'Bubu', 69)

s1.show()


"""so now i need a details of laptops where the values are just stored or pre-defined maybe 
either i create a class outside or for betterment i creat a class inside"""

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() # created an object of innerclass and can directly this
    
    def show(self):
        print(self.name, self.rollno, self.lap.show())

    class Laptop:

        def __init__(self):
            self.brand = "Apple"
            self.model = "M4 Air"
            self.gb = "16gb"
        
        def show(self):
            print("Heres the config: ", self.brand, self.model, self.gb)



s1 = Student('Babushka', 67)
s2 = Student( 'Bubu', 69)

# theres 2 ways i access the laptop class
# 1. create an object of the inner class inside the outer class
# 2. create the object outside the outerclass but with reference to the outerclass

s1.show()
print(s1.name, s1.rollno, s1.lap) # the object is created inside 

lap1 = Student.Laptop()
lap2 = Student.Laptop() #obj created outside with refernce to outerclass

