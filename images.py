# import pygame
import pygame

# Background and Dog
Welcome = pygame.image.load("Resources/Welcome Page.png")
Home = pygame.image.load("Resources/Home.png")
Inventory = pygame.image.load("Resources/Inventory.png")
Store = pygame.image.load("Resources/Store Page.png")

dog = pygame.image.load("Resources/Dog.png")
dog = pygame.transform.scale(dog, (305, 247))   # --- store --- [35,284] --- home --- [44,150] --- store -> home [+9,-134]

switcherBackground  = {
  1: Welcome,
  2: Home,
  3: Store,
  4: Inventory
}

# Interact
drink = pygame.image.load("Resources/bowl.png")
drink = pygame.transform.scale(drink, (89, 64))   # [left,top] = [32,343]

feed = pygame.image.load("Resources/bone.png")
feed = pygame.transform.scale(feed, (152, 141))   # [left,top] = [92,175]

dog_exercise = pygame.image.load("Resources/exercise.png")
dog_exercise = pygame.transform.scale(dog_exercise, (305, 305))   # [left,top] = [44,121]

dog_meditate = pygame.image.load("Resources/Dog on rug.png")
dog_meditate = pygame.transform.scale(dog_meditate, (381, 331))   # [left,top] = [8,122]

switcher_points = {
  1: feed,
  2: drink,
  3: dog_exercise,
  4: dog_meditate
}

# Items
hat_im = pygame.image.load("Resources/baseballcap.png")
hat_im = pygame.transform.scale(hat_im, (133, 82))   # store --- [left,top] = [104,251] --- home --- [left,top] = [113,117]

bowtie_im = pygame.image.load("Resources/bowtie.png")
bowtie_im = pygame.transform.scale(bowtie_im, (88, 44))   # store --- [left,top] = [113,385] --- home --- [left,top] = [122,251]

hairbow_im = pygame.image.load("Resources/hairbow.png")
hairbow_im = pygame.transform.scale(hairbow_im, (108, 75))   # store --- [left,top] = [121,272] --- home --- [left,top] = [130,138]

tie_im = pygame.image.load("Resources/tie.png")
tie_im = pygame.transform.scale(tie_im, (118, 167))   # store --- [left,top] = [104,362] --- home --- [left,top] = [113,228]

switcher_inventory = {
  1: hat_im,
  2: hairbow_im,
  3: tie_im,
  4: bowtie_im
}

# Other --- more items to buy if time allows?
#treat = pygame.image.load("Resources/bone.png") # Treat and Feed are the same image
#ball = pygame.image.load("Resources/tennisball.png") # Part of exercise
#leash = pygame.image.load("Resources/leash.png") # Part of exercise
