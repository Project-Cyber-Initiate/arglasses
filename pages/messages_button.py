from main import game, pygame
import os
import subprocess
import sys

pygame.init()
draw_params = []

# Set the new dimensions
display_info = pygame.display.Info()

WIDTH = game.WIDTH
HEIGHT = game.HEIGHT

Red = (255, 0, 0)
clicks = 0

def is_even(number):
    return number % 2 == 0

# Adjusted sizes based on proportions of WIDTH and HEIGHT
messages = pygame.transform.scale(pygame.image.load(os.path.join('png', 'nomessages.png')),
                                  (int(WIDTH* .6), int(HEIGHT*.6)))
background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'justbackground.png')),
                                    (int(WIDTH * 1.1), int(HEIGHT)))

def run_oled_code():
    return
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_messages_test.py"
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
            draw_params.append((game.get("screen").blit, (background, (int(WIDTH * 0.042), int(HEIGHT * 0.07)))))
            draw_params.append((game.get("screen").blit, (messages, (int(WIDTH * 0.169), int(HEIGHT * 0.143)))))
            run_oled_code()
    except Exception as e:
        print("Drawing Error:", e)
        pass

def event(game, event):
    pass

def ready():
    pass

def hide():
    global draw_params
    draw_params = []
    pass


def oled ():
    run_oled_code2

def draw(game):
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])
