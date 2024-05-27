import pygame.ftfont
from main_yt import game, pygame, offsetX, offsetY, openai
import os
import sys
import subprocess
from threading import Thread

draw_params = []
text_draws = []

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
    global clicks, draw_params, text_draws
    clicks += 1
    try:
        if len(draw_params) > 0:
            run_oled_code2()
            draw_params = []
            text_draws = []
            game.set('currentscreen', 'none')
            scroller.set_text("")   
        else:
            ai = False
            draw_params.append((game.draw_surface.blit, (background, (int(WIDTH * 0.211) + 50 + offsetX, int(HEIGHT * 0.35) + offsetY / 1.6))))
            draw_params.append((game.draw_surface.blit, (search_surface, (int(WIDTH * 0.381) + 50 + offsetX, int(HEIGHT * 0.35) + offsetY / 1.6))))
            # Run OLED display code when button is clicked
            run_oled_code()
    except Exception as e:
        run_oled_code2
        print("Error:", e)
        pass

current_input = ""

class Scroller:
    def __init__(self, game):
        self.position = 0
        self.text = ""
        self.game = game
    def set_text(self, text):
        self.text = text
        self.draw()
    def event(self, event):
        if event.type == pygame.MOUSEWHEEL:
            print(event, self.position)
            self.position -= event.y
            numLines = len(self.text) / 20
            if self.position < 0:
                self.position = 0
            elif self.position >= numLines * 5 + 5:
                self.position = 5 * numLines

            self.draw()
            #self.position = max(0, min(len(self.text), self.position))
            # game.render += 1
    def draw(self):
        global text_draws
        text_draws = []
        maxLines = 7
        lines = int(self.position / 5)
        text = [self.text[i:i+20] for i in range(0, len(self.text), 20)]
        otext = text.copy()
        if len(otext) < 1:
            otext = [" "]
        text = text[max(0, lines - maxLines):]
        text_draws.append((pygame.draw.rect, (self.game.draw_surface, (200, 200, 200), (offsetX + 870, offsetY + 70, 10, 400))))
        text_draws.append((pygame.draw.rect, (self.game.draw_surface, (110, 110, 110), (offsetX + 870, offsetY + 70 + max(0, 400 * ((lines - 7) / len(otext))), 10, 40))))
        for i in range(len(text)):
            if i <= maxLines:
                text_surface = pygame.font.Font(None, 60).render(text[i], True, (0, 0, 0))
                text_draws.append((self.game.draw_surface.blit, (text_surface, ((offsetX + 400, offsetY + 70 + (i * 50))))))

ai = False
scroller = None

def event(game, event):
    global current_input, draw_params, ai, scroller, text_draws
    if event.type == pygame.MOUSEBUTTONDOWN and len(text_draws) > 0:
        print(event.pos)
        if event.button == 1:
            if pygame.Rect(offsetX + 850, (offsetY + 70) / 1.6, 10, 400 / 1.6).collidepoint(event.pos):
                scroller.position = event.pos[1] - offsetY - 70
    if event.type == pygame.MOUSEWHEEL and len(draw_params) > 0:
        scroller.event(event)
    if event.type == pygame.KEYDOWN and len(draw_params) > 0:
        if event.key == pygame.K_RSHIFT:
            current_input = ""
            ai = False
            draw_params = []
            text_draws = []
            draw_params.append((game.draw_surface.blit, (background, (int(WIDTH * 0.211) + offsetX, int(HEIGHT * 0.35) + offsetY / 1.6))))
            draw_params.append((game.draw_surface.blit, (search_surface, (int(WIDTH * 0.381) + offsetX, int(HEIGHT * 0.35) + offsetY / 1.6))))
        if event.key == pygame.K_RETURN and len(current_input) > 0:
            ai = True
            def gpt():
                global current_input, ai, draw_params, scroller
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
                current_input = ""
                for resp in chat:
                    if resp.choices[0].delta.content:
                        full_res += str(resp.choices[0].delta.content)
                    draw_params = [(lambda: None, [])]
                    if scroller:
                        scroller.set_text(full_res)
                    #draw_params.append((game.draw_surface.blit, (background, (int(WIDTH * 0.211) + offsetX, int(HEIGHT * 0.35) + offsetY / 1.6))))
                    text = full_res
                    text = [text[i:i+20] for i in range(0, len(text), 20)]
                    for i in range(len(text)):
                        pass
                        #text_surface = pygame.font.Font(None, 80).render(text[i], True, (0, 0, 0))
                        #temp_params.append((game.draw_surface.blit, (text_surface, (offsetX + 400, offsetY + 120 + (i * 30)))))
                    #temp_params.append((lambda: None, []))
                    #draw_params = temp_params
                current_input = ""
            Thread(target=gpt).start()
        elif event.key == pygame.K_BACKSPACE: 
            current_input = current_input[:-1] 
        else: 
            current_input += event.unicode
    pass

def ready(render, game):
    global scroller
    scroller = Scroller(game)
    pass

def hide():
    global draw_params, text_draws
    text_draws = []
    draw_params = []

def oled ():
    run_oled_code2

def draw(game, events):
    global ai
    global scroller
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])
        if not ai and len(current_input) > 0:
            text_surface = pygame.font.Font(pygame.font.match_font('sfnsmono'), 26).render(current_input, True, (0, 0, 0)) 

            game.draw_surface.blit(text_surface, (offsetX + 475, (offsetY)/1.6 + 290)) 
    if len(text_draws) > 0 and ai:
        for params in text_draws:
            params[0](*params[1])