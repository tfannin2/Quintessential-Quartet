# import pygame and activate library
import pygame
pygame.init()

# screen setup
white = (255,255,255)
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

def home_food():
  image = pygame.image.load(r'<filename>')
  return image

def home_water():
  image = pygame.image.load(r'<filename>')
  return image

def home_exercise():
  image = pygame.image.load(r'<filename>')
  return image

def home_meditate():
  image = pygame.image.load(r'<filename>')
  return image

def store():
  image = pygame.image.load(r'<filename>')
  return image

def store_baseball_hat():
  image = pygame.image.load(r'<filename>')
  return image

def store_hair_bow():
  image = pygame.image.load(r'<filename>')
  return image

def store_tie():
  image = pygame.image.load(r'<filename>')
  return image

def store_bow_tie():
  image = pygame.image.load(r'<filename>')
  return image

# implementing python switch case statement using dictionary
switcher = {
  1: home(),
  2: home_food(),
  3: home_water(),
  4: home_exercise(),
  5: home_meditate(),
  6: store(),
  7: store_baseball_hat(),
  8: store_hair_bow(),
  9: store_tie(),
  10: store_bow_tie()
}

def switch(button):
  return switcher.get(button, home())()
