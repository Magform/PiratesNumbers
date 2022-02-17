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
import tkinter.font
import webbrowser
pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR/tesseract.exe"




def Option():


    def Test():
        
        if x1Option.get()=='' or y1Option.get()=='' or x2Option.get()=='' or y2Option.get()=='' or x1dOption.get()=='' or y1dOption.get()=='' or x2dOption.get()=='' or y2dOption.get()=='':
             error=tkinter.Toplevel(window)
             error.title('Error')
             error.iconbitmap(icon)
             error.geometry('200x25')
             error=tkinter.Label(error, text='Error: all spaces must be filled ').grid()

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
             error.iconbitmap(icon)
             error.geometry('200x25')
             error=tkinter.Label(error, text='Error: all spaces must be filled').grid()

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
             error.iconbitmap(icon)
             error.geometry('215x25')
             error=tkinter.Label(error, text='Error: the first 2 spaces must be filled ').grid()
             
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
             error.iconbitmap(icon)
             error.geometry('215x25')
             error=tkinter.Label(error, text='Error: the first 2 spaces must be filled ').grid()
             
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
        TestPr.iconbitmap(icon)
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
                    Log.write(x1)
                    Log.write(y1)
                    Log.write(x2)
                    Log.write(y2)
                    Log.write(x1d)
                    Log.write(y1d)
                    Log.write(x2d)
                    Log.write(y2d)
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
    option.iconbitmap(icon)
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
            NewGold=NewGold.replace('>','')
            
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
            NewDoubloons=NewDoubloons.replace('«','')

            previousdata()
            currentDT = datetime.datetime.now()
            data=tkinter.Label(text=currentDT, bg='white').grid(row=6, column=1)
            window.update()
            
            if NewGold!='':
                money=tkinter.Label(text=NewGold, bg='white').grid(row=2, column=1)
                NewGold=int(NewGold)
                window.update()
                EarnGold=NewGold-OldGold
                EarnGold=str(EarnGold)
                OldGold=NewGold
                NewGold=str(NewGold)
                EarnGold=EarnGold.replace('\n','')
                earned=tkinter.Label(text=EarnGold, bg='white').grid(row=3, column=1)
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
                money=tkinter.Label(text=NewDoubloons, bg='white').grid(row=4, column=1)
                NewDoubloons=int(NewDoubloons)
                EarnDoubloons=NewDoubloons-OldDoubloons
                EarnDoubloons=str(EarnDoubloons)
                OldDoubloons=NewDoubloons
                NewDoubloons=str(NewDoubloons)
                EarnDoubloons=EarnDoubloons.replace('\n','')
                earned=tkinter.Label(text=EarnDoubloons, bg='white').grid(row=5, column=1)
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
    previousdata=tkinter.Label(text=previousdata, bg='white').grid(row=7, column=1)


def update():
    sloopo=int(sloop.get())
    brigantineo=int(brigantine.get())
    galliono=int(gallion.get())
    total.set(sloopo+brigantineo+galliono)
    
def SaveData():
    Ssloop=sloop.get()
    Sbrigantine=brigantine.get()
    Sgallion=gallion.get()
    SS=open('sinked.txt','w')
    SS.write(Ssloop+'\n')
    SS.write(Sbrigantine+'\n')
    SS.write(Sgallion+'\n')
    SS.close()
    update()

def credit():

    def open(url):
        webbrowser.open_new(url)
    
    credit=tkinter.Toplevel(window)
    credit.title('Credit')
    credit.iconbitmap(icon)
    credit.geometry('420x600')
    creditTitle =tkinter.font.Font( family = 'Courier', weight = "bold", size=12)
    creditSubTitle =tkinter.font.Font(family='Courier', size=11)
    fntTitle =tkinter.font.Font( family = "Comic Sans MS", size = 20, weight = "bold")
    titleOption=tkinter.Label(credit, text='Credit', font=fntTitle).grid(columnspan=2)
    
    credit1=tkinter.Label(credit, text='Conception, realization and development:', font=creditTitle).grid(sticky="W", row=1, column=0)
    name1=tkinter.Label(credit, text='Nicolas "Magform" Ferraresso ', fg="black", cursor="hand2")
    name1.grid(sticky="W", row=2, column=0)
    name1.bind("<Button-1>", lambda e: open("https://magform.github.io/nicolasferraresso/"))
    clear=tkinter.Label(credit, text='').grid(row=3, column=0)
    credit3=tkinter.Label(credit, text='Various idea and suggestion:', font=creditTitle).grid(sticky="W", row=4, column=0)
    
    name2=tkinter.Label(credit, text='Sunken boat idea:  Damiano Cerioni', fg="black", cursor="hand2")
    name2.grid(sticky="W", row=5, column=0)
    name2.bind("<Button-2>", lambda e: open(''))
 
NewGold=0
data=0
earnedGold=0
NewDoubloons=0
earnedDoubloons=0
window = tkinter.Tk()
icon = 'icon.ico'
window.title('Pirates number')
window.iconbitmap(icon)
window.geometry('1000x400')
window.resizable(width=False, height=False)
BGimg=tkinter.PhotoImage(file='BG.png')
label1=tkinter.Label(image=BGimg).place(x = 0,y = 0)
previousdata()
clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=0, column=0)
fntTitle =tkinter.font.Font( family = "Comic Sans MS", size = 20, weight = "bold")
titleL = tkinter.Label(text='Pirates number',font=fntTitle, bg='white', bd=0).grid(row=0, column=1, columnspan=10)
counterlabel=tkinter.Label(text='Counter: ', bg='white', font='family').grid(sticky='W', row=1, column=0)
line1=tkinter.Label(text='Your current gold: ', bg='white').grid(sticky="W", row=2, column=0)
money=tkinter.Label(text=NewGold, bg='white').grid(row=2, column=1)
line4=tkinter.Label(text='Gold earned from last check:             ', bg='white').grid(sticky="W", row=3, column=0)
earned=tkinter.Label(text=earnedGold, bg='white').grid(row=3, column=1)
line1=tkinter.Label(text='Your current doubloons: ', bg='white').grid(sticky="W", row=4, column=0)
money=tkinter.Label(text=NewDoubloons, bg='white').grid(row=4, column=1)
line4=tkinter.Label(text='Doubloons earned from last check:             ', bg='white').grid(sticky="W", row=5, column=0)
earned=tkinter.Label(text=earnedDoubloons, bg='white').grid(row=5, column=1)
line2=tkinter.Label(text='Last check: ', bg='white').grid(sticky="W", row=6, column=0)
line3=tkinter.Label(text='Previous check: ', bg='white').grid(sticky="W", row=7, column=0)
line5=tkinter.Label(text='To update the counter press refresh and, on the game, press TAB', bg='white').grid(sticky="W", row=8, column=0, columnspan=2)

clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=1, column=2)

Log=open('sinked.txt','r')
last_line = Log.readlines()
galliono=last_line[len(last_line)-1]
brigantineo=last_line[len(last_line)-2]
sloopo=last_line[len(last_line)-3]
Log.close()
galliono=galliono.replace('\n','')
brigantineo=brigantineo.replace('\n','')
sloopo=sloopo.replace('\n','')
gallion=tkinter.StringVar()
gallion.set(galliono)
brigantine=tkinter.StringVar()
brigantine.set(brigantineo)
sloop=tkinter.StringVar()
sloop.set(sloopo)
total=tkinter.StringVar()
update()

counterlabel=tkinter.Label(text='Sunken boats: ', bg='white', font='family').grid(sticky='W', row=1, column=3)
sloopcounterlabel=tkinter.Label(text='sloops: ', bg='white').grid(sticky='W', row=2, column=3)
brigantinecounterlabel=tkinter.Label(text='brigantines: ', bg='white').grid(sticky='W', row=3, column=3)
gallioncounterlabel=tkinter.Label(text='gallions: ', bg='white').grid(sticky='W', row=4, column=3)
totallabel=tkinter.Label(text='total sunken boats: ', bg='white').grid(sticky='W', row=5, column=3)

clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=1, column=4)
sloopcounter=tkinter.Entry(width=5, borderwidth=2, textvariable=sloop).grid(sticky="W", row=2,column=5)
brigantinecounter=tkinter.Entry(width=5, borderwidth=2, textvariable=brigantine).grid(sticky="W", row=3,column=5)
gallioncounter=tkinter.Entry(width=5, borderwidth=2, textvariable=gallion).grid(sticky="W", row=4,column=5)
totalcounter=tkinter.Entry(width=5, borderwidth=2, textvariable=total, state='disable').grid(sticky="W", row=5,column=5)

clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=9, column=9)
refresh=tkinter.Button(text='refresh', command=Run, bg='gray').grid(row=10, column=1)
savedata=tkinter.Button(text='save', command=SaveData, bg='gray').grid(row=10, column=5)
option=tkinter.Button(text='option', command=Option, bg='gray').grid( sticky="SE", row=10, column=10)

clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=99, column=99)
clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=98, column=99)
clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=97, column=99)
clear=tkinter.Label(text='                              ', bg='white').grid(sticky='W', row=96, column=99)
clear=tkinter.Label(text='    ', bg='white').grid(sticky='W', row=96, column=98)
credit=tkinter.Button(text='credit', command=credit).grid(sticky='SE', row=100, column=100)
window.mainloop()

