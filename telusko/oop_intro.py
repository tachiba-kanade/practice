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
