# algorithms require two control structures: iteration and selection
#for ITERATION exist while and for statements
counter = 1 #we should define the name if not we ll get an Error: name is not defined

while counter <= 5: #repeats a body of code as long as the condition is true
    print ("Hi everyone")
    counter += 1 #counter = counter + 1

#while counter <= 10 and not done:

#would cause the body of the statement
# to be executed only in the case where both parts of the condition are satisfied.
#The value of the variable counter would need to be less than or equal to 10 and the value
#of the variable done would need to be False (not False is True) so that True and True results in True.


# for statement works with sequential collection data types (lists, tuples, strings)
for item in [1, 4.6, 5, 66, 7]: #as long as the item is in the list
    print (item) #print it

for item in range(5): #as long as the number(item) is in the range of 5(not including 5 itself)
    print (item ** 2) # print a result of exponentiation of each item

#The range function will return a range object representing the sequence 0,1,2,3,4 and
# each value will be assigned to the variable item.
# This value is then squared and printed.

#The other very useful version of this iteration structure is used to process each character of a string.
# The following code fragment iterates over a list of strings and for each string processes each
#character by appending it to a list.
# The result is a list of all the letters in all of the words.

wordlist = ["kitten", "doggy", "panda"] # we assign an objects in a list for a global frame\name "wordlist"

letterlist = [] # we assign an empty list for a name "letterlist"

for aword in wordlist: # as long as "aword"(we automatically assign every object in a list to this viriable) is in "wordlist"
    for aletter in aword: # and as long as "aletter" is in "aword"
        letterlist.append(aletter) # add "aletter" to the empty "letterlist"
        print letterlist



# SELECTION statements allow programmers to ask questions and then, based on the result, perform different actions.
# Most programming languages provide two versions of this useful construct: the IFELSE and the IF.

import math
n = 5.0
if n<0: # if the value is less than 0
    print "The value is negative, dude!"
else: # if not
    print math.sqrt(n)  #if not done "import math" the terminal returns Error: 'math' is not defined


print "Hello students"
print "Please enter your scores to recieve your grade value"

score = raw_input(">")

if score >= 90:
    print "Your grade is A"
else:
    if score >= 80: #f the score is greater than or
    #equal to 80 then it must be between 80 and 89 since the answer to the first question was false.
        print "Your grade is B"
    else:
        if score >= 70:
            print "Your grade is C"
        else:
            if score >= 60:
                print "Your grade is D"
            else:
                print "Sorry dude but your grade is F" # How to modify it to become a good scores calculator?

#An alternative syntax for this type of nested selection uses the elif keyword.
#The else and the next if are combined so as to eliminate the need for additional nesting levels.

if score >= 90: # why all my inputs recieve "A" answer even if i input "0"?
    print "A"
elif score >=80:
    print "B"
elif score >= 70:
    print "C"
elif score >= 60:
    print "D"
else:
    print "F"


#list that uses iteration and selection constructs known as a list comprehension.
#A list comprehension allows you to easily create a list based on some processing or selection criteria.
# For example, if we would like to create a list of the first 10 perfect squares, we could use a for statement:

sqlist = []
for x in range (1, 11):
    sqlist.append(x**2) #or we could type (x*x)

print sqlist

#but we can make it shorter by using the LIST COMPREHENSION:
sqlist = [x**2 for x in range (1, 11)]

print sqlist

#The general syntax for a list comprehension also allows a selection criteria to be added so that only certain items get added:

sqlist = [x**2 for x in range(1, 11) if x%2  != 0] # if we ommit "!=0" nothing will happen
print sqlist

result = [ch.upper() for ch in 'comprehension' if ch not in 'ei'] # return the string without "these" characters
print result
