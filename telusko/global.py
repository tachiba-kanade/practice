"""GLOBAL KEYWORDS IN PYTHON"""

a=10

def func():
    a= 20
    print("local a =", a)

func()
print("global a =", a)