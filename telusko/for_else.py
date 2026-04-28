from math import e


nums = [10, 34, 45, 12, 3, 4, 5]

for num in nums:
    if num%5 == 0:
        print(num)
        break # the loop will stop after finding the first number that is divisible by 5/ only 1 iteration
    else:
        print("Not found")
        # the loop will continue until it finds a number that is divisible by 5/ multiple iterations


