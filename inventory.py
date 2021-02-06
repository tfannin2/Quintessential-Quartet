import os
import sys
import pygame
from pygame.locals import *
#import screenDisplay
import points


def initializeInventory(): # ("item",bought,wearing)
    global inventory
    inventory = [["hat", False, False], ["tie", False, False],["bow tie", False, False], ["bow", False, False]]



def getInventory():
    global inventory
    return inventory

def makePurchase(item, cost):
    global inventory
    for stock in inventory:
        if stock[0] == item and stock[1] == False:
            if points.makePurchase(cost):
                stock[1] = True
                return "done"
            else:
                return "insufficient funds"
        elif stock[0] == item and stock[1] == True:
            return "previously bought"

"""
def displayInventory():
    #display inventory base image

    global inventory
    for stock in inventory:
        if stock[1] == True:
            #displayItem(stock[0])
            x = 1
"""
