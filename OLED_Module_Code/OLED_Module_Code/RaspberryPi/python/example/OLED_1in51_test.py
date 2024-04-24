#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import re
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
import time
import traceback
from waveshare_OLED import OLED_1in51
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

currentPath = "main_page.bmp"

def picpath(path):
    return os.path.join(picdir, path)

print("listening for inputs nig")

drawbmp = None

try:
    disp = OLED_1in51.OLED_1in51()

    logging.info("\r1.51inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

    # Create blank image for drawing   
    def display():
        global drawbmp
        logging.info ("***draw image")
        Himage2 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
        if drawbmp == None:
            drawbmp = Image.open(picpath(currentPath))
        Himage2.paste(drawbmp, (0,0))
        Himage2=Himage2.rotate(180) 	
        disp.ShowImage(disp.getbuffer(Himage2)) 
        drawbmp = None
    
    display()

    def receiveImage():
        string = input()
        try:
            buffer = bytearray(map(int, string.split()))
            image = Image.frombytes('1', (disp.width, disp.height), bytes(buffer))
            image.save('amogujs.bmp')
            return ""
        except:
            return string


    while True:
        entry = input()

        if entry == "IMAGE":
            entry = receiveImage()

        match = re.match(r"^SCREEN\.(\w+)", entry)

        if not match:
            continue

        screen = match.group(1)

        print(screen)

        if screen == "search":
            currentPath = "search_oled.bmp"
            pass
        elif screen == "gayming":
            currentPath = "gaming_oled.bmp"
            pass
        elif screen == "messages":
            currentPath = "messages_oled.bmp"
            pass
        else:
            currentPath = "main_page.bmp"
            pass

        display()
    # time.sleep(3)    
    # disp.clear()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    disp.module_exit()