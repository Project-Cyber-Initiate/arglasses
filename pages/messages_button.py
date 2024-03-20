import pygame
import os
import sys
pygame.init()
draw_params = []
display_info = pygame.display.Info()
WIDTH = display_info.current_w - 100
HEIGHT = display_info.current_h - 100


Red = (255, 0, 0)

clicks = 0

def is_even(number):
    return number % 2 == 0

messages = pygame.transform.scale(pygame.image.load(os.path.join('png', 'nomessages.png')), (900,500))
background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'justbackground.png')), (1200,600))

def show(game, event, buttonsnum):
    global clicks, draw_params
    clicks += 1
    try:
        if len(draw_params) > 0:
            draw_params = []
            pass
        else:
            draw_params.append((game.get("screen").blit, (background, (50, 75))))
            draw_params.append((game.get("screen").blit, (messages, (200, 100))))
    except Exception as e:
        print("Drawing Error:", e)
        pass

def event(game, event):
    pass

def hide():
    global draw_params
    draw_params = []
    pass

def draw(game):
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])