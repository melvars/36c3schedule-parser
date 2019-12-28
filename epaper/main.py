#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

font_size = 14

try:
    epd = epd2in13.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    
    # Drawing on the image
    image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
    
    draw = ImageDraw.Draw(image)    
    font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', font_size)
    draw.text((0, 0), 'Guten Tag!', font=font, fill=0)
    draw.text((0, font_size + 2), 'Marvin ist toll!', font=font, fill=0)
    epd.display(epd.getbuffer(image))
    # time.sleep(10)
    # epd.Clear(0xFF)
    epd.sleep()
        
except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()

