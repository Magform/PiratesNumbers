#!/usr/bin/python

from PIL import Image, ImageTk, ImageGrab
import tkinter
import time
import keyboard
import os
import pytesseract
import datetime
import glob
import inspect, re
import functools
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"




def Option():


    def Test():
        
        if x1Option.get()=='' or y1Option.get()=='' or x2Option.get()=='' or y2Option.get()=='' or x1dOption.get()=='' or y1dOption.get()=='' or x2dOption.get()=='' or y2dOption.get()=='':
             error=tkinter.Toplevel(window)
             error.title('Error')
             error.geometry('200x25')
             error=tkinter.Label(error, text='Error: all value need to be filled ').grid()

        else:
        
            x1=int(x1Option.get())
            y1=int(y1Option.get())
            x2=int(x2Option.get())
            y2=int(y2Option.get())
            test=ImageGrab.grab(bbox=(x1,y1,x2,y2))
            test.save('testg.png')
            x1OptionT=tkinter.Label(option, text='Gold: ').grid(sticky="W", row=14, column=0)
            load=Image.open('testg.png')
            render=ImageTk.PhotoImage(load)
            img=tkinter.Label(option, image=render)
            img.image=render
            img.grid(row=15, columnspan=2)
            os.remove('testg.png')

            x1d=int(x1dOption.get())
            y1d=int(y1dOption.get())
            x2d=int(x2dOption.get())
            y2d=int(y2dOption.get())
            test=ImageGrab.grab(bbox=(x1d,y1d,x2d,y2d))
            test.save('testd.png')
            load=Image.open('testd.png')
            render=ImageTk.PhotoImage(load)
            img=tkinter.Label(option, image=render)
            img.image=render
            x1OptionT=tkinter.Label(option, text='Doubloons: ').grid(sticky="W", row=16, column=0)
            img.grid(row=17, columnspan=2)
            os.remove('testd.png')


    def Apply():
        if x1Option.get()=='' or y1Option.get()=='' or x2Option.get()=='' or y2Option.get()=='' or x1dOption.get()=='' or y1dOption.get()=='' or x2dOption.get()=='' or y2dOption.get()=='':
             error=tkinter.Toplevel(window)
             error.title('Error')
             error.geometry('200x25')
             error=tkinter.Label(error, text='Error: all value need to be filled ').grid()

        else:
            Log=open('Log.txt','w')
            Log.write(x1Option.get()+'\n')
            Log.write(y1Option.get()+'\n')
            Log.write(x2Option.get()+'\n')
            Log.write(y2Option.get()+'\n')
            Log.write(x1dOption.get()+'\n')
            Log.write(y1dOption.get()+'\n')
            Log.write(x2dOption.get()+'\n')
            Log.write(y2dOption.get()+'\n')
            Log.close()
        

    def TestSt():

        if x1Option.get()=='' or y1Option.get()=='':
             error=tkinter.Toplevel(window)
             error.title('Error')
             error.geometry('215x25')
             error=tkinter.Label(error, text='Error: the first 2 values cannot be empty ').grid()
             
        else:
            
            x1=int(x1Option.get())
            y1=int(y1Option.get())
            x2=int(x1Option.get())+126
            y2=int(y1Option.get())+35
            x1d=int(x1Option.get())-115
            y1d=int(y1Option.get())
            x2d=int(x1Option.get())-31
            y2d=int(y1Option.get())+35
            x2=int(x2)
            y2=int(y2)
            x1d=int(x1d)
            y1d=int(y1d)
            x2d=int(x2d)
            y2d=int(y2d)
        
            test=ImageGrab.grab(bbox=(x1,y1,x2,y2))
            test.save('testg.png')
            x1OptionT=tkinter.Label(option, text='Gold: ').grid(sticky="W", row=14, column=0)
            load=Image.open('testg.png')
            render=ImageTk.PhotoImage(load)
            img=tkinter.Label(option, image=render)
            img.image=render
            img.grid(row=15, columnspan=2)
            os.remove('testg.png')
            
            test=ImageGrab.grab(bbox=(x1d,y1d,x2d,y2d))
            test.save('testd.png')
            load=Image.open('testd.png')
            render=ImageTk.PhotoImage(load)
            img=tkinter.Label(option, image=render)
            img.image=render
            x1OptionT=tkinter.Label(option, text='Doubloons: ').grid(sticky="W", row=16, column=0)
            img.grid(row=17, columnspan=2)
            os.remove('testd.png')
            

    def ApplySt():
        if x1Option.get()=='' or y1Option.get()=='':
             error=tkinter.Toplevel(window)
             error.title('Error')
             error.geometry('215x25')
             error=tkinter.Label(error, text='Error: the first 2 values cannot be empty ').grid()
             
        else:
            x1=x1Option.get()
            y1=y1Option.get()
            x2=int(x1Option.get())+126
            y2=int(y1Option.get())+35
            x1d=int(x1Option.get())-115
            y1d=int(y1Option.get())
            x2d=int(x1Option.get())-31
            y2d=int(y1Option.get())+35
            x2=str(x2)
            y2=str(y2)
            x1d=str(x1d)
            y1d=str(y1d)
            x2d=str(x2d)
            y2d=str(y2d)
        
            Log=open('Log.txt','w')
            Log.write(x1+'\n')
            Log.write(y1+'\n')
            Log.write(x2+'\n')
            Log.write(y2+'\n')
            Log.write(x1d+'\n')
            Log.write(y1d+'\n')
            Log.write(x2d+'\n')
            Log.write(y2d+'\n')
            Log.close()
        
    def TestPr():

        def Tes(fileNumber):
            path = 'preset/'
            a=0
            for filename in glob.glob(os.path.join(path, '*.txt')):
                if a==fileNumber:
                    Log=open(os.path.join(os.getcwd(), filename), 'r')
                    last_line = Log.readlines()
                    y2=last_line[len(last_line)-5]
                    x2=last_line[len(last_line)-6]
                    y1=last_line[len(last_line)-7]
                    x1=last_line[len(last_line)-8]
                    y2d=last_line[len(last_line)-1]
                    x2d=last_line[len(last_line)-2]
                    y1d=last_line[len(last_line)-3]
                    x1d=last_line[len(last_line)-4]
                    Log.close()
                    
                    y2=int(y2)
                    x2=int(x2)
                    y1=int(y1)
                    x1=int(x1)
                    y2d=int(y2d)
                    x2d=int(x2d)
                    y1d=int(y1d)
                    x1d=int(x1d)

                    
                    test=ImageGrab.grab(bbox=(x1,y1,x2,y2))
                    test.save('testg.png')
                    x1OptionT=tkinter.Label(option, text='Gold: ').grid(sticky="W", row=14, column=0)
                    load=Image.open('testg.png')
                    render=ImageTk.PhotoImage(load)
                    img=tkinter.Label(option, image=render)
                    img.image=render
                    img.grid(row=15, columnspan=2)
                    os.remove('testg.png')
            
                    test=ImageGrab.grab(bbox=(x1d,y1d,x2d,y2d))
                    test.save('testd.png')
                    load=Image.open('testd.png')
                    render=ImageTk.PhotoImage(load)
                    img=tkinter.Label(option, image=render)
                    img.image=render
                    x1OptionT=tkinter.Label(option, text='Doubloons: ').grid(sticky="W", row=16, column=0)
                    img.grid(row=17, columnspan=2)
                    os.remove('testd.png')
                    break
                else:
                    a+=1
                    
        TestPr=tkinter.Toplevel(option)
        TestPr.title('Preset')
        TestPr.geometry('300x200')
        titleOption=tkinter.Label(TestPr, text='Preset', font='Courier').grid(columnspan=2)
        path = 'preset/'
        a=0
        for filename in glob.glob(os.path.join(path, '*.txt')):
            filename=filename.replace("preset\k",'')
            filename=tkinter.Label(TestPr, text=filename).grid(sticky="W", row=a+1, column=0)
            space=tkinter.Label(TestPr, text='       ').grid(sticky="W", row=a+1, column=1)
            Button=tkinter.Button(TestPr, text='Use', command = functools.partial(Tes,a)).grid(row=a+1,column=2)
            a+=1
        titleOption=tkinter.Label(TestPr, text='to add presets add preset files in "preset\k"').grid(row=a+2)

                


    def ApplyPr():
        def Tes(fileNumber):
            path = 'preset/'
            a=0
            for filename in glob.glob(os.path.join(path, '*.txt')):
                if a==fileNumber:
                    Log=open(os.path.join(os.getcwd(), filename), 'r')
                    last_line = Log.readlines()
                    y2=last_line[len(last_line)-5]
                    x2=last_line[len(last_line)-6]
                    y1=last_line[len(last_line)-7]
                    x1=last_line[len(last_line)-8]
                    y2d=last_line[len(last_line)-1]
                    x2d=last_line[len(last_line)-2]
                    y1d=last_line[len(last_line)-3]
                    x1d=last_line[len(last_line)-4]
                    Log.close()

                    Log=open('Log.txt','w')
                    Log.write(x1+'\n')
                    Log.write(y1+'\n')
                    Log.write(x2+'\n')
                    Log.write(y2+'\n')
                    Log.write(x1d+'\n')
                    Log.write(y1d+'\n')
                    Log.write(x2d+'\n')
                    Log.write(y2d+'\n')
                    Log.close()
                    ApplyPr.destroy()
                    break
                else:
                    a+=1
                    
        ApplyPr=tkinter.Toplevel()
        ApplyPr.title('Preset')
        ApplyPr.geometry('300x200')
        titleOption=tkinter.Label(ApplyPr, text='Preset', font='Courier').grid(row=0, columnspan=2)
        path = 'preset/'
        a=0
        for filename in glob.glob(os.path.join(path, '*.txt')):
            filename=filename.replace("preset\k",'')
            filename=tkinter.Label(ApplyPr, text=filename).grid(sticky="W", row=a+1, column=0)
            space=tkinter.Label(ApplyPr, text='       ').grid(sticky="W", row=a+1, column=1)
            Button=tkinter.Button(ApplyPr, text='Use', command = functools.partial(Tes,a)).grid(row=a+1,column=2)
            a+=1
        titleOption=tkinter.Label(ApplyPr, text='to add presets add preset files in "preset\k"').grid(row=a+2)

       
    option=tkinter.Toplevel(window)
    option.title('Option')
    option.geometry('500x700')
    titleOption=tkinter.Label(option, text='Option', font='Courier').grid(columnspan=2)
    
    x1Option=tkinter.StringVar()
    y1Option=tkinter.StringVar()
    x2Option=tkinter.StringVar()
    y2Option=tkinter.StringVar()
    
    x1dOption=tkinter.StringVar()
    y1dOption=tkinter.StringVar()
    x2dOption=tkinter.StringVar()
    y2dOption=tkinter.StringVar()
    
    x1OptionT=tkinter.Label(option, text='X coordinate of the TOP LEFT of the gold: ').grid(sticky="W", row=1,column=0)
    x1OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=x1Option).grid(sticky="W", row=1,column=1)
    y1OptionT=tkinter.Label(option, text='Y coordinate of the TOP LEFT of the gold: ').grid(sticky="W", row=2,column=0)
    y1OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=y1Option).grid(sticky="W", row=2,column=1)
    x2OptionT=tkinter.Label(option, text='X coordinate of the BOTTOM RIGHT of the gold: ').grid(sticky="W", row=3,column=0)
    x2OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=x2Option).grid(sticky="W", row=3,column=1)
    y2OptionT=tkinter.Label(option, text='Y coordinate of the BOTTOM RIGHT of the gold: ').grid(sticky="W", row=4,column=0)
    y2OptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=y2Option).grid(sticky="W", row=4,column=1)

    clear=tkinter.Label(option, text=' ').grid(row=5)
    
    x1dOptionT=tkinter.Label(option, text='X coordinate of the TOP LEFT of the doubloons: ').grid(sticky="W", row=6,column=0)
    x1dOptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=x1dOption).grid(sticky="W", row=6,column=1)
    y1dOptionT=tkinter.Label(option, text='Y coordinate of the TOP LEFT of the doubloons: ').grid(sticky="W", row=7,column=0)
    y1dOptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=y1dOption).grid(sticky="W", row=7,column=1)
    x2dOptionT=tkinter.Label(option, text='X coordinate of the BOTTOM RIGHT of the doubloons: ').grid(sticky="W", row=8,column=0)
    x2dOptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=x2dOption).grid(sticky="W", row=8,column=1)
    y2dOptionT=tkinter.Label(option, text='Y coordinate of the BOTTOM RIGHT of the doubloons: ').grid(sticky="W", row=9,column=0)
    y2dOptionE=tkinter.Entry(option, width=5, borderwidth=2, textvariable=y2dOption).grid(sticky="W", row=9,column=1)

    clear=tkinter.Label(option, text=' ').grid(row=10)
    
    TestButton=tkinter.Button(option, text='Test', command=Test).grid(row=11,column=0)
    ApplyButton=tkinter.Button(option, text='Apply', command=Apply).grid(row=11, column=1)
    TestStandard=tkinter.Button(option, text='Test with standard distance', command=TestSt).grid(row=12, column=0)
    TestStandard=tkinter.Button(option, text='Apply with standard distance', command=ApplySt).grid(row=12, column=1)
    TestStandard=tkinter.Button(option, text='Test preset', command=TestPr).grid(row=13, column=0)
    TestStandard=tkinter.Button(option, text='Apply preset', command=ApplyPr).grid(row=13, column=1)





def Run():
    x=0
    while x==0:
        GoldLog=open('Gold.txt','r')
        last_line=GoldLog.readlines()
        OldGold=last_line[len(last_line)-1]
        GoldLog.close()
        OldGold=int(OldGold)
        
        DoubloonsLog=open('Doubloons.txt','r')
        last_line=DoubloonsLog.readlines()
        OldDoubloons=last_line[len(last_line)-1]
        DoubloonsLog.close()
        OldDoubloons=int(OldDoubloons)
        
        if keyboard.is_pressed('tab'):
            x=1
            time.sleep(1)
            Log=open('Log.txt','r')
            last_line = Log.readlines()
            y2=last_line[len(last_line)-5]
            x2=last_line[len(last_line)-6]
            y1=last_line[len(last_line)-7]
            x1=last_line[len(last_line)-8]
            Log.close()
            x1=int(x1)
            y1=int(y1)
            x2=int(x2)
            y2=int(y2)
            image = ImageGrab.grab(bbox=(x1,y1,x2,y2))
            image.save('money.png')
            time.sleep(1)
            img=Image.open('money.png')
            NewGold=pytesseract.image_to_string(img)
            os.remove('money.png')
            NewGold=NewGold.replace('.','')
            NewGold=NewGold.replace('','')                                                 
            NewGold=NewGold.replace(' ','')
            NewGold=NewGold.replace('\n','')
            
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
            image.save('doubloons.png')
            time.sleep(1)
            img=Image.open('doubloons.png')
            NewDoubloons=pytesseract.image_to_string(img)
            os.remove('doubloons.png')
            NewDoubloons=NewDoubloons.replace('.','')
            NewDoubloons=NewDoubloons.replace('','')                                                 
            NewDoubloons=NewDoubloons.replace(' ','')
            NewDoubloons=NewDoubloons.replace('\n','')
            NewDoubloons=NewDoubloons.replace('|','')
            NewDoubloons=NewDoubloons.replace(':','')
            NewDoubloons=NewDoubloons.replace('∞','')

            previousdata()
            currentDT = datetime.datetime.now()
            data=tkinter.Label(text=currentDT, bg='white').grid(row=5, column=1)
            window.update()
            
            if NewGold!='':
                money=tkinter.Label(text=NewGold, bg='white').grid(row=1, column=1)
                NewGold=int(NewGold)
                window.update()
                EarnGold=NewGold-OldGold
                EarnGold=str(EarnGold)
                OldGold=NewGold
                NewGold=str(NewGold)
                EarnGold=EarnGold.replace('\n','')
                earned=tkinter.Label(text=EarnGold, bg='white').grid(row=2, column=1)
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

            if NewDoubloons!='':
                money=tkinter.Label(text=NewDoubloons, bg='white').grid(row=3, column=1)
                NewDoubloons=int(NewDoubloons)
                EarnDoubloons=NewDoubloons-OldDoubloons
                EarnDoubloons=str(EarnDoubloons)
                OldDoubloons=NewDoubloons
                NewDoubloons=str(NewDoubloons)
                EarnDoubloons=EarnDoubloons.replace('\n','')
                earned=tkinter.Label(text=EarnDoubloons, bg='white').grid(row=4, column=1)
                if OldDoubloons!=NewDoubloons:
                    DoubloonsRecord=open('DoubloonsRecord.txt','a')
                    DoubloonsRecord.write(str(currentDT))
                    DoubloonsRecord.write(' --> ')
                    DoubloonsRecord.write(NewDoubloons)
                    DoubloonsRecord.write(' (+')
                    DoubloonsRecord.write(EarnDoubloons)
                    DoubloonsRecord.write(')\n')
                    DoubloonsRecord.close()
                    NewOldDoubloons=open('Doubloons.txt','a')
                    NewOldDoubloons.write(NewDoubloons)
                    NewOldDoubloons.write('\n')
                    NewOldDoubloons.close()
                    window.update()

def previousdata():
    GoldRecord=open('GoldRecord.txt','r')
    last_line=GoldRecord.readlines()
    previousdata=last_line[len(last_line)-1]
    GoldRecord.close()
    previousdata=previousdata[0:26]
    previousdata=tkinter.Label(text=previousdata, bg='white').grid(row=6, column=1)


                
NewGold=0
data=0
earnedGold=0
NewDoubloons=0
earnedDoubloons=0
window = tkinter.Tk()
window.title('Sea Of Thieves Counter')
window.geometry('600x400')
BGimg=tkinter.PhotoImage(file='BG.png')
label1=tkinter.Label(image=BGimg).place(x = 0,y = 0)
previousdata()
title = tkinter.Label(text='SEA OF THIEVES COUNTER', bg='white', font='Courier', bd=0).grid(row=0, column=0, columnspan=5)
line1=tkinter.Label(text='Your current gold: ', bg='white').grid(sticky="W", row=1, column=0)
money=tkinter.Label(text=NewGold, bg='white').grid(row=1, column=1)
line4=tkinter.Label(text='Gold earned from last check:             ', bg='white').grid(sticky="W", row=2, column=0)
earned=tkinter.Label(text=earnedGold, bg='white').grid(row=2, column=1)
line1=tkinter.Label(text='Your current doubloons: ', bg='white').grid(sticky="W", row=3, column=0)
money=tkinter.Label(text=NewDoubloons, bg='white').grid(row=3, column=1)
line4=tkinter.Label(text='Doubloons earned from last check:             ', bg='white').grid(sticky="W", row=4, column=0)
earned=tkinter.Label(text=earnedDoubloons, bg='white').grid(row=4, column=1)
line2=tkinter.Label(text='Last check: ', bg='white').grid(sticky="W", row=5, column=0)
data=tkinter.Label(text=data, bg='white').grid(row=5, column=1)
line3=tkinter.Label(text='Previous check: ', bg='white').grid(sticky="W", row=6, column=0)
line5=tkinter.Label(text='To update the counter press refresh and, on the game, press TAB', bg='white').grid(sticky="W", row=7, column=0, columnspan=2)
option=tkinter.Button(text='refresh', command=Run, bg='gray').grid(row=10, column=1)
option=tkinter.Button(text='option', command=Option, bg='gray').grid( sticky="SE", row=10, column=10)
window.mainloop()





