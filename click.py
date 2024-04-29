import pygame

mouse_x, mouse_y = pygame.mouse.get_pos()

def click (mouse_x, mouse_y, rectx, recty, rectw, recth, offsetX, offsetY):

    if rectx*.3 <= mouse_x <= rectx*.3 + rectw and recty*.2 <= mouse_y <= recty*.2 + recth:
        if pygame.mouse.get_pressed()[0]:
            print ("search click")
        
    elif rectx*.3 <= mouse_x <= rectx*.3 + rectw and recty <= mouse_y <= recty + recth:
        # print("Mouse is over rectangle 2")
        None
        
    elif rectx*.3 <= mouse_x <= rectx*.3 + rectw and recty*1.8 <= mouse_y <= recty*1.8 + recth:
        # print("Mouse is over rectangle 3")
        None
    else:
        None