import pygame

# returnvalue: (obj, draw function)
def search(game, event):
    box = pygame.Rect(0, 0, 200, 32)
    return (box, pygame.draw.rect)