#!/usr/bin/python

from PIL import Image, ImageTk
import tkinter
import time
import keyboard
import os
import pytesseract
import datetime
from PIL import ImageGrab
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def Option():

    def Test():
        x1=int(x1Option.get())
        y1=int(y1Option.get())
        x2=int(x2Option.get())
        y2=int(y2Option.get())
        test=ImageGrab.grab(bbox=(x1,y1,x2,y2))
        test.save('test.png')
        load=Image.open('test.png')
        render=ImageTk.PhotoImage(load)
        img=tkinter.Label(option, image=render)
        img.image=render
        img.grid(row=7)


    def Apply():
        Log=open('Log.txt','w')
        Log.write(x1Option.get()+'\n')
        Log.write(y1Option.get()+'\n')
        Log.write(x2Option.get()+'\n')
        Log.write(y2Option.get()+'\n')
        Log.close()
        
    option=tkinter.Toplevel(window)
    option.title('option')
    option.geometry('400x300')
    titleOption=tkinter.Label(option, text='Option').grid()
    
    x1Option=tkinter.StringVar()
    y1Option=tkinter.StringVar()
    x2Option=tkinter.StringVar()
    y2Option=tkinter.StringVar()
    
    x1OptionT=tkinter.Label(option, text='X coordinate of the TOP LEFT of the gold: ').grid(row=1,column=0)
    x1OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=x1Option).grid(row=1,column=1)
    y1OptionT=tkinter.Label(option, text='Y coordinate of the TOP LEFT of the gold: ').grid(row=2,column=0)
    y1OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=y1Option).grid(row=2,column=1)
    x2OptionT=tkinter.Label(option, text='X coordinate of the BOTTOM RIGHT of the gold: ').grid(row=3,column=0)
    x2OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=x2Option).grid(row=3,column=1)
    y2OptionT=tkinter.Label(option, text='Y coordinate of the BOTTOM RIGHT of the gold: ').grid(row=4,column=0)
    y2OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=y2Option).grid(row=4,column=1)
    clear=tkinter.Label(option, text='    ').grid(row=5, column=0)
    TestButton=tkinter.Button(option, text='Test', command=Test).grid(row=6,column=0)
    ApplyButton=tkinter.Button(option, text='Apply', command=Apply).grid(row=6, column=1)




def RunGold():
    x=0
    while x==0:
        GoldLog=open('Gold.txt','r')
        last_line=GoldLog.readlines()
        OldGold=last_line[len(last_line)-1]
        GoldLog.close()
        OldGold=int(OldGold)
        if keyboard.is_pressed('tab'):
            x=1
            time.sleep(1)
            Log=open('Log.txt','r')
            last_line = Log.readlines()
            y2=last_line[len(last_line)-1]
            x2=last_line[len(last_line)-2]
            y1=last_line[len(last_line)-3]
            x1=last_line[len(last_line)-4]
            Log.close()
            x1=int(x1)
            y1=int(y1)
            x2=int(x2)
            y2=int(y2)
            image = ImageGrab.grab(bbox=(x1,y1,x2,y2))
            image.save('money.png')
            previousdata()
            time.sleep(1)
            img=Image.open('money.png')
            NewGold=pytesseract.image_to_string(img)
            os.remove('money.png')
            NewGold=NewGold.replace('.','')
            NewGold=NewGold.replace('','')                                                 
            NewGold=NewGold.replace(' ','')
            if NewGold!='':
                NewGold=int(NewGold)
                money=tkinter.Label(text=NewGold, bg='white').grid(row=1, column=1)
                currentDT = datetime.datetime.now()
                data=tkinter.Label(text=currentDT, bg='white').grid(row=2, column=1)
                window.update()
                EarnGold=NewGold-OldGold
                EarnGold=str(EarnGold)
                OldGold=NewGold
                NewGold=str(NewGold)
                earned=tkinter.Label(text=EarnGold, bg='white').grid(row=4, column=1)
                if OldGold!=NewGold:
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
                    window.update()

def previousdata():
    GoldRecord=open('GoldRecord.txt','r')
    last_line=GoldRecord.readlines()
    previousdata=last_line[len(last_line)-1]
    GoldRecord.close()
    previousdata=previousdata[0:26]
    previousdata=tkinter.Label(text=previousdata, bg='white').grid(row=3, column=1)

def RunDoublon():
    

def Run():
    RunGold()
    RunDoublon()
                
NewGold=0
data=0
earned=0
window = tkinter.Tk()
window.title('Sea Of Thieves Counter')
window.geometry('600x300')
BGimg=tkinter.PhotoImage(file='BG.png')
label1=tkinter.Label(image=BGimg).place(x = 0,y = 0)
previousdata()
line1=tkinter.Label(text='').grid(row=0, column=0)
title = tkinter.Label(text='SEA OF THIEVES COUNTER',bd=0, bg='white', font='Courier').grid(row=0, column=0)
line1=tkinter.Label(text='Your current gold: ', bg='white').grid(sticky="W", row=1, column=0)
money=tkinter.Label(text=NewGold, bg='white').grid(row=1, column=1)
line2=tkinter.Label(text='Last money check: ', bg='white').grid(sticky="W", row=2, column=0)
data=tkinter.Label(text=data, bg='white').grid(row=2, column=1)
line3=tkinter.Label(text='Previous money check: ', bg='white').grid(sticky="W", row=3, column=0)
line4=tkinter.Label(text='Gold earned between the two previous checks:             ', bg='white').grid(sticky="W", row=4, column=0)
earned=tkinter.Label(text=earned, bg='white').grid(row=4, column=1)
line5=tkinter.Label(text='To update the counter press refresh and, on the game, press TAB', bg='white').grid(sticky="W", row=5, column=0, columnspan=2)
option=tkinter.Button(text='refresh', command=Run, bg='gray').grid(row=10, column=1)
option=tkinter.Button(text='option', command=Option, bg='gray').grid( sticky="SE", row=10, column=10)


window.mainloop()





