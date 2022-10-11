# functions return statements

# return statement - used to end the excecution of the function call and returns the value to the caller
# -they are used to return the results of a function after excecution , therefore the ruturned values can be
# stored inside a variable to be used in another program

def multiply(a, b, c):
    return a * b * c

result = multiply(10, 10, 10)
print(result)

def sum(A, B, C):
    return A+B+C

def product(D):
    return D * 2

answer = product(sum(20, 20, 20))
print(answer)





