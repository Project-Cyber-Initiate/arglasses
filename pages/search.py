import pygame

draw_params = []

clicks = 0

def search(game, event):
    global click, draw_params
    
    clicks += 1
    box = pygame.Rect(0, 0, 200, 32)
    text = str(clicks)
    font = pygame.font.Font(None, 32)
    text = font.render(text, True, (255, 255, 255))
    draw_params = []
    draw_params.append((pygame.draw.rect, (game.get('screen'), (0, 0, 0), box)))
    draw_params.append((game.get('screen').blit, (text, (10, 10))))

def draw(game):
    if len(draw_params) > 0:
        for params in draw_params:
            params[0](*params[1])