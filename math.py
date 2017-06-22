
# universal import -- [from module import*]
# will import a ton of variables and functions

import math

ev = dir(math) # this will show the functions of the math module
print ev

def biggest_number():
    print max(args)
    return max(args)

def smallest_number():
    print min(args)
    return min(args)

def distance_from_zero():
    print abs(args)
    return abs(args)

biggest_number(-9, -3, 3, 9)
smallest_number(-9, -3, 3, 9)
distance_from_zero(-8)
