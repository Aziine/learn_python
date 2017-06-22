name = 'Aziine'
age = 18
height = 172
weight = 60
eyes = 'black'
  hair = 'black'

print "Let's talk about %s" % name
print "She's %d cantimeters tall." % height
print "Her weight is %d." % weight
print "She is %d years old." % age
print "If I add %d, %d and %d I get %d." % (weight, height, age, age + height + weight)

x = "There are %d types of people." % 2
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "The fact that %r is true." % x
print "I said: %s." % y

#%r - format "print it anyway"

good = False
work_evaluation = "Is the work that I am doing is right? %r"
print work_evaluation % good

a = "This is"
b = " a good job"

print a + b


print "Mary had a little lamb."
print "It's fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 3

a1 = "C"
b2 = "h"
b3 = "e"
b4 = "e"
b5 = "s"
b6 = "e"
b7 = "B"
b8 = "u"
b9 = "r"
b10 = "g"
b11 = "e"
b12 = "r"

print a1 + b2 + b3 + b4 + b5 + b6,
print  b7 + b8 + b9 + b10 + b11 + b12

print a1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12


formatter = "%r %r %r %r" #r = it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (False, True, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
        "Than I got this thing.",
        "After that I recieved this.",
        "Finally I have this."
        )


days = "Mon Tue Wed Thu Fri Sut Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n = new line

print "Here are the days: ", days
print "Here are the months: ", months




tabby_cat = "\tI'm tabbed in." #\t - tab
print tabby_cat

persian_cat = "I'm split/non a line."
print persian_cat

backslash_cat = "I'm \\ a \\ cat."
print backslash_cat

fat_cat = """The list of smthg:
\t* Cookies
\t* cat food"""

print fat_cat



age = raw_input ("How old are you?")
height = raw_input ("How tall are you?")
weight = raw_input ("How much do you weight?")

print "So you're %r years old, %r heavy, %r tall. " % (age, weight, height)
print "Am I right?",
answer = raw_input ()

from sys import argv #this is called an "import." This is how you add features to your script from the Python feature set

skript, first, second, third = argv #Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order

print "This file is called: ", skript
print "This is the: ", first
print "This is the: ", second
print "This is the: ", third

from sys import argv
skript, user_name = argv
prompt = '> '

print "Hi %s, I am the %s skript!." % (user_name, skript)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name

temperature = 98.6
original = temperature
temperature = temperature + 5.0
original = temperature
# in this example identificators(temperature and original) are alies
print original
print temperature

print "How are you?",
mood = raw_input()# raw_input() vs input(). Input() is not safe coz it can run the script


#Built-in Collection Data types: ordered - lists, strings and tuples
myList = [1, 2, 5, 4, 67, 87, 99, True, 0]

print myList [1] #this is called indexing. used to access an element from a sequence

print myList [2] * 2 #conctatenate repeated num of times

print myList + myList #conctatenation. can only conctatenate list (not int, float or str) to list
print myList [0:6] #sclicing - extract the part of a sequence (from 1 to 99 not including the 99)

#the methods that lists support to build data structure are below
myList.append("Hi I have been just added") #alist.append(item) adds a new item to the end of the list
print myList

myList.insert(0, "someone added me to this place") #alist.insert(i, item) inserts a new item to the ith position in the list
print myList"""

"""newList = [1, 2, 3, 4, 5, 6, 7, 8]
print newList

newList.pop(0) #removes and returns the item on the 0 position in the list

newList.pop() #removes and returns the last item in the list
print newList

newList.sort() #modifies a list to be sorted in order
print newList

newList.reverse() #modifies a list to be in reverse order
print newList

del newList [1] #deletes an item in the indicated[1] position in the list
print newList

newList.insert(0, 0)
newList.insert(0, 99)
print newList
print newList.index(0) #returns the index of the first occurence of 0

print newList.count(99) #returns the number of occurences of the 99

newList.remove(0)
print newList

print in(newList) #in --membership(how to ask whether an item is in membership)
print [0] in(newList)

#range produces a range object that represents a sequence of values.
# By using the list function, it is possible to see the value of the range object as a list. This is illustrated below.

range (10)
print list(range(10)) #starts from 0 to 10 not including the 10 itself

print list(range(5, 10)) #starts from 5 to 10(not including 10)

print list(range(5, 10, 2)) #starts from 5 to 10 but skips every 2nd item

print list(range(10, 1, -1)) #starts from 10 and the following items are less (-1)"""

# A major difference between lists and strings is that lists can be modified while strings cannot.
# This is referred to as mutability. Lists are mutable; strings are immutable.
myName = "Aziine"

print myName[1]
print myName * 2

print len(myName)

print myName.upper() #AZIINE

print myName.lower() #aziine

print myName.center(12) #returns a string in a center of a field of size 12(for example)

print myName.count("i") #returns a nummber of occurences of an item in a strings

print myName.ljust(15) #returns a string left-justified of a field of size 15

print myName.rjust(15) #returns a string right-justified of a field of size 15

print myName.find("z") #returns an index of the first occurence of item

print myName.split("n") #splits a string into two substrings at "n"(or any other item(s) in a string)

#Tuples are very similar to lists in that they are heterogeneous sequences of data.
 #The difference is that a tuple is immutable, like a string. A tuple cannot be changed.
 #Tuples are written as comma-delimited values enclosed in parentheses.
 #As sequences, they can use any operation described above.

myTuple = (1, 2, 5, False, 6, 90, 1)

print len(myTuple)

print myTuple * 2

print myTuple [1:10]

print myTuple[0]

#A set is an unordered collection of zero or more immutable Python data objects.
#Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces.
#The empty set is represented by set().
#Sets are heterogeneous, and the collection can be assigned to a variable as below.
#sets are not sequential

myset = {False, True, 77, 88, 54, "kitten", 56}
newset = {False, 66, 55, 11, 12, "doggy"}
#operations are below
print len(myset)

print myset| newset #returns a new set with elements from both sets


print myset & newset #returns a new set of the elements that are common to both sets

print myset - newset #returns a new set with all items in a myset not in newset
print newset - myset #returns a new set with all items from the first set(newset) not in second(myset)

print newset <=myset # ask whether all elements from the first set are in the second

print "kitten" in myset #asks a membership

#methods of sets are below
print myset.union(newset) #method similiar to the operation aset | otherset

print myset.intersection(newset) #method similiar to the operation aset & otherset

print newset.difference(myset) #similiar to the operation newset - myset

print myset.issubset(newset) #the same as myset <= newset

myset.add("Hi everybody") #adds new item in a set
print myset

myset.remove("kitten") #removes an item from a set
print myset

newset.pop() #removes arbitrary item from the set
print newset

newset.clear() #removes all elements from the set
print newset

# unordered structure called a dictionary.
# Dictionaries are collections of associated pairs of items where each pair consists of a key and a value.
# This key-value pair is typically written as key:value.
# Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces.

capitals = {"Kyrgyzstan":"Bishkek", "Kazachstan": "Astana", "United Kingdom":"London", "France":"Paris"}
print (len(capitals))

for n in capitals:
    print (capitals[n], "is the capital of", n) # myDict[] operator returns a value associated with the key[]

    print "Kyrgyzstan" in capitals #returns true if there is a such key i the diitionary "capitals

 #methods of the dict Class

print capitals.keys() #returns the keys of the dictionary 'capitals'
print capitals.values() #returns the values

print capitals.items() #returns the key:value of a dictionary

print capitals.get("Kyrgyzstan") #returns the value associated with the given key. "none" otherwise
print capitals.get("Canada", "no entry") #returns the value associated with the key. if no then - "no entry

#Python provides us with a function that allows us to ask a user to enter
# some data and returns a reference to the data in the form of a string.
#The function is called input.
# input function takes a single parameter that is a string.
 #This string is often called the prompt because
 #it contains some helpful text prompting the user to enter something.

aName = raw_input("What is your name ") # input doest work at all. i have checked
print ("So your name is", aName.upper(), "and is as long as", len(aName), "letters")

cradius = input("Please, enter the radius of a circle ")
print cradius
radius = float(cradius) #string is interpreted to the float type
print radius
diameter = radius * 2
print diameter

#String formatting
# % is the formatting operator
# d, i - integer
# s - string
# f - floating point as m.ddddddd
# u - insigned floating point
# e - floating point as m.ddddde +\-xx
# E - floating point as m.dddddE  +\-xx
# c - single character
# s - string, or any python object that can be converted into a string using str function
# r - insert no matter What

from sys import argv

skript, username, friend= argv
podskazka = "----"

print "Hi %s I am the %s skript." % (username, skript)
print "I\'d like to ask you a few questions."
print "Do you like %s?" % (friend)
likes = raw_input(podskazka)

print "Where do you live %s?" % (username)
lives = raw_input(podskazka)

print "What an operation system do you have %s?" % (username)
opsys = raw_input(podskazka)

print """So you answered %s to the question of liking me.
\nYou have also said the you live in %s and that you have a %r on your computer.
\nThat's nice." % (likes, lives, opsys)""
