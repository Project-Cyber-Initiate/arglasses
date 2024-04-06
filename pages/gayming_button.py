from main import pygame
import os
import sys
import subprocess
import flappybird.flappybird as flappybirdgame
# from main import WIDTH, HEIGHT
# import screen from main
pygame.init()
draw_params = []
# print (WIDTH)
display_info = pygame.display.Info()
WIDTH = display_info.current_w * .76
HEIGHT = display_info.current_h * .76

games = {
    'flappybird': None,
    'basketrandom': None
}
def run_oled_code():
    oled_script_path = r"C:\Users\veerk\Downloads\arglasses software\OLED_Module_Code\OLED_Module_Code\RaspberryPi\python\example\OLED_1in51_search_test.py"
    subprocess.run(["python", oled_script_path])

Red = (255, 0, 0)
currentGame = None
clicks = 0

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
            draw_params = []
        else:
            draw_params.append((game.get("screen").blit, (basketrandom, (int(WIDTH * 0.381), int(HEIGHT * 0.357)))))
            draw_params.append((game.get("screen").blit, (flappybird, (int(WIDTH * 0.678), int(HEIGHT * 0.357)))))
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

def ready():
    for game in {
        'flappybird': flappybirdgame,
        'basketrandom': None
    }.items():
        if (game[1] != None):
            games[game[0]] = game[1].main()

def draw(game):
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])
    if (currentGame != None):
        game.get('screen').blit(currentGame(), (0, 0))