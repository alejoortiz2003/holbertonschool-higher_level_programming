#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    n1 = number % 10
    n1 = n1 * -1
    number = number * -1
else:
    n1 = number % 10
if n1 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, n1))
elif n1 == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, n1))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, n1))
