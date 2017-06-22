def add(a, b):#Our function is called with two arguments: a and b.

#You might say this as, "I add a and b then return them."

    print "ADDING %d + %d." % (a, b) # We print out what our function is doing, in this case "ADDING."
    return a + b # Then we tell Python to do something kind of backward: we return the addition of a + b.
#Python adds the two numbers.
# Then when the function ends, any line that runs it will be able to assign this a + b result to a variable.
def substract(a,b):
    print 'Substracting %d - %d.' % (a, b)
    return a - b

def multiply(a, b):
    print 'Multiplying %d * %d.' % (a, b)
    return a * b

def divide(a, b):
    print 'Dividing %d/%d.' % (a, b)
    return a/b

print "Let's do some math using just functions."

age = add(30, 5)
SAT = multiply(8, 100)
height = substract (200, 28)
weight = divide(120, 2)
iq = multiply (70, 2)


#print "Age: %d, SAT: %d, Height: %d, Weight: %d, iq: %d" % (age, SAT, height, weight, iq)

print 'Here is the puzzle!'

#what = add(age , substract(height, multiply(weight, divide(iq, 2))))

#print "That becomes: ", what, "Can you do it by hand?"

#another_what = divide(height, multiply(weight, substract(iq, add(SAT, 1))))#I'm taking the return value of one
#function and using it as the argument of another function.
#I'm doing this in a chain so that I'm kind of creating a formula using the functions

#print "This becomes: ", another_what, "Can you do it mentally?"

result = divide(add(24.0,26.0), add(100.0,44.0))

print result
