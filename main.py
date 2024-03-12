import pygame
import sys
import os 
import cv2
import numpy as np
from pygame.locals import *
from PIL import Image 

# import button
# Initialize Pygame
pygame.init()

import click
import button

from pages.search import search

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

game = dict(
    zip(
        ['pygame', 'click', 'clock', 'display_info', 'WIDTH', 'HEIGHT', 'FPS', 'scalex', 'scaley', 'scalex1', 'scaley1', 'scalex2', 'scaley2', 'scx', 'scy', 'initialize1', 'initialize2', 'initialize3', 'cap', 'screen', 'WHITE', 'RED', 'rectw', 'recth', 'recty', 'rectx', 'rectx_2', 'hovershift1', 'hovershift2', 'hovershift3', 'hover_background1', 'hover_background2', 'hover_background3', 'running'], 
        [pygame, click, pygame.time.Clock(), display_info, WIDTH, HEIGHT, FPS, scalex, scaley, scalex1, scaley1, scalex2, scaley2, scx, scy, initialize1, initialize2, initialize3, cap, screen, WHITE, RED, rectw, recth, recty, rectx, rectx_2, hovershift1, hovershift2, hovershift3, hover_background1, hover_background2, hover_background3, True]
    )
)

draws = []

# Function to draw the window
def draw_window():
    # print(hovershift2)
    # Fill the screen with white
    # screen.blit(frame, (0, 0))
    game.get('screen').fill(WHITE)
    # pygame.draw.rect(screen, color, (rectx, recty, rectw, recth))
    # pygame.draw.rect(screen, WHITE, (rectx * 4.5, recty, rectw, recth))
    # pygame.draw.rect(screen, WHITE, (rectx * 8, recty, rectw, recth))
    game.get('screen').blit(game.get('search_background'), (game.get('rectx') * .3 + game.get('hovershift1')[0], game.get('recty') * .2 + game.get('hovershift1')[1]-20))
    game.get('screen').blit(game.get('search'), (game.get('rectx') * .3 + game.get('hovershift1')[0], game.get('recty') * .2 + game.get('hovershift1')[1]))
    game.get('screen').blit(game.get('gayming_background'), (game.get('rectx') * .3 + game.get('hovershift2')[0], game.get('recty') + game.get('hovershift2')[1]-15))
    game.get('screen').blit(game.get('gayming'), (game.get('rectx') * .3 + game.get('hovershift2')[0], game.get('recty') + game.get('hovershift2')[1]))
    game.get('screen').blit(game.get('messages_background'), (game.get('rectx') * .3 + game.get('hovershift3')[0], game.get('recty')*1.8 + game.get('hovershift3')[1]-15))
    game.get('screen').blit(game.get('messages'), (game.get('rectx') * .3 + game.get('hovershift3')[0], game.get('recty')*1.8 + game.get('hovershift3')[1]))

    for draw in draws:
        draw[2](game.get('screen'), (0, 0, 0), draw[0])
    # Update the display
    pygame.display.flip()

# Main loop
while game.get('running') == True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game['running'] = False
        elif event.type == pygame.MOUSEMOTION:
            game['scalex'], game['scaley'], game['scalex1'], game['scaley1'], game['scalex2'], game['scaley2'], game['initialize1'], game['initialize2'], game['initialize3'], game['hover_background1'], game['hover_background2'], game['hover_background3'] = button.button((event.pos, game.get('rectx'), game.get('recty'), game.get('rectw'), game.get('recth')))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.get('initialize1'):
                draws.append(search(game, event))
                pass
            elif game.get('initialize2'):
                pass
            elif game.get('initialize3'):
                pass
            
        game['search'] = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search.png')), (game.get('rectw')*game.get('scalex'), game.get('recth')*game.get('scaley'))))
        game['search_background'] = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search_background.png')), (game.get('rectw')*game.get('scalex')*2*game.get('hover_background1'), game.get('recth')*game.get('scaley')*1.2)))
        game['gayming'] = pygame.transform.scale(pygame.image.load(os.path.join('png', 'gayming.png')), (game.get('rectw')*game.get('scalex1'), game.get('recth')*game.get('scaley1')))
        game['gayming_background'] = pygame.transform.scale(pygame.image.load(os.path.join('png', 'Gayming_background.png')), (game.get('rectw')*game.get('scalex1')*game.get('hover_background2')*2.1, game.get('recth')*game.get('scaley1')*1.2))
        game['messages'] = pygame.transform.scale(pygame.image.load(os.path.join('png', 'messages.png')), (game.get('rectw')*game.get('scalex2'), game.get('recth')*game.get('scaley2')))
        game['messages_background'] = pygame.transform.scale(pygame.image.load(os.path.join('png', 'texts_background.png')), (game.get('rectw')*game.get('scalex2')*game.get('hover_background3')*2, game.get('recth')*game.get('scaley2')*1.2))
    
        
    # print(game.get('initialize2'))
    ret, frame = cap.read()
    if ret:
        # Convert the OpenCV frame to a Pygame surface
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)  # Rotate the frame 90 degrees
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.scale(frame, (game.get('WIDTH'), game.get('HEIGHT')+ 200))

    game['hovershift1'] = (game.get('rectw') * (1 - game.get('scalex')) * .5 * game.get('initialize1'), game.get('recth') * (1 - game.get('scaley')) * .5 * game.get('initialize1'))
    game['hovershift2'] = (game.get('rectw') * (1 - game.get('scalex1')) * .5 * game.get('initialize2'), game.get('recth') * (1 - game.get('scaley1')) * .5 * game.get('initialize2'))
    game['hovershift3'] = (game.get('rectw') * (1 - game.get('scalex2')) * .5 * game.get('initialize3'), game.get('recth') * (1 - game.get('scaley2')) * .5 * game.get('initialize3'))
        
    # hovershift2 = initialize2

    # Draw the window
    draw_window()
    # Cap the FPS
    game.get('clock').tick(game.get('FPS'))
   
    # buffer = pygame.image.tostring(screen, "RGBA")
    # image = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buffer)

    # try:
    #     image.save('surface.bmp')
    # except:
    #     pass

# Quit Pygame
pygame.quit()
sys.exit()
