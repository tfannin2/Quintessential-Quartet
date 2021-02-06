import os
import sys
import pygame
from pygame.locals import *
import screenDisplay


def initializeInventory():
    global inventory
    inventory = [("hat", False), ("tie", False), ("bow tie", False) ("bow", False)]

def makePurchase(item):
    global inventory
    for stock in inventory:
        if stock[0] == item:
            stock[1] = True
            break

def displayInventory():
    #display inventory base image

    global inventory
    for stock in inventory:
        if stock[1] == True:
            #displayItem(stock[0])

