#if-statements inside the if-statements


print "Do you like games?"
answer = raw_input("Yes or no? ") # define for a user two variations of answers

if answer == "yes" or answer == "yeah": # if user used 1 variant execute the block of code below 
    print "Let's play then!"
    print "You enter a dark room with two doors. Do you go through door # 1 or #2?."

    door = raw_input("> ") # assign the input of a user to this variable

    if door == "1" or door == "one": # if (input - door equals "1" or "one) it is true then run the code below line by line
        print "There's a giant bear here eating a cheese cake. What do you do?"
        print "1. Take the cake."
        print "2. Scream at the bear."

        bear = raw_input("> ") # assign another input to this name

        if bear == "1" or bear == "take the cake": # if it is true run the code below
            print "The bear eats your face off. Good job!"
        elif bear == "2" or bear == "Scream at the bear": # if the previous if-statement is false try out this condition
            print "The bear eats your legs off. Good job!"
        else: # if the previous conditions are false run this:
            print "Well, doing %s is probably better. Bear runs away."

    elif door == "2" or door == "two" or door == "second one": # if the first if-statement is false, try this
        print "You stare into endless abyss at Cthulhu's retina. What do you imagine?"
        print "1. Blueberries."
        print "2. Yellow jacket clothespins."
        print "3. Understanding revolvers yelling melodies."

        insanity = raw_input("> ")

        if insanity == "1" or insanity == "2":
            print "Your body survives powered by a mind of jello."
        else:
            print "The insanity rots your eyes into a pool of muck. Good job!"

    else:
        print "You stumble around and fall on a knife and die. Good job!"

elif answer == "no":
    print "Okay, bye!"

else:
    print "Sorry, but I don't understand your answer"
