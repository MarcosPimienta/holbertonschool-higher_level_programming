#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number

if number < 0:
    ld = n % -10
else:
    ld = n % 10
if ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, ld))
elif ld < 6 and ld != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, ld))
else:
    print("Last digit of {} is {} and is 0".format(n, ld))
