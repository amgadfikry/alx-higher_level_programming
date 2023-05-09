#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number / 10
temp = int(num) * 10
res = number - temp
if (res > 5):
    print(f"Last digit of {number} is {res} and is greater than 5")
elif (res == 0):
    print(f"Last digit of {number} is {res} and is 0")
else:
    print(f"Last digit of {number} is {res} and is less than 6 and not 0")
