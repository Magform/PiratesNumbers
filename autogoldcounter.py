#!/usr/bin/python

import tkinter
import time
import keyboard
import os
import pytesseract
import datetime
from PIL import ImageGrab
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

GoldRecord=open('GoldRecord.txt','r')
last_line = GoldRecord.readlines()
OldGold=last_line[len(last_line)-1]
GoldRecord.close()
OldGold= OldGold[31:]
OldGold=int(OldGold)
print(1)

while True: 
    try:
        if keyboard.is_pressed('tab'):
            time.sleep(1)
            image = ImageGrab.grab(bbox=(1995,75,2120,110))
            image.save('money.png')
            time.sleep(1)
            img=Image.open('money.png')
            NewGold=pytesseract.image_to_string(img)
            NewGold=NewGold.replace('.','')
            NewGold=NewGold.replace('','')
            NewGold=NewGold.replace(' ','')
            if NewGold!='':
                NewGold=int(NewGold)
                if OldGold!=NewGold:
                    EarnGold=NewGold-OldGold
                    EarnGold=str(EarnGold)
                    OldGold=NewGold
                    NewGold=str(NewGold)
                    currentDT = datetime.datetime.now()
                    print(str(currentDT))
                    print(' --> ')
                    print(NewGold)
                    print('(+')
                    print(EarnGold)
                    print(')')
                    GoldRecord=open('GoldRecord.txt','a')
                    GoldRecord.write(str(currentDT))
                    GoldRecord.write(' --> ')
                    GoldRecord.write(NewGold)
                    GoldRecord.write('(+')
                    GoldRecord.write(EarnGold)
                    GoldRecord.write(')')
                    GoldRecord.close()
                    time.sleep(600)
                    
    except:
        break
