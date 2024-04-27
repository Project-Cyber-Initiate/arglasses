import pygame
import sys
import os 
#import cv2
#import numpy as np
from pygame.locals import *
from PIL import Image, ImageFilter
import base64
import time

# import button
# Initialize Pygame
pygame.init()

import click
import button
import subprocess

# Define screen dimensions and FPS
display_info = pygame.display.Info()
WIDTH = display_info.current_w * 0.885
HEIGHT = WIDTH/2
FPS = 30
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
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)

screen.set_colorkey((0, 0, 0))
pygame.display.set_caption("arglasses")

buttonsnum = 0

# Define colors
# color: (255,255,255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
rectw = WIDTH//6.5
recth = HEIGHT//4
recty = HEIGHT//2.5 - recth/2
rectx = WIDTH//12
rectx_2 = rectx * 0.3

hovershift1 = 0.0
hovershift2 = 0.0
hovershift3 = 0.0
hover_background1 = 0
hover_background2 = 0
hover_background3 = 0

def run_oled_code():
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_test.py"
    process = subprocess.Popen(["python", oled_script_path], stdin=subprocess.PIPE, stdout=sys.stdout, stderr=sys.stderr, text=True)
    
    def send(data):
        try:
            process.stdin.write(data + "\n")
            process.stdin.flush()
        except:
            pass
    
    def read():
        return process.stdout.readline()
    
    return (send, read)

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
                if key == 'currentscreen':
                    sendToChild(f"SCREEN.{value}")
                if key in ['hover_background1', 'hover_background2', 'hover_background3']:
                    game.render += 1
                if key in ['hover_background1']:
                    game.search = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search.png')), (game.get('rectw')*game.get('scalex')*.9, game.get('recth')*game.get('scaley'))))
                    game.search_background = (pygame.transform.scale(pygame.image.load(os.path.join('png', 'search_background.png')), (game.get('rectw')*game.get('scalex')*2*game.get('hover_background1'), game.get('recth')*game.get('scaley')*1.2)))
                if key in ['hover_background2']:
                    game.gayming = pygame.transform.scale(pygame.image.load(os.path.join('png', 'gayming.png')), (game.get('rectw')*game.get('scalex1')*.85, game.get('recth')*game.get('scaley1')))
                    game.gayming_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'Gayming_background.png')), (game.get('rectw')*game.get('scalex1')*game.get('hover_background2')*2.1, game.get('recth')*game.get('scaley1')*1.2))
                if key in ['hover_background3']:
                    game.messages = pygame.transform.scale(pygame.image.load(os.path.join('png', 'messages.png')), (game.get('rectw')*game.get('scalex2')*.9, game.get('recth')*game.get('scaley2')))
                    game.messages_background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'texts_background.png')), (game.get('rectw')*game.get('scalex2')*game.get('hover_background3')*2, game.get('recth')*game.get('scaley2')*1.2))
                if key == 'render':
                    onDraw(passImage)
            except Exception as e:
                print(e)
                pass
        self.__dict__[key] = value
    

game = Game()

for key, value in zip(
    ['pygame', 'click', 'clock', 'display_info', 'WIDTH', 'HEIGHT', 'FPS', 'scalex', 'scaley', 'scalex1', 'scaley1', 'scalex2', 'scaley2', 'scx', 'scy', 'initialize1', 'initialize2', 'initialize3', 'cap', 'screen', 'WHITE', 'RED', 'rectw', 'recth', 'recty', 'rectx', 'rectx_2', 'hovershift1', 'hovershift2', 'hovershift3', 'hover_background1', 'hover_background2', 'hover_background3', 'running', 'currentscreen', 'render', 'draw_surface'], 
    [pygame, click, pygame.time.Clock(), display_info, WIDTH, HEIGHT, FPS, scalex, scaley, scalex1, scaley1, scalex2, scaley2, scx, scy, initialize1, initialize2, initialize3, cap, screen, WHITE, RED, rectw, recth, recty, rectx, rectx_2, hovershift1, hovershift2, hovershift3, hover_background1, hover_background2, hover_background3, True, 'none', 0, pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)]
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

    sendToChild, readFromChild = run_oled_code()

    game.draw_surface.convert_alpha()

    def passImage():
        imgscreen = pygame.Surface((256, 128), pygame.SRCALPHA, 32)
        imgscreen = imgscreen.convert_alpha()
        pygame.transform.scale(game.draw_surface, (256, 128), imgscreen)
        
        # Flip the image horizontally
        imgscreen = pygame.transform.flip(imgscreen, True, False)
        
        # grayscale image
        buffer = pygame.image.tobytes(imgscreen, "RGBA")

        sendToChild("IMAGE")
        sendToChild(str(base64.b64encode(buffer)))
        
    waitDraw = []
    def onDraw(fn):
        waitDraw.append(fn)

    def draw_window(events):
        game.draw_surface.fill(pygame.Color(0, 0, 0, 0))
        game.draw_surface.blit(game.get('search_background'), (game.get('rectx') * .3 + game.get('hovershift1')[0], game.get('recty') * .2 + game.get('hovershift1')[1]-10))
        game.draw_surface.blit(game.get('search'), (game.get('rectx') * .3 + game.get('hovershift1')[0], game.get('recty') * .2 + game.get('hovershift1')[1]))
        game.draw_surface.blit(game.get('gayming_background'), (game.get('rectx') * .3 + game.get('hovershift2')[0], game.get('recty') + game.get('hovershift2')[1]-10))
        game.draw_surface.blit(game.get('gayming'), (game.get('rectx') * .3 + game.get('hovershift2')[0] + 10, game.get('recty') + game.get('hovershift2')[1]+4))
        game.draw_surface.blit(game.get('messages_background'), (game.get('rectx') * .3 + game.get('hovershift3')[0], game.get('recty')*1.8 + game.get('hovershift3')[1]-15))
        game.draw_surface.blit(game.get('messages'), (game.get('rectx') * .3 + game.get('hovershift3')[0], game.get('recty')*1.8 + game.get('hovershift3')[1]))

        for draw in draws:
            draw(game, events)

        overlay_surface = pygame.transform.scale(game.draw_surface, (WIDTH, HEIGHT / 1.6))

        game.screen.fill(pygame.Color(255, 255, 255))
        game.screen.blit(overlay_surface, (0, 0))

        pygame.display.flip()

        for fn in waitDraw:
            fn()

        waitDraw.clear()
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
        events = pygame.event.get()
        for event in events:
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
                    game.set('currentscreen', 'search')
                    pages.search.show(game, event, buttonsnum)
                    pages.gayming_button.hide()
                    pages.messages_button.hide()
                elif game.get('initialize2'):
                    searchdown = 0
                    game.set('currentscreen', 'gayming')
                    pages.gayming_button.show(game, event, buttonsnum)
                    pages.search.hide()
                    pages.messages_button.hide()
                elif game.get('initialize3'):
                    searchdown = 0
                    game.set('currentscreen', 'messages')
                    pages.messages_button.show(game, event, buttonsnum)
                    pages.search.hide()
                    pages.gayming_button.hide()
                game.render += 1
            
        # print(game.get('initialize2'))
        # ret, frame = (None, None)#cap.read()
        # if ret:
        #     # Convert the OpenCV frame to a Pygame surface
        #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     frame = np.rot90(frame)  # Rotate the frame 90 degrees
        #     frame = pygame.surfarray.make_surface(frame)
        #     frame = pygame.transform.scale(frame, (game.get('WIDTH'), game.get('HEIGHT')+ 200))

        game.hovershift1 = (game.get('rectw') * (1 - game.get('scalex')) * .5 * game.get('initialize1'), game.get('recth') * (1 - game.get('scaley')) * .5 * game.get('initialize1'))
        game.hovershift2 = (game.get('rectw') * (1 - game.get('scalex1')) * .5 * game.get('initialize2'), game.get('recth') * (1 - game.get('scaley1')) * .5 * game.get('initialize2'))
        game.hovershift3 = (game.get('rectw') * (1 - game.get('scalex2')) * .5 * game.get('initialize3'), game.get('recth') * (1 - game.get('scaley2')) * .5 * game.get('initialize3'))
            
        # hovershift2 = initialize2

        # Draw the window
        draw_window(events)
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
