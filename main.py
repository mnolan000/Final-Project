
import pygame
from pygame.constants import KEYDOWN

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
user_input = ""
input_box = pygame.Rect(50,285,30,30)
active_color = pygame.Color("lightpink")
passive_color = pygame.Color("black")
color = passive_color
active = False



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

    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if input_box.collidepoint(event.pos):
            active = not active
        else:
            active = False
        color = active_color if active else passive_color
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(user_input)
                user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

         

      # Render the current text.
    txt_surface = base_font.render(user_input, True, color)
      # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
      # Blit the text.
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
      # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)


    #update screen
    pygame.display.flip()
    #fps
    dt = clock.tick(speed)/1000



#quit
pygame.quit