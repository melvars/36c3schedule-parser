#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13
import json
import time
import requests
from datetime import date
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont

font_size = 14

epd = epd2in13.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

image = Image.new('1', (epd2in13.EPD_HEIGHT, epd2in13.EPD_WIDTH), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', font_size)

resp = json.load(open("everything.schedule.json"))
print("marvin ist nicht toll")
days = resp['schedule']['conference']['days']
conferences = []
for day in days:
    for room in day['rooms']:
        for conference in day['rooms'][room]:
            conf_date = datetime.strptime(conference['date'].split('+')[0], '%Y-%m-%dT%H:%M:%S')
            offset = conf_date - datetime.now()
            if offset.seconds / 3600 < 3 and offset.seconds/3600 > 0 and offset.days==0:
                print(offset.seconds / 3600)
                conferences.append(conference)
sorted_list = sorted(conferences, key=lambda i: i['date'])
print(sorted_list)

for i in range(1, 6):
    draw.text((0, font_size * i + 2), conferences[i - 1]['title'], font=font, fill=0)
epd.display(epd.getbuffer(image))

# time.sleep(10)
# epd.Clear(0xFF)
epd.sleep()