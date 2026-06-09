f = open('file_handling', 'w')
# f = open('file_handling', 'r')

f1 = open('file_handling2', 'a') # if you wanna append
f1.write("laptop")
f1.write (" computer")
f1.write (" exit")
f.write("\n for testing file handling, we add a sentence") #it writes , overwrites kind of



"""
  f.write("\n for testing file handling, we add a sentence") #it writes , overwrites kind of
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
io.UnsupportedOperation: not writable

"""
#if i wanna write everything from file_handling to file_handling2


f = open('file_handling', 'r')

for data in f:
    f1.write(data)

