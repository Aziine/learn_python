from sys import exit # we import from python package the feature/module called "exit"

def death(why): # function to be used if the answer is wrong
    print why, "Good job!"
    exit(0)

def start_here():
    print """Congratulations! You just entered the great game!
    Can you survive with your knowledge?
    There are two doors. Which one do you choose?
    1. "Math" door on your right
    2. "PigLatin" door on your left"""
    choice = raw_input(">")

    if choice == "1" or choice == "right" or choice == "math":
        math_tasks()
    elif choice == "2" or choice == "left" or choice == "hangman":
        piglatin()
    else:
        death("You died. In this game survival is about making decisions.")



def math_tasks():
    print "You are staying in front of a giant head who will examine you."
    print "Try to answer correctly to his math questions and you will survive."
    task_1()
def task_1():
    print "Listen. This is my first question"
    print "What is the result of 34 * 11 ?"

    result = raw_input(">")

    if result != "374" or type(result) != int:
        print "Learn to type numbers!"
    elif result == "374" and type(result) == int:
        task_2()
    else:
        death("Nope)")


def task_2():
    print "This is the second question."
    print "What is the result of 83 * 11"

    result = raw_input(">")

    if result == "913":
        treasures()
    else:
        death("You might have been won.")

def treasures():
    print "  You solved the tasks of the giant head."
    print """  The head became jealous of your intelligence,
               blew out of jealosy and burst and became treasure
               of a thousands of gold coins. It seems that the head
               was full of gold. The question is would you become jealous
               of the treasure or would you leave this place without any coin to survive?"""

    answer = raw_input("Yes or no?\n")

    if answer == "yes":
        print "Hmm...How many coins would you take?"
        how_much = int(raw_input("type a number of coins"))
        if 0 <= how_much <= 1:
            print "Good. You survived"
            exit(0)
        else:
            death("You are no better than this terrible head. Stay here and die because of your own jealosy and greediness")
    elif answer == "no":
        print "You are silly!. How cam someone leave the treasures without taking any single coin?"
        print "But I will give you another try."
        print "How many coins would you take?"
        how_many = int(raw_input("type a number of coins"))
        if 0 <= how_many <= 1:
            print "Well done. Now I am satysfied. You survived!"
            exit(0)
        else:
            death("I did not say that you should have been taken many coins. I said to take one single coin, greedy bastard! You're dead")


def piglatin():
    print "Welcome to the PigLatin's house!"
    print "PigLatin loves to translate words into his own's country's language"
    print "PigLatin: Here you would translate my words into this language"
    print "PigLatin: I will show you how it works."

    pyg = 'ay'

    original = raw_input('Enter a word: ')

    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[1:len(new_word)]
        print "Here is the translated word: %r" % new_word
        piglatin_word()
    else:
        print "You missed the only chance to win this game."
        print "Now, the luck is your best friend."
        piglatin_word()

def piglatin_word():
    print "Listen to my word that you should translate into my language."
    print "Translate the word 'dmagic'"
    translated = raw_input(">")
    if translated == "magicday":
        print "Congratulations! You deserved your survival...and the gift!"
        print """
              [;;;;;;;;;;;]
               [=========]
               [=========]
               [=========]
                 [=====]
                  [===]
                   [=]
                  [===]
                [[=====]]"""
        exit(0)
    else:
        death("I expected that. PigLatin never gifts the life to the ones who lose.")


start_here()
