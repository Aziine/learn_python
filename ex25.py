def break_words(stuff):
    """This functions will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words in alphabetical way"""
    return sorted(words)

def print_first_word (words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print word


def print_last_word(words):
    """prints the last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Returns the sorted words of a full sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


#or: from ex25 import *
"""import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
words
sorted_words = ex25.sort_words(words)
sorted_words
ex25.print_first_word(words)
ex25.print_last_word(words)
words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words
sorted_words = ex25.sort_sentence(sentence)
sorted_words
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)""" # this lines to type into python iself into terminal
# help(ex25)
# help(ex25.break_words)
