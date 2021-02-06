# import pygame and points images
import pygame
import images
import random
import datetime

# global variables
global user_points
user_points = 0

global quotesList
quotesList = []


def initializeQuotesVariables():
    global quotesList
    quotesList = ["Whatever makes you happy, put that in your world.", "We don't make mistakes, just happy little accidents.",
                  "Talent is a pursued interest.", "The secret to doing anything is believing you can do it."]

    global quotesIndex
    quotesIndex = random.randint(0, (len(quotesList) - 1))

    global currentDate
    currentDate = datetime.date.today()
    currentDate += datetime.timedelta(days=1)


# points awarded to the user for actions they complete
def drank_water(screen):
    global user_points
    user_points += 10
    # locations inputted as [X,Y]
    drink = pygame.image.load("Resources/bowl.png")
    drink = pygame.transform.scale(drink, (89, 64))   # [left,top] = [32,343]
    screen.blit(drink, [32, 343])
    pygame.display.update()


def ate_food(screen):
    global user_points
    user_points += 10
    feed = pygame.image.load("Resources/bone.png")
    feed = pygame.transform.scale(feed, (152, 141))   # [left,top] = [92,175]
    screen.blit(feed, [92, 175])


def exercise(screen):
    global user_points
    user_points += 5
    dog_exercise = pygame.image.load("Resources/exercise.png")
    dog_exercise = pygame.transform.scale(dog_exercise, (305, 305))
    screen.blit(dog_exercise, [44, 150])


def meditate(screen):
    global user_points
    user_points += 5
    dog_meditate = pygame.image.load("Resources/Dog on rug.png")
    dog_meditate = pygame.transform.scale(dog_meditate, (381, 331))
    screen.blit(dog_meditate, [8, 126])


def daily_quote():
    # TODO: only allow points once a day
    global currentDate
    global quotesList
    if datetime.date.today() != currentDate:
        global quotesIndex
        quotesIndex = random.randint(0, (len(quotesList) - 1))
        currentDate = datetime.date.today()

        global user_points
        user_points += 1

    return quotesList[quotesIndex]

# Updates the points display on the dog screen


def displayPonts():
    global user_points
    return str(user_points)

# Subtracts the points spent at the store from the overall points


def makePurchase(cost):
    global user_points

    if user_points >= cost:
        user_points -= cost
        return True
    else:
        return False
