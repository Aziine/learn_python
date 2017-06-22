'''import math
anumber = int(raw_input("Please enter an integer"))
#print math.sqrt(anumber) # this creates a logical errors if the user inputs negative value(-anumber)
try:
    print math.sqrt(anumber)
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print math.sqrt(abs(anumber))
    #his means that the program will not terminate but instead will continue on to the next statements.
    # [exept] cathes an exeption(logical error) and returns a message and uses absolute value

# It is also possible for a programmer to cause a runtime exception by using the raise statement.
# For example, instead of calling the square root function with a negative number, we could have checked
# the value first and then raised our own exception.
# The code fragment below shows the result of creating a new RuntimeError exception.
# Note that the program would still terminate but now the exception that caused the termination is
# something explicitly created by the programmer.

import math #import math features\modules
anynumber = int(raw_input("Please enter your number")) # ask an input from a user
if anynumber <0: # ask if an input value is less than 0
    raise RuntimeError("You can't use negative number") # if it is than create an error\exeption
else: # if not
    print math.sqrt(anynumber) #compute the square root of a given Value'''

print "Do you like movies and books about Sherlock Holmes?"
anyanswer = raw_input("Please, indicate 'yes' or 'no'.")
if anyanswer == "yes" or "y" or "Yes" :
    print "Oh, that's good! It seems that we have common interests."
elif anyanswer == "no" or "n" or "No" or "NO": # why in case of "No" it gives me the 1st "print" version ?
    print "This is sad. It seems that we don't have common interests."
else:
    raise RuntimeError("You didn't indicated any comprehensive answer.")
