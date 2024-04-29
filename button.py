scx = 0.85
scy = 0.85


def button(tup):
    ((mouse_x, mouse_y), rectx, recty, rectw, recth, offsetX, offsetY) = tup

    if rectx*.3 <= mouse_x-offsetX <= rectx*.3 + rectw and (recty*.2/1.6) <= (mouse_y-offsetY/1.6) <= recty*.2/1.6 + recth/1.6:
        # print("Mouse is over the rectangle!")
        return (
            scx, # scalex
            scy, # scaley
            1, # scalex1
            1, # scaley1
            1, # scalex2
            1, # scaley2
            1, # initialize1
            0, # initialize2
            0, # initialize3
            1,
            0,
            0
        )
        
    elif rectx*.3 <= mouse_x-offsetX <= rectx*.3 + rectw and (recty/1.6) <= (mouse_y-offsetY/1.6) <= recty/1.6 + (recth)/1.6:
        # print("Mouse is over rectangle 2")
        return (
            1, # scalex
            1, # scaley
            scx, # scalex1
            scy, # scaley1
            1, # scalex2
            1, # scaley2
            0, # initialize1
            1, # initialize2
            0, # initialize3
            0,
            1,
            0
        )
    elif rectx*.3 <= mouse_x-offsetX <= rectx*.3 + rectw and (recty*1.8/1.6) <= (mouse_y-offsetY/1.6) <= recty*1.8/1.6 + (recth)/1.6:
        # print("Mouse is over rectangle 3")
        return (
            1, # scalex
            1, # scaley
            1, # scalex1
            1, # scaley1
            scx, # scalex2
            scx, # scaley2
            0, # initialize1
            0, # initialize2
            1, # initialize3
            0,
            0, 
            1
        )
    else:
        return (
            1, # scalex
            1, # scaley
            1, # scalex1
            1, # scaley1
            1, # scalex2
            1, # scaley@
            0, # initialize1
            0, # initialize2
            0, # initialize
            0,
            0,
            0
        )