prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices: # we loop through each key in prices
    print key
    print "price: %s" % prices[key] # print values for each key in prices
    print "stock: %s" % stock[key] # print values for each key in stock

total = 0 # set the new variable to 0
for key in prices: # loop through prices
    n = prices[key] * stock[key] # multiply number in prices by number in stock
    print n
    total += n # add the results for each key in prices to the total
print total




shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food: # while loop through each item in food
        if stock[item] > 0 : # if the item's stock count is greater than 0
            total += prices[item] # add the price to the total
            stock[item] -= 1 # decremennt
    return total #  this should be outside the loop but inside the function




lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]




# Write a function average that takes a list of numbers and returns the average.
def average(numbers):
    total = sum(numbers)
    total = float(total)
    result = total/len(numbers)
    return result

# now we need to compute a student's average using weighted averages

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1*homework + 0.3*quizzes + 0.6*tests

# Now let's write a get_letter_grade function that takes a number score as
# input and returns a string with the letter grade that that student should receive.
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print get_letter_grade()
# test function
get_letter_grade(get_average(lloyd))

# We need to get the average for each student and then calculate the average of those averages.
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


print get_class_average(students) # print average score of the class
print get_letter_grade(get_class_average(students)) # print the grade that the class recieves according to an average score
