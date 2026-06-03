""" ITERATORS"""


nums = [ 3,4,6,7,8]

it = iter(nums) # it create a pre assigned object 
print(it) #<list_iterator object at 0x100e6dc60>

print(it.__next__()) # 3 just the first then
print(it.__next__()) # 4 and so on

# so we run a loop

for i in nums:
    print(i) # 3 4 6 7 8


"""WHAT ABOUT CREATING MY OWN ITERATOR MY OWN OBJECT?????? meaning now i need my own class"""

class TopTen:

    def __init__(self):
        self.num = 1 # counter variable to start from 1

    def __iter__(self):
        return self
    def __next__(self):

        if self.num <= 10: # it will keep showing NONE
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration # we have to raise exception for this
    
values = TopTen()

for i in values:
    print(i)



"""GENERATORS - Those give you iterators"""