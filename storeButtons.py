import pygame
import sys
import points
import math
import inventory
# import screenDisplay

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
buttonHeight = 39
buttonWidth = 113
widthBuffer = buttonWidth/2
heightBuffer = buttonHeight/2

# Therefore, the button locations are as follows (top, left)
hatButton = [13, 90]
hairBowButton = [247, 90]
bowTieButton = [247, 153]
tieButton = [13, 153]
backButton = [170, 610]

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
pointsText = smallfont.render(points.displayPonts(), True, color)
image = pygame.image.load('resources/Store.png')


def buyAnItem(itemName, cost):
    inventory.makePurchase(itemName, cost)


while True:
        screen.blit(image, (0, 0))

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if hatButton[0] <= mouse[0] <= (hatButton[0]+buttonWidth) and hatButton[1] <= mouse[1] <= (hatButton[1] + buttonHeight):
                    buyAnItem("hat", 100)

                if bowTieButton[0] <= mouse[0] <= (bowTieButton[0]+buttonWidth) and botTieButton[1] <= mouse[1] <= (bowTieButton[1] + buttonHeight):
                    buyAnItem("bow tie", 120)

                if hairBowButton[0] <= mouse[0] <= (hairBowButton[0]+buttonWidth) and hairBowButton[1] <= mouse[1] <= (hairBowButton[1] + buttonHeight):
                    buyAnItem("bow", 120)

                if tieButton[0] <= mouse[0] <= (tieButton[0]+buttonWidth) and tieButton[1] <= mouse[1] <= (tieButton[1] + buttonHeight):
                    buyAnItem("tie", 120)

                if backButton[0] <= mouse[0] <= (backButton[0]+(buttonWidth/2)) and backButton[1] <= mouse[1] <= (backButton[1] + buttonHeight):
                    # need to re load images for home screen TODO
                    print("NEED TO SWITCH HOME SCREEN")

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
