print "Welcome to the GPA Calculator."
print "Enter all your grades, one per line"
print "Enter a blank line to desighnate the end"

points = {"A+": 4.0, "A":4.0, "A-": 3.67, "B+":3.33, "B":3.0, "B-":2.67, "C+":2.33,
        "C": 2.0, "C-": 1.67, "D+":1.33, "D":1.0, "F":0.0} #we set a dictionary of grades and points

num_courses = 0
total_points = 0
done = False
while not done:
    grade = raw_input(">")  #readline from a user
    if grade == " ":        #empty line was entered
        done = True
    elif grade not in points:  #if unrecognized grade entered
        print "Unknown grade '{0}' being ignored".format(grade)
    else: num_courses += 1 # the same as num_courses = num_courses + 1
    total_points += points[grade] # the same as total_points = total_points + points[grades]

if num_courses > 0:
    print "Your GPA is {0:.3}".format(total_points/num_courses)
