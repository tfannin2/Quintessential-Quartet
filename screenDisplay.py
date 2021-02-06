# import background images and pygame
import images
import pygame

# activate pygame library
pygame.init()

# screen setup
res = (375,667)
screen = pygame.display.set_mode(res)

# set the pygame window name
pygame.display.set_caption('Image')

# create switch() function that allows the background image to change with called
def switch_background(display_screen):
  return switcher.get(display_screen, home)
