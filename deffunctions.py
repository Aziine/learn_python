#we can hide the details of any computation by defining a function.
# A function definition requires a name, a group of parameters, and a body.
# It may also explicitly return a value.

'''def square(n):
    return n**2
def multiply(a, b):
    return a*b

print square(3)
print square(square(2))
print multiply(square(1), 0)'''

def squareroot(n):
    root = n/2 #initial guess will be 1/2 of n

    for k in range(20):
        root = (1/2)*(root +(n/root)) #Newton's method
    return root

    print squareroot
