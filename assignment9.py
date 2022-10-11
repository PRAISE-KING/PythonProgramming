# using math module , generate 5 common mathematical functions
# create three user defined function , bmi...
# create a new file to import the functions generated

from math import log10 ,log1p ,sqrt ,sin ,pow



def bmi(w , h):
    tot = w /(h**2)
    return tot

def prezzo(l , w, h):
    return l*w*h

def cuberoot(D):
    res = D**3
    return res

