import pygame.ftfont
from main import game, pygame, offsetX, offsetY, openai
import os
import sys
import subprocess

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
search_surface = pygame.transform.scale(pygame.image.load(os.path.join('png', 'google search.webp')),
                                       (int(WIDTH * 0.32), int(HEIGHT * 0.345)))
background = pygame.transform.scale(pygame.image.load(os.path.join('png', 'justbackground.png')),
                                    (int(WIDTH * 0.65), int(HEIGHT * 0.345)))

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
            draw_params.append((game.draw_surface.blit, (background, (int(WIDTH * 0.211) + offsetX, int(HEIGHT * 0.35) + offsetY / 1))))
            draw_params.append((game.draw_surface.blit, (search_surface, (int(WIDTH * 0.381) + offsetX, int(HEIGHT * 0.35) + offsetY / 1))))
            # Run OLED display code when button is clicked
            run_oled_code()
    except Exception as e:
        run_oled_code2
        print("Error:", e)
        pass

current_input = ""

ai = False

def event(game, event):
    global current_input, draw_params, ai
    if event.type == pygame.KEYDOWN and len(draw_params) > 0:
        if event.key == pygame.K_RSHIFT:
            current_input = ""
            ai = False
            draw_params = []
            draw_params.append((game.draw_surface.blit, (background, (int(WIDTH * 0.211) + offsetX, int(HEIGHT * 0.35) + offsetY / 1))))
            draw_params.append((game.draw_surface.blit, (search_surface, (int(WIDTH * 0.381) + offsetX, int(HEIGHT * 0.35) + offsetY / 1))))
        if event.key == pygame.K_RETURN and len(current_input) > 0:
            ai = True
            chat = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": current_input}
                ],
                max_tokens=150,
                stream=True
            )
            full_res = ""
            for resp in chat:
                if resp.choices[0].delta.content:
                    full_res += resp.choices[0].delta.content
                temp_params = []
                # draw_params.append((game.draw_surface.blit, (background, (int(WIDTH * 0.211) + offsetX, int(HEIGHT * 0.35) + offsetY / 1))))
                text = full_res
                text = [text[i:i+30] for i in range(0, len(text), 30)]
                for i in range(len(text)):
                    text_surface = pygame.font.Font(None, 40).render(text[i], True, (0, 0, 0))
                    temp_params.append((game.draw_surface.blit, (text_surface, (offsetX + 400, offsetY + 120 + (i * 30)))))
                draw_params = temp_params
            current_input = ""
            ai = False
        elif event.key == pygame.K_BACKSPACE: 
            current_input = current_input[:-1] 
        else: 
            current_input += event.unicode
    pass

def ready(render):
    pass

def hide():
    global draw_params
    draw_params = []

def oled ():
    run_oled_code2

def draw(game, events):
    global ai
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])

        if not ai:
            text_surface = pygame.font.Font(None, 32).render(current_input, True, (0, 0, 0)) 

            game.draw_surface.blit(text_surface, (offsetX + 560, offsetY + 240)) 