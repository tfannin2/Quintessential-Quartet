# import pygame and activate library
import pygame
pygame.init()

# screen setup
res = (375,667)
screen = pygame.display.set_mode(res)

# set the pygame window name
pygame.display.set_caption('Image')

# functions being called in the switch case statement
def welcome():
  image = pygame.image.load(r'<filename>')
  return image

def home():
  image = pygame.image.load(r'<filename>')
  return image

def store():
  image = pygame.image.load(r'<filename>')
  return image

# implementing python switch case statement using dictionary
switcher = {
  1: welcome,
  2: home,
  3: store
}

def switch(display_screen):
  return switcher.get(display_screen, home)
