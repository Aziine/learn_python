from sys import exit # exit? is that a build-in module?

def gold_room(): # we define new function which we can later call in another function
    print "This room is full of gold. How much do you take?"

    choice = int(raw_input("> ")) # we assign the future input from a user to this variable

    if choice in range(0, 50):# if even one of the conditions is true
        print "Nice, you're not greedy, you win!"
        exit(0) # stop running any loops and if-statements
    elif choice in range(50, 100000):
        dead("You greedy bastard!")
    else: # if it is false
        dead("Man, learn to type a number.")



def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    print "1. Take honey?"
    print "2. Taunt bear?"
    print "3. Open door?"

    bear_moved = False

    while True: # we create an infinite loop
        choice = raw_input("> ")

        if choice == "1" or choice == "Take honey":
            dead("The bear looks at you then slaps your face off.") # run this function
        elif choice == "2" and not bear_moved: # if true and not false
            print "The bear has moved from the door."
            bear_moved = True
        elif choice == "2" and bear_moved: # if true and true
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "3" and bear_moved:
            gold_room()
        elif choice == "3" and not bear_moved: # if true and false
            print "oops! Too early! The bear is not moved yet. Try to move him."
        else:
            print "I got no idea what that means."

def cthulhu_room(): # define function with no parameter
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    print "1. flee?"
    print "2. head?"

    choice = raw_input("> ")

    if "flee" in choice or "1" in choice:
        start() # run this function if true
    elif "head" in choice or "2":
        dead("Well that was tasty!") # run this function with such input variable
    else: # if nothing above is true or unrecognized input
        cthulhu_room()

def dead(why): # define function with one parameter
    print why, "You're killed!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which on do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room() # call this function with its own block of code
    elif choice == "right":
        cthulhu_room() # or call this function with its own block of code
    else: # if unrecognized input
        dead("You stumble around the room until you starve.") # print this function with its statement

start() #we call this function and the game starts
