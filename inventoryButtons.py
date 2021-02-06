import pygame
import sys
import points
import math
import inventory
import images

"""
pygame.init()
res = (375, 667)
screen = pygame.display.set_mode(res)
"""
color = (0, 0, 0)
color_light = (170, 170, 170)
color_dark = (255, 0, 0)


def accessInventory(screen):
  width = screen.get_width()
  height = screen.get_height()

  ####Calculating the button sizing#####
  # Top four buttons
  buttonHeight = 100
  buttonWidth = 100
  widthBuffer = buttonWidth/2
  heightBuffer = buttonHeight/2

  # Therefore, the button locations are as follows (left, top)
  hatButton = [21, 106]
  hairBowButton = [138, 106]
  bowTieButton = [254, 106]
  tieButton = [21, 227]
  backButton = [170, 610]

  currInventory = inventory.getInventory()

  # Only show inventory images if user has previously bought the item.
  for stock in currInventory:
    if stock[1] == True:
      if stock[0] == "hat":
        image_hat = pygame.image.load("Resources/baseballcap.png")
        image_hat = pygame.transform.scale(image_hat, (76, 47))
        screen.blit(image_hat, [33, 132])
      elif stock[0] == "tie":
        image_tie = pygame.image.load("Resources/tie.png")
        image_tie = pygame.transform.scale(image_tie, (55, 78))
        screen.blit(image_tie, [44, 238])
      elif stock[0] == "bow tie":
        image_bowTie = pygame.image.load("Resources/bowtie.png")
        image_bowTie = pygame.transform.scale(image_bowTie, (77, 39))
        screen.blit(image_bowTie, [265, 136])
      elif stock[0] == "bow":
        image_hairBow = pygame.image.load("Resources/hairbow.png")
        image_hairBow = pygame.transform.scale(image_hairBow, (75, 52))
        screen.blit(image_hairBow, [151, 130])

  # defining a font
  smallfont = pygame.font.SysFont('Corbel', 35)

  # rendering a text written in
  # this font
  pointsText = smallfont.render(points.displayPonts(), True, color)
  image = pygame.image.load("Resources/Inventory.png")


  while True:
    screen.blit(image, (0, 0))

    for ev in pygame.event.get():

      if ev.type == pygame.QUIT:
        pygame.quit()

      # checks if a mouse is clicked
      if ev.type == pygame.MOUSEBUTTONDOWN:
        if hatButton[0] <= mouse[0] <= (hatButton[0]+buttonWidth) and hatButton[1] <= mouse[1] <= (hatButton[1] + buttonHeight):
          for stock in currInventory:
            if stock[0] == "hat":
              stock[2] = True
            else:
              stock[2] = False

        if bowTieButton[0] <= mouse[0] <= (bowTieButton[0]+buttonWidth) and bowTieButton[1] <= mouse[1] <= (bowTieButton[1] + buttonHeight):
            for stock in currInventory:
              if stock[0] == "bow tie":
                stock[2] = True
              else:
                stock[2] = False

        if hairBowButton[0] <= mouse[0] <= (hairBowButton[0]+buttonWidth) and hairBowButton[1] <= mouse[1] <= (hairBowButton[1] + buttonHeight):
            for stock in currInventory:
              if stock[0] == "bow":
                stock[2] = True
              else:
                stock[2] = False

        if tieButton[0] <= mouse[0] <= (tieButton[0]+buttonWidth) and tieButton[1] <= mouse[1] <= (tieButton[1] + buttonHeight):
            for stock in currInventory:
              if stock[0] == "tie":
                stock[2] = True
              else:
                stock[2] = False

        if backButton[0] <= mouse[0] <= (backButton[0]+(buttonWidth/2)) and backButton[1] <= mouse[1] <= (backButton[1] + buttonHeight):
            return

    mouse = pygame.mouse.get_pos()

    # updates the frames of the game
    pygame.display.update()
    
