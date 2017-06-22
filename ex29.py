people = 25
cats = 15
dogs = 26

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats. The world is saved!" # ":"  and the space indicates that you are going to create the block of a code

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people > dogs and cats < people :   # If this boolean expression is True, then run the code under it, otherwise skip it.
    print "People are dogs."
