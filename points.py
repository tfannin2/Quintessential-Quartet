# import pygame and points images
import pygame
import images

# global variables
user_points = 0
woke = false                # PROBABLY RESETS EVERYTIME APP IS EXITED... FIX LATER

# points awarded to the user for actions they complete
def drank_water():
    user_points += 10
    screen.blit(water,[32,343])     # locations inputted as [X,Y]

def ate_food():
    user_points += 10
    screen.blit(food,[92,175])

def exercise():
    user_points += 5
    screen.blit(exercise,[44,150])

def meditate():
    user_points += 5
    screen.blit(meditate,[8,126])

def daily_quote():
    if !woke :
        user_points += 1
        woke = true
