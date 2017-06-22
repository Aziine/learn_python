def hotel_cost(nights): #
    return 140* nights

def plane_ride_cost(city): # the function that calculates the cost of a plane ride to different cities
    if city == "Berlin":
        return 183
    elif city == "Chicago":
        return 220
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days): # the function that calculates the cost for renting a car
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money): # function that sums up all the expenses
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost("Chicago", 5, 600) # how does it cost to trip to Chicago for 5 days with spending 600 dollars

        
