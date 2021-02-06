# import pygame
import pygame

# Background and Dog
Welcome = pygame.images.load("resources/Welcome Page.png")
Home = pygame.images.load("resources/Home.png")
Inventory = pygame.images.load("resources/Inventory.png")
Store = pygame.images.load("resources/Store Page.png")
dog = pygame.images.load("resources/Dog.png")

switcher_background{
  1: Welcome,
  2: Home,
  3: Store,
  4: Inventory
}

# Interact
drink = pygames.image.load("resources/bowl.png")
feed = pygame.images.load("resources/bone.png")
dog_exercise = pygame.images.load("resources/exercise.png")
dog_meditate = pygame.images.load("resources/Dog on rug.png")

switcher_points{
  1: feed,
  2: drink,
  3: dog_exercise,
  4: dog_meditate
}

# Items
hat_im = pygame.images.load("resources/baseballhat.png")
bowtie_im = pygames.image.load("resources/bowtie.png")
hairbow_im = pygame.images.load("resources/hairbow.png")
tie_im = pygame.images.load("resources/tie.png")

switcher_inventory{
  1: hat_im,
  2: bow_im,
  3: tie_im,
  4: bowtie_im
}

# Other
treat = pygame.images.load("resources/bone.png") # Treat and Feed are the same image
ball = pygame.images.load("resources/tennisball.png") # Part of exercise
leash = pygame.images.load("resources/leash.png") # Part of exercise