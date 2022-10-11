# Modules in Python (library)

# Module - python file containing python statements, variable, functions, classes
# Ready Made Modules
# User-defined Modules
# import statements are used to call modules

import math
power = math.pow(8, 2)
print(power)
# help(math) - used to show the contents of the file e.g math

#               OR
from math import pow ,sqrt ,sin
power = pow(8,2)
print(power)
print(sqrt(625))
print(sin(sqrt(625)))

import os
# help(os)

# Volume of figures

def cuboid(l, w, h):
    return l*w*h

def volSphere(r):
    PI = 3.142
    answer = 4/3 *PI * r**3
    return answer

def cylinder(r, h):
    PI = 3.142
    answer = PI * r**2 *h
    return answer

