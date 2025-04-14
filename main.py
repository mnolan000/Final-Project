
import pygame

#initialize pygame
pygame.init()

#create screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
#set name of the game
pygame.display.set_caption("final")

#set fps
clock = pygame.time.Clock()
dt = 0
speed = 10

"""Game loop"""
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.quit:
      running = False

  screen.fill("white")

  
  #update screen
  pygame.display.flip()
  #fps
  dt = clock.tick(speed)/1000

#quit
pygame.quit