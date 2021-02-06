# import pygame and points images
import pygame
import images

# global variables
user_points = 0
woke = false                # PROBABLY RESETS EVERYTIME APP IS EXITED... FIX LATER

# points awarded to the user for actions they complete
def drank_water():
    user_points += 10
    screen.blit(water,)     # ADD LOCATION

def ate_food():
    user_points += 10
    screen.blit(food,)     # ADD LOCATION

def exercise():
    user_points += 5
    screen.blit(exercise,)     # ADD LOCATION

def meditate():
    user_points += 5
    screen.blit(meditate,)     # ADD LOCATION

def daily_quote():
    if !woke :
        user_points += 1
        woke = true
