# for-loops and lists
# A while-loop will keep executing the code block under it as long as a boolean expression is True.
# What they do is simply do a test like an if-statement, but instead of running the code block once,
# they jump back to the "top" where the while is, and repeat. A while-loop runs until the expression is False.
# 1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
# 2. Review your while statements and make sure that the boolean test will become False at some point.
# 3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
elements = []

# this first kind of for-loop goes through a lists
for number in the_count:# we assign empty variable(storage) for each single element in the list called "the_count"
    print "This is count %d" % number # we print the result

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# then use the range functions to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)


# now we can print them out too
for i in elements: #
    print "Elements was: %d" % i
