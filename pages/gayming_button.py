from main import game, pygame, passImage
import os
import sys
import subprocess
import flappybird.flappybird as flappybirdgame
import time

_game = game

draw_params = []
display_info = pygame.display.Info()
# Setting the new dimensions

games = {
    'flappybird': None,
    'basketrandom': None
}
def run_oled_code():
    return
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_gaming_test.py"
    subprocess.Popen(["python", oled_script_path])
def run_oled_code2():
    return
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_test.py"
    subprocess.Popen(["python", oled_script_path])

Red = (255, 0, 0)
currentGame = None
clicks = 0

WIDTH = game.WIDTH
HEIGHT = game.HEIGHT

def is_even(number):
    return number % 2 == 0

# Adjusted sizes based on proportions of WIDTH and HEIGHT
basketrandom = pygame.transform.scale(pygame.image.load(os.path.join('png', 'basketrandom_logo.jpg')),
                                      (int(WIDTH * 0.169), int(HEIGHT * 0.286)))
flappybird = pygame.transform.scale(pygame.image.load(os.path.join('png', 'flappybird_logo.png')),
                                     (int(WIDTH * 0.169), int(HEIGHT * 0.286)))

def show(game, event, buttonsnum):
    global clicks, draw_params
    clicks += 1
    box = pygame.Rect(0, 0, int(WIDTH * 0.169), int(HEIGHT * 0.046))
    text = str(clicks)
    font = pygame.font.Font(None, int(WIDTH * 0.046))
    text = font.render(text, True, (255, 255, 255))
    try:
        if len(draw_params) > 0:
            run_oled_code2()
            draw_params = []
            game.set('currentscreen', 'none')
        else:
            draw_params.append((game.draw_surface.blit, (basketrandom, (int(WIDTH * 0.381), int(HEIGHT * 0.357)))))
            draw_params.append((game.draw_surface.blit, (flappybird, (int(WIDTH * 0.678), int(HEIGHT * 0.357)))))
            run_oled_code()
    except Exception as e:
        print("Error:", e)
        pass

def set_game(name):
    global currentGame
    if name in games:
        currentGame = games[name]
    else:
        currentGame = None

def event(game, event):
    global currentGame
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if pygame.Rect(int(WIDTH * 0.381), int(HEIGHT * 0.357), int(WIDTH * 0.169), int(HEIGHT * 0.286)).collidepoint(event.pos):
                print("Basketrandom")
            if pygame.Rect(int(WIDTH * 0.678), int(HEIGHT * 0.357), int(WIDTH * 0.169), int(HEIGHT * 0.286)).collidepoint(event.pos):
                set_game("flappybird")
    pass

def hide():
    global draw_params
    draw_params = []
    pass

on = None

def oled ():
    run_oled_code2

def ready():
    for game in {
        'flappybird': flappybirdgame,
        'basketrandom': None
    }.items():
        if (game[1] != None):
            name = game[0]
            fn = game[1]
            def close():
                global on
                games[name] = fn.main(close)
                set_game(None)

                time.sleep(1)
                def f():
                    passImage()
                
                on = f

            games[game[0]] = game[1].main(close)

def draw(game, events):
    global on
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])
    if (currentGame != None):
        game.draw_surface.blit(currentGame(events), (0, 0))
    if (on != None):
        on()
        on = None
