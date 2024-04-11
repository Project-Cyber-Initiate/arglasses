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
import subprocess

# Define screen dimensions and FPS
display_info = pygame.display.Info()
WIDTH = display_info.current_w * .95
HEIGHT = WIDTH/2
FPS = 60
scalex=1
scaley=1
scalex1=1
scaley1=1
scalex2=1
scaley2=1
searchdown = 0

scx=.95
scy=.95
initialize1=0
initialize2=0
initialize3=0
cap = None#(cv2.VideoCapture(0))


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("arglasses")

buttonsnum = 0

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

print (WIDTH)
print (HEIGHT)

def run_oled_code():
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_test.py"
    subprocess.run(["python", oled_script_path])
    
run_oled_code()

class Game:
    def __init__(self):
        pass
    def get(self, key):
        return self.__dict__.get(key)
    def __setattr__(self, key, value):
        self.set(key, value)
    def set(self, key, value):
        if key in self.__dict__ and value != self.__dict__.get(key):
            try:
                self.__dict__[key] = value
                if key in ['rectw', 'recth', 'scalex', 'scaley', 'initialize1', 'hover_background1']:
                    game.search = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search.png')), (game.get('rectw')*game.get('scalex')*.9, game.get('recth')*game.get('scaley'))))
                    game.search_background = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search_background.png')), (game.get('rectw')*game.get('scalex')*2*game.get('hover_background1'), game.get('recth')*game.get('scaley')*1.2)))
                if key in ['rectw', 'recth', 'scalex1', 'scaley1', 'initialize2', 'hover_background2']:
                    game.gayming = pygame.transform.scale(pygame.image.load(os.path.join('png', 'gayming.png')), (game.get('rectw')*game.get('scalex1')*.88, game.get('recth')*game.get('scaley1')*.95))
                    game.gayming_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'Gayming_background.png')), (game.get('rectw')*game.get('scalex1')*game.get('hover_background2')*2.1, game.get('recth')*game.get('scaley1')*1.2))
                if key in ['rectw', 'recth', 'scalex2', 'scaley2' 'initialize3', 'hover_background3']:
                    game.messages = pygame.transform.scale(pygame.image.load(os.path.join('png', 'messages.png')), (game.get('rectw')*game.get('scalex2')*.9, game.get('recth')*game.get('scaley2')))
                    game.messages_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'texts_background.png')), (game.get('rectw')*game.get('scalex2')*game.get('hover_background3')*2, game.get('recth')*game.get('scaley2')*1.2))
            except:
                pass
        self.__dict__[key] = value
    

game = Game()

for key, value in zip(
    ['pygame', 'click', 'clock', 'display_info', 'WIDTH', 'HEIGHT', 'FPS', 'scalex', 'scaley', 'scalex1', 'scaley1', 'scalex2', 'scaley2', 'scx', 'scy', 'initialize1', 'initialize2', 'initialize3', 'cap', 'screen', 'WHITE', 'RED', 'rectw', 'recth', 'recty', 'rectx', 'rectx_2', 'hovershift1', 'hovershift2', 'hovershift3', 'hover_background1', 'hover_background2', 'hover_background3', 'running'], 
    [pygame, click, pygame.time.Clock(), display_info, WIDTH, HEIGHT, FPS, scalex, scaley, scalex1, scaley1, scalex2, scaley2, scx, scy, initialize1, initialize2, initialize3, cap, screen, WHITE, RED, rectw, recth, recty, rectx, rectx_2, hovershift1, hovershift2, hovershift3, hover_background1, hover_background2, hover_background3, True]
):
    game.__setattr__(key, value)

if (__name__ == "__main__"):
    import pages.search
    import pages.gayming_button
    import pages.messages_button

    draws = [pages.search.draw, pages.gayming_button.draw, pages.messages_button.draw]

    pages.search.ready()
    pages.gayming_button.ready()
    pages.messages_button.ready()

    def draw_window():
        # print(hovershift2)
        # Fill the screen with white
        # screen.blit(frame, (0, 0))
        # print (searchdown)

        game.oled_show = pygame.transform.scale(pygame.image.load(os.path.join('png', 'main_page.bmp')), (game.get('rectw'), game.get('recth')*game.get('scaley2')*1.2))
        
        game.get('screen').fill(WHITE)
        game.get('screen').blit(game.get('search_background'), (game.get('rectx') * .3 + game.get('hovershift1')[0], game.get('recty') * .2 + game.get('hovershift1')[1]-20))
        game.get('screen').blit(game.get('search'), (game.get('rectx') * .3 + game.get('hovershift1')[0], game.get('recty') * .2 + game.get('hovershift1')[1]))
        game.get('screen').blit(game.get('gayming_background'), (game.get('rectx') * .3 + game.get('hovershift2')[0]+10, game.get('recty') + game.get('hovershift2')[1]-10))
        game.get('screen').blit(game.get('gayming'), (game.get('rectx') * .3 + game.get('hovershift2')[0]+10, game.get('recty') + game.get('hovershift2')[1]+10))
        game.get('screen').blit(game.get('messages_background'), (game.get('rectx') * .3 + game.get('hovershift3')[0], game.get('recty')*1.8 + game.get('hovershift3')[1]-15))
        game.get('screen').blit(game.get('messages'), (game.get('rectx') * .3 + game.get('hovershift3')[0], game.get('recty')*1.8 + game.get('hovershift3')[1]))
        if game.get(initialize1) == 1:
            None
        else:
            game.get('screen').blit(game.get('oled_show'), (game.get('WIDTH')*.8, game.get('HEIGHT')*.05))


        for draw in draws:
            draw(game)

        # Update the display
        pygame.display.flip()
    # Main loop

    game.search = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search.png')), (game.get('rectw')*game.get('scalex')*.9, game.get('recth')*game.get('scaley'))))
    game.search_background = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search_background.png')), (game.get('rectw')*game.get('scalex')*2*game.get('hover_background1'), game.get('recth')*game.get('scaley')*1.2)))
    game.gayming = pygame.transform.scale(pygame.image.load(os.path.join('png', 'gayming.png')), (game.get('rectw')*game.get('scalex1')*.88, game.get('recth')*game.get('scaley1')*.95))
    game.gayming_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'Gayming_background.png')), (game.get('rectw')*game.get('scalex1')*game.get('hover_background2')*2.1, game.get('recth')*game.get('scaley1')*1.2))
    game.messages = pygame.transform.scale(pygame.image.load(os.path.join('png', 'messages.png')), (game.get('rectw')*game.get('scalex2')*.9, game.get('recth')*game.get('scaley2')))
    game.messages_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'texts_background.png')), (game.get('rectw')*game.get('scalex2')*game.get('hover_background3')*2, game.get('recth')*game.get('scaley2')*1.2))        
        
    while game.get('running') == True:
        # draw_window()
        # Handle events
        for event in pygame.event.get():
            pages.search.event(game, event)
            pages.gayming_button.event(game, event)
            pages.messages_button.event(game, event)

            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.MOUSEMOTION:
                game.scalex, game.scaley, game.scalex1, game.scaley1, game.scalex2, game.scaley2, game.initialize1, game.initialize2, game.initialize3, game.hover_background1, game.hover_background2, game.hover_background3 = button.button((event.pos, game.get('rectx'), game.get('recty'), game.get('rectw'), game.get('recth')))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.get('initialize1'):
                    searchdown = 1
                    pages.search.show(game, event, buttonsnum)
                    pages.gayming_button.hide()
                    pages.messages_button.hide()
                elif game.get('initialize2'):
                    searchdown = 0
                    pages.gayming_button.show(game, event, buttonsnum)
                    pages.search.hide()
                    pages.messages_button.hide()
                elif game.get('initialize3'):
                    searchdown = 0
                    pages.messages_button.show(game, event, buttonsnum)
                    pages.search.hide()
                    pages.gayming_button.hide()
            
        # print(game.get('initialize2'))
        ret, frame = (None, None)#cap.read()
        if ret:
            # Convert the OpenCV frame to a Pygame surface
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)  # Rotate the frame 90 degrees
            frame = pygame.surfarray.make_surface(frame)
            frame = pygame.transform.scale(frame, (game.get('WIDTH'), game.get('HEIGHT')+ 200))

        game.hovershift1 = (game.get('rectw') * (1 - game.get('scalex')) * .5 * game.get('initialize1'), game.get('recth') * (1 - game.get('scaley')) * .5 * game.get('initialize1'))
        game.hovershift2 = (game.get('rectw') * (1 - game.get('scalex1')) * .5 * game.get('initialize2'), game.get('recth') * (1 - game.get('scaley1')) * .5 * game.get('initialize2'))
        game.hovershift3 = (game.get('rectw') * (1 - game.get('scalex2')) * .5 * game.get('initialize3'), game.get('recth') * (1 - game.get('scaley2')) * .5 * game.get('initialize3'))
            
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
