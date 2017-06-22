#The variables in your function are not connected to the variables in your script.

'''def cheese_and_crackers(cheese_count, boxes_of_crackers): #we create a function using def
    print "You have %d cheeses." % cheese_count
    print "You have %d boxes of crackers." % boxes_of_crackers
    print "That's enough for a party."
    print "Get a blanket.\n"

print "We can just give the function numbers directly."
cheese_and_crackers(15, 30)

print "Or we can use variables from our skript."
amount_of_cheese = 18
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math inside too"
cheese_and_crackers(18+15, 20+30/1)

print "We can combine variables and math"
cheese_and_crackers(amount_of_cheese + 16, amount_of_crackers+30)'''


def houses_cars(houses, cars):
    print "%r houses and %r cars." % (houses, cars)
    print "That's cool.\n"

print "This is first method."
houses_cars(3, 4)

print "This is second."
amount_of_cars = 4
amount_of_houses = 2
houses_cars(amount_of_houses, amount_of_cars)

print "This is third.",
your_houses = int(raw_input("How many houses do you have?")),
your_cars = int(raw_input("And how many cars?"))
houses_cars(your_houses, your_cars)

print "This is fifth."
houses_cars(amount_of_cars + 4, amount_of_houses + 5)

def houses_cars(*args):
    houses, cars = args
    print "This is forth. houses: %d, cars: %d" % (houses, cars)
    houses_cars(6, 8) # why it does not print anything???

    
