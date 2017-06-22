#reading files
"""from sys import argv
#uses argv to get a filename
skripts, filename = argv

txt = open(filename) #returns file object

print "Here\'s your file %r" % (filename)
print txt.read() # Reads the contents of the file. You can assign the result to a variable.

print "Type the filename again: "
file_again = raw_input(">>>") #asks again the filename

txt_again = open(file_again) #returns the file object

print txt_again.read()"""

#reading and writing files

from sys import argv #import modules to a skript from python modules set

skript, filename = argv # unpack it and assign it to all the variables in order

print "Were are going to erase %r." % (filename)
print "If you don\'t want that, hit Ctrl - C (^C)."
print "If you do want that, hit RETURN."

raw_input("??")

print "Opening the file..."
target = open(filename, "w") #open this file in "write" mode

print "Truncating the file...Goodbye."
target.truncate() #REMOVE all the items in the file

print "Now I\'m going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I\'m going to write this to the file."

target.write('%s\n%s\n%s\n' % (line1, line2, line3))
# the same as:
# target.write(line1)
#...


print "Now I\'m going to close the file."
target.close() #how we do we know that the file is closed?

target = open(filename, "r") #open this file in "read" mode. We can also ommit "r" coz it is default parameter
print target.read() #read the file

#creating more files
'''
from sys import argv
from os.path import exists #function exists returns true if the file exists, and false otherwise based on its name in a string as an argument

skript, from_file, to_file = argv

print "Copying from %s to %s..." % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
#we could write this two line in one like this:
#indata = open(to_file, "w").read()
#then you dont need in_file.close().
# It should already be closed by Python once that one line runs.

print "The input file is %d bites long." % len(indata)
print "Does the output file exists? %r" % exists(to_file)
print "If you ready, hit Enter to continue, Cntrl-C to abort."
raw_input("?")

outfile = open(to_file, "w")
outfile.write(indata)


print "Done, now we close the files."

outfile.close()
in_file.close()'''
