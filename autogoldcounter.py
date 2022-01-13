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

GoldLog=open('Gold.txt','r')
last_line = GoldLog.readlines()
OldGold=last_line[len(last_line)-1]
GoldLog.close()
OldGold=int(OldGold)

while True: 
    try:
        if keyboard.is_pressed('tab'):
            time.sleep(1)
            image = ImageGrab.grab(bbox=(1995,75,2120,110))
            image.save('money.png')
            time.sleep(1)
            img=Image.open('money.png')
            NewGold=pytesseract.image_to_string(img)
            os.remove('money.png')
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
                    GoldRecord.write(' (+')
                    GoldRecord.write(EarnGold)
                    GoldRecord.write(')\n')
                    GoldRecord.close()
                    NewOldGold=open('Gold.txt','a')
                    NewOldGold.write(NewGold)
                    NewOldGold.write('\n')
                    NewOldGold.close()
                    time.sleep(600)
                    print('New Tab waiting')
                    
    except:
        break
