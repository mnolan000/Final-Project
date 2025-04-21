
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

#text box
base_font = pygame.font.Font(None, 32)
user_input = " "
input_box = pygame.Rect(300,400,50,30)
active_color = pygame.Color("blue")
passive_color = pygame.Color("green")
color = passive_color
      

"""Game loop"""
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.quit:
        running = False

      
    screen.fill("white")

    #draw the circle
    pygame.draw.circle(screen, "black", (400,300) , 270)
    pygame.draw.circle(screen, "white", (400,300) , 265)

    #draw the lines
    pygame.draw.line(screen, "black", (130,300), (665,300), 3)
    pygame.draw.line(screen, "black", (400,30), (400,565), 3)

    #draw the textbox
      #this doesnt work
    pygame.draw.rect(screen, color, input_box, 20)
    if event.type == pygame.MOUSEBUTTONDOWN:
        color = active_color
    else: 
        color = passive_color

    #update screen
    pygame.display.flip()
    #fps
    dt = clock.tick(speed)/1000


#quit
pygame.quit