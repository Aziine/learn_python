# A for-loop can only iterate (loop) "over" collections of things.
# A while-loop can do any kind of iteration (looping) you want.

i = 0
numbers = [] # we assigned empty list

while i < 6: # as long as this is true print the following line by line
    print "At the top i is %d" % i # print the result
    numbers.append(i) # add the new value\result to the end of the list

    i += 1 # now we add 1 to i. It is really needed in while loops
    print "Numbers now: ", numbers # now we print the list which has [0] in it
    print "At the bottom i is %d" % i # print new i
# this while-loop will run again and again until it will become false

print "The numbers: "

# here we print all the numbers one by one when the block of code above is over
for num in numbers: # as long as num is in the list
    print num


# the task:
# 1. convert while-loop to a function that we can call *
# 2. replace 6 with a variable (\ replaced range instead *)
# 3. try different numbers *
# 4. change += 1 so we can change how much it increments by *
# 5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore? *tom"  yes we still need it to print "At the bot"
#  What happens if you do not get rid of it? * 6 in range that is not included arises

i = 0
numbers = []
number = range(0, 6) # assigned the range to the variable

def while_loop_function(i): # defined a new function with the parameter i
    for i in number: # for-loop with function range within the variable
        print "At the top i is %d" % i
        numbers.append(i)


        i += 1 # add to the list 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

def print_numbers():
    print "The numbers: "

    for num in numbers:
        print num
# then we call functions
while_loop_function(i)
print_numbers()
