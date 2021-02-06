# import pygame
import pygame

# Background and Dog
Welcome = pygame.image.load("Resources/Welcome Page.png")
Home = pygame.image.load("Resources/Home.png")
Inventory = pygame.image.load("Resources/Inventory.png")
Store = pygame.image.load("Resources/Store Page.png")
dog = pygame.image.load("Resources/Dog.png")

switcherBackground  = {
  1: Welcome,
  2: Home,
  3: Store,
  4: Inventory
}

# Interact
drink = pygame.image.load("Resources/bowl.png")
feed = pygame.image.load("Resources/bone.png")
dog_exercise = pygame.image.load("Resources/exercise.png")
dog_meditate = pygame.image.load("Resources/Dog on rug.png")

switcher_points = {
  1: feed,
  2: drink,
  3: dog_exercise,
  4: dog_meditate
}

# Items
hat_im = pygame.image.load("Resources/baseballcap.png")
bowtie_im = pygame.image.load("Resources/bowtie.png")
hairbow_im = pygame.image.load("Resources/hairbow.png")
tie_im = pygame.image.load("Resources/tie.png")

switcher_inventory = {
  1: hat_im,
  2: hairbow_im,
  3: tie_im,
  4: bowtie_im
}

# Other
treat = pygame.image.load("Resources/bone.png") # Treat and Feed are the same image
ball = pygame.image.load("Resources/tennisball.png") # Part of exercise
leash = pygame.image.load("Resources/leash.png") # Part of exercise