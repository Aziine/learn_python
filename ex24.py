print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
not comprehend passion from intuition
and requires an explanation
\n\t\twhere there is one.
"""

print "-----------"
print poem
print "-----------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula (started): # started is the parameter that can be replaced with any other name with value
    jeally_beans = started * 500 # inside the function the viriable is temporary.
    #when you return it then it can be assigned to a viriable for later
    jars = jeally_beans/1000
    crates = jars/ 100
    return jeally_beans, jars, crates # return the result of the calculations

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do it in that way."
print "We'd have %d beans, %d jars, %d crates." % secret_formula(start_point)
