import time
import keyboard
import os
import pytesseract
import datetime
from PIL import ImageGrab
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Path to the tesseract
OldGold=0
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
            NewGold=NewGold.replace('.','')
            NewGold=NewGold.replace('','')
            NewGold=NewGold.replace(' ','')
            NewGold=int(NewGold)
            if OldGold!=NewGold:
                if NewGold!=0:
                    print(NewGold)
                    EarnGold=NewGold-OldGold
                    EarnGold=str(EarnGold)
                    OldGold=NewGold
                    NewGold=str(NewGold)
                    currentDT = datetime.datetime.now()
                    GoldRecord=open('GoldRecord.txt','a')
                    GoldRecord.write(str(currentDT))
                    GoldRecord.write(' --> ')
                    GoldRecord.write(NewGold)
                    GoldRecord.write('(+')
                    GoldRecord.write(EarnGold)
                    GoldRecord.write(')')
                    GoldRecord.close()
                    time.sleep(6)
                 
    except:
        break
