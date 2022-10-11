# functions - is a block of code that is performing a related task
# enclosed inside brackets
# two categories of functions
# 1. inbuilt functions eg print(), input(), type(), int()....
# 2. user-designed functions
# to create start with a key word 'def'
# then function name
# brackets
# full collon
# any item of a function is indented -

# Add two numbers

# creating
def Add():
    a = 10
    b = 20
    sum = a + b
    print(sum)

# calling a function
# name , followed by the brackets - first exit the function for the pro to run
Add()

# create and call a function that computes the area of a circle

def area_circle():
    PI = 3.142
    rad = 20
    area = PI * (rad**2)
    print(area)
area_circle()

#  parameters - values that are passed inside a function
def multiply(num1 , num2):
    product = num1 * num2
    print(product)

multiply(10 , 20)

def greet(name):
    print("Hey {}".format(name))

greet("PraizKing")

# using function create a bmi calculator
def bmi_calculator(weight, height):
    bmi = weight /(height**2)
    print(bmi)
    return bmi

bmi_calculator(67, 1.7)

