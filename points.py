# import pygame and points images
import pygame
import images

# global variables
global user_points
user_points = 0
#woke = false                # PROBABLY RESETS EVERYTIME APP IS EXITED... FIX LATER

# points awarded to the user for actions they complete
def drank_water(screen):
    global user_points
    user_points += 10
    screen.blit(pygame.image.load("Resources/bowl.png"),[32,343])     # locations inputted as [X,Y]
    pygame.display.update()

def ate_food(screen):
    global user_points
    user_points += 10
    screen.blit(images.food,[92,175])

def exercise(screen):
    global user_points
    user_points += 5
    screen.blit(images.exercise,[44,150])

def meditatescreen():
    global user_points
    user_points += 5
    screen.blit(images.meditate,[8,126])

def daily_quote(screen):
    """
    if !woke :
        user_points += 1
        woke = true
    """
    #TODO: only allow points once a day
    quotesList = ["Whatever makes you happy, put that in your world.","We don't make mistakes, just happy little accidents.","Talent is a pursued interest.","The secret to doing anything is believing you can do it."]
    quotesIndex = random.randint(0,(len(quotesList) - 1))

    global user_points
    user_points += 1

    return quotesList[quotesIndex]

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
    
        




