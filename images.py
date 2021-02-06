# import pygame
import pygame

# background images
welcome = pygame.image.load("resources/welcome.png")
home = pygame.image.load("resources/home.png")
store = pygame.image.load("resources/store.png")
inventory = pygame.image.load("resources/inventory.png")

switcher_background{
  1: welcome,
  2: home,
  3: store,
  4: inventory
}

# inventory images
hat_im = pygame.images.load("resources/hat.png")
bow_im = pygame.images.load("resources/bow.png")
tie_im = pygame.images.load("resources/tie.png")
bowtie_im = pygames.image.load("resources/bowtie.png")

switcher_inventory{
  1: hat_im,
  2: bow_im,
  3: tie_im,
  4: bowtie_im
}

# points images
food = pygame.images.load("resources/treat.png")
water = pygames.image.load("resources/toy.png")
exercise = pygame.images.load("resources/ball.png")
meditate = pygame.images.load("resources/toy.png")

switcher_points{
  1: food,
  2: water,
  3: exercise,
  4: meditate
}
