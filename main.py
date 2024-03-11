import pygame
import sys
import os 
# import button
# Initialize Pygame
pygame.init()
import cv2
import numpy as np
from pygame.locals import *
from PIL import Image 
import click

# Define screen dimensions and FPS
display_info = pygame.display.Info()
WIDTH = display_info.current_w - 100
HEIGHT = display_info.current_h - 100
FPS = 60
scalex=1
scaley=1
scalex1=1
scaley1=1
scalex2=1
scaley2=1
scx=.95
scy=.95
initialize1=0
initialize2=0
initialize3=0
cap = (cv2.VideoCapture(0))

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("White Screen Example")

# Define colors
# color: (255,255,255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
rectw = WIDTH//6.5
recth = HEIGHT//4
recty = HEIGHT//2 - recth/2
rectx = WIDTH//12
rectx_2 = rectx * 0.3

hovershift1 = 0.0
hovershift2 = 0.0
hovershift3 = 0.0
hover_background1 = 0
hover_background2 = 0
hover_background3 = 0


import button

# Function to draw the window
def draw_window():
    # print(hovershift2)
    # Fill the screen with white
    # screen.blit(frame, (0, 0))
    screen.fill(WHITE)
    # pygame.draw.rect(screen, color, (rectx, recty, rectw, recth))
    # pygame.draw.rect(screen, WHITE, (rectx * 4.5, recty, rectw, recth))
    # pygame.draw.rect(screen, WHITE, (rectx * 8, recty, rectw, recth))
    screen.blit(search_background, (rectx * .3 + hovershift1[0], recty * .2 + hovershift1[1]-20))
    screen.blit(search, (rectx * .3 + hovershift1[0], recty * .2 + hovershift1[1]))
    screen.blit(gayming_background, (rectx * .3 + hovershift2[0], recty + hovershift2[1]-15))
    screen.blit(gayming, (rectx * .3 + hovershift2[0], recty + hovershift2[1]))
    screen.blit(messages_background, (rectx * .3 + hovershift3[0], recty*1.8 + hovershift3[1]-15))
    screen.blit(messages, (rectx * .3 + hovershift3[0], recty*1.8 + hovershift3[1]))


    # Update the display
    pygame.display.flip()

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            scalex, scaley, scalex1, scaley1, scalex2, scaley2, initialize1, initialize2, initialize3, hover_background1, hover_background2, hover_background3 = button.button((event.pos, rectx, recty, rectw, recth))
            click.click(event.pos[0], event.pos[1], rectx, recty, rectw, recth)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if initialize1:
                pass
            elif initialize2:
                pass
            elif initialize3:
                pass
            
        search = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search.png')), (rectw*scalex, recth*scaley)))
        search_background = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search_background.png')), (rectw*scalex*2*hover_background1, recth*scaley*1.2)))
        gayming = pygame.transform.scale(pygame.image.load(os.path.join('png', 'gayming.png')), (rectw*scalex1, recth*scaley1))
        gayming_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'Gayming_background.png')), (rectw*scalex1*hover_background2*2.1, recth*scaley1*1.2))
        messages = pygame.transform.scale(pygame.image.load(os.path.join('png', 'messages.png')), (rectw*scalex2, recth*scaley2))
        messages_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'texts_background.png')), (rectw*scalex2*hover_background3*2, recth*scaley2*1.2))
    
        
    # print(initialize2)
    ret, frame = cap.read()
    if ret:
        # Convert the OpenCV frame to a Pygame surface
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)  # Rotate the frame 90 degrees
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.scale(frame, (WIDTH, HEIGHT+ 200))

    hovershift1 = (rectw * (1 - scalex) * .5 * initialize1, recth * (1 - scaley) * .5 * initialize1)
    hovershift2 = (rectw * (1 - scalex1) * .5 * initialize2, recth * (1 - scaley1) * .5 * initialize2)
    hovershift3 = (rectw * (1 - scalex2) * .5 * initialize3, recth * (1 - scaley2) * .5 * initialize3)
   
        
    # hovershift2 = initialize2

    # Draw the window
    draw_window()
    # Cap the FPS
    clock.tick(FPS)
   
    # buffer = pygame.image.tostring(screen, "RGBA")
    # image = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buffer)

    # try:
    #     image.save('surface.bmp')
    # except:
    #     pass

# Quit Pygame
pygame.quit()
sys.exit()