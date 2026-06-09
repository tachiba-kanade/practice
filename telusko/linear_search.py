pos = -1
def search(lst, n):
    i = 0
    for i in range (len(lst)):
        if lst[i] == n:
            globals()['pos'] = i
            return True
    else:
        return False

lst = [3, 4, 5, 5, 7, 8, 9, 10, 45, 34, 33]
n = 10

if search(lst, n):
    print("found at", pos+1)
else:
    print("not found")



