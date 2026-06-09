""" THREADS

Big task into small tasks 
cpu with multiple tasks

we do time shreading in most os but these days
we have multicore cpu like quad or octa core cpu we run multiple core with multi task

"""
from time import sleep

from threading import *

class Hello(Thread):

    def run(self):
        for i in range(500):
            print("hello")
            sleep(1) #now it will print alternate

class Hii(Thread):

    def run(self):
        for i in range(500):
            print("hii")
            sleep(1) #now it will print alternate

t1 = Hello()
t2 = Hii()

# t1.run()
t1.start()
sleep(0.2) # give a break to avoid colilsion
# t2.run()
t2.start()

# now main makes t1 t2 wait till they are done and then print bye
t1.join()
t2.join()
print("bye") # main thread prints 

#now 3 threads - main, t1, t2

#every execution has 1 thread - the main thread() 
#how we execute 2 threads for hello and hii
# so hello and hii has to be subclass of thread class