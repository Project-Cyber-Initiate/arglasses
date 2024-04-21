import pygame
import os
import sys
import subprocess

pygame.init()
draw_params = []

# Set the new dimensions
display_info = pygame.display.Info()
WIDTH = display_info.current_w * .95
HEIGHT = WIDTH/2

Red = (255, 0, 0)
clicks = 0

def is_even(number):
    return number % 2 == 0

# Adjusted sizes based on proportions of WIDTH and HEIGHT
search_surface = pygame.transform.scale(pygame.image.load(os.path.join('png', 'google search.webp')),
                                       (int(WIDTH * 0.339), int(HEIGHT * 0.357)))
background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'justbackground.png')),
                                    (int(WIDTH * 0.678), int(HEIGHT * 0.357)))

# Function to execute OLED display code
def run_oled_code():
    return
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_search_test.py"
    subprocess.Popen(["python", oled_script_path])
def run_oled_code2():
    return
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_test.py"
    subprocess.Popen(["python", oled_script_path])
    
def show(game, event, buttonsnum):
    global clicks, draw_params
    clicks += 1
    try:
        if len(draw_params) > 0:
            run_oled_code2()
            draw_params = []
            game.set('currentscreen', 'none')
        else:
            draw_params.append((game.get("screen").blit, (background, (int(WIDTH * 0.211), int(HEIGHT * 0.329)))))
            draw_params.append((game.get("screen").blit, (search_surface, (int(WIDTH * 0.381), int(HEIGHT * 0.329)))))
            # Run OLED display code when button is clicked
            run_oled_code()
    except Exception as e:
        run_oled_code2
        print("Error:", e)
        pass

def event(game, event):
    pass

def ready():
    pass

def hide():
    global draw_params
    draw_params = []

def oled ():
    run_oled_code2

def draw(game):
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])
