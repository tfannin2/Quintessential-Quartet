# Global variables
global user_points
user_points = 0

# Points awarded to the user for actions they complete
def drank_water():
    global user_points
    user_points += 10

def ate_food():
    global user_points
    user_points += 10

def exercise():
    global user_points
    user_points += 5

def meditate():
    global user_points
    user_points += 5

def daily_quote():
    global user_points
    user_points += 1

#Updates the points display on the dog screen
def displayPonts():
    global user_points
    return str(user_points)

#Subtracts the points spent at the store from the overall points
def makePurchase(cost):
    global user_points

    if user_points >= cost:
        user_points -= cost
        return True
    else:
        return False
    
        



