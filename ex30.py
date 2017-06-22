people = 30
cars = 40
trucks = 15 # we assigned thise integer values to this variables\names\identificators

if cars > people: # in case if it is true then run the code after it. If false - just skip it
    print "We should produce or import more cars."
elif cars < people: # in case if the first condition was false and this condition is true then run the code after it. otherwise skip it
    print "We should decrease the production and import of cars."
else: # final condition is true if the above statements are false
    print "We can't decide coz cars are not either greater or less than people."

if trucks > cars:
    print "There're too much trucks comparing to the amount of cars."
elif trucks < cars:
    print "Maybe we should import or produce more trucks."
else:
    print "We still can't decide coz trucks are not either greater or less than cars."

if people > trucks or cars > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's do not change anything."
