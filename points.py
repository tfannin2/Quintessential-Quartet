# Global variables
global user_points
user_points = 0

# Points awarded to the user for actions they complete
def drank_water():
    global user_points
    print(user_points)
    user_points += 10

def ate_food():
    global user_points
    print(user_points)
    user_points += 10

def exercise():
    global user_points
    print(user_points)
    user_points += 5

def meditate():
    global user_points
    print(user_points)
    user_points += 5

def daily_quote():
    global user_points
    print(user_points)
    user_points += 1

#Updates the points display on the dog screen
def displayPonts():
    global user_points
    print(user_points)
    return str(user_points)

