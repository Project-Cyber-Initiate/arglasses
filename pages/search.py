import pygame
import os
import sys

pygame.init()
draw_params = []

# Set the new dimensions
display_info = pygame.display.Info()
WIDTH = display_info.current_w - 100
HEIGHT = display_info.current_h - 100

Red = (255, 0, 0)
clicks = 0

def is_even(number):
    return number % 2 == 0

# Adjusted sizes based on proportions of WIDTH and HEIGHT
search_surface = pygame.transform.scale(pygame.image.load(os.path.join('png', 'google search.webp')),
                                       (int(WIDTH * 0.339), int(HEIGHT * 0.357)))
background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'justbackground.png')),
                                    (int(WIDTH * 0.678), int(HEIGHT * 0.357)))

def show(game, event, buttonsnum):
    global clicks, draw_params
    clicks += 1
    try:
        if len(draw_params) > 0:
            draw_params = []
            pass
        else:
            draw_params.append((game.get("screen").blit, (background, (int(WIDTH * 0.211), int(HEIGHT * 0.329)))))
            draw_params.append((game.get("screen").blit, (search_surface, (int(WIDTH * 0.381), int(HEIGHT * 0.329)))))
    except Exception as e:
        print("Error:", e)
        pass

def event(game, event):
    pass

def ready():
    pass

def hide():
    global draw_params
    draw_params = []
    pass

def draw(game):
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])
