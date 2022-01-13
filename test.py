from PIL import Image, ImageTk
from PIL import ImageGrab
from PIL import Image
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

print(x1)
print(y1)
print(x2)
print(y2)
