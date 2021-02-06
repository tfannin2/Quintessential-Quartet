import pygame
import sys
import points
import math
import inventory
import images

pygame.init()
res = (375, 667)
screen = pygame.display.set_mode(res)
color = (0, 0, 0)
color_light = (170, 170, 170)
color_dark = (255, 0, 0)
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

# Only show inventory images if user has previously bought the item.
for stock in inventory
  if stock[1] == True:
    if stock[0] == "hat":
      screen.blit(hat_im,hatButton)
    elif stock[0] == "tie":
      screen.blit(tie_im,tieButton)
    elif stock[0] == "bow tie":
      screen.blit(bowtie_im,bowTieButton)
    elif stock[0] == "bow":
      screen.blit(hairbow_im,hairBowButton)

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
pointsText = smallfont.render(points.displayPonts(), True, color)
image = Inventory


while True:
        screen.blit(image, (0, 0))

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if hatButton[0] <= mouse[0] <= (hatButton[0]+buttonWidth) and hatButton[1] <= mouse[1] <= (hatButton[1] + buttonHeight):
                    for stock in inventory
                      if stock[0] == "hat":
                        stock[2] = True
                      else
                        stock[2] = False

                if bowTieButton[0] <= mouse[0] <= (bowTieButton[0]+buttonWidth) and botTieButton[1] <= mouse[1] <= (bowTieButton[1] + buttonHeight):
                    for stock in inventory
                      if stock[0] == "bow tie":
                        stock[2] = True
                      else
                        stock[2] = False

                if hairBowButton[0] <= mouse[0] <= (hairBowButton[0]+buttonWidth) and hairBowButton[1] <= mouse[1] <= (hairBowButton[1] + buttonHeight):
                    for stock in inventory
                      if stock[0] == "bow":
                        stock[2] = True
                      else
                        stock[2] = False

                if tieButton[0] <= mouse[0] <= (tieButton[0]+buttonWidth) and tieButton[1] <= mouse[1] <= (tieButton[1] + buttonHeight):
                    for stock in inventory
                      if stock[0] == "tie":
                        stock[2] = True
                      else
                        stock[2] = False

                if backButton[0] <= mouse[0] <= (backButton[0]+(buttonWidth/2)) and backButton[1] <= mouse[1] <= (backButton[1] + buttonHeight):
                    switch_background(2)

        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(screen, color_dark, [
            hatButton[0], hatButton[1], buttonWidth, buttonHeight], 3)  # hat

        pygame.draw.rect(screen, color_dark, [
            bowTieButton[0], bowTieButton[1], buttonWidth, buttonHeight], 3)  # bowtie

        pygame.draw.rect(screen, color_dark, [
            hairBowButton[0], hairBowButton[1], buttonWidth, buttonHeight], 3)  # hairbow

        pygame.draw.rect(screen, color_dark, [
            tieButton[0], tieButton[1], buttonWidth, buttonHeight], 3)  # hairbow

        pygame.draw.rect(screen, color_dark, [
            backButton[0], backButton[1], buttonWidth/2, buttonHeight], 3)  # hairbow

        # left, top, width, height pygame.draw.rect(screen, color, (x,y,width,height), thickness)

    # (heigh, width, top, bottom)
    screen.blit(pointsText, (width/2+50, height/2 + height/4 + 15))

    # updates the frames of the game
    pygame.display.update()
    
