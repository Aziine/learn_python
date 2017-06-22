#names, variables, methods, functions
#You can create a function by using the word def in Python

def print_two(*args):#similar to the from sys import argv.First we tell Python we want to make a function using def for "define".
    arg1, arg2 = args #unpacks the argument
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg3, arg4): #we can make it simpier by removing the *args
    print "arg3: %r, arg4: %r" % (arg3, arg4)

def print_just_one_arg(arg5): #this one makes 1 argument
    print "arg5: %r" % (arg5)

def print_none(): #this one makes none
    print "There is nothing"

    print_two("Coder", "Qoovie")
    print_just_one_arg("Qoovie")
    print_two_again("Coder", "Qoovie")
