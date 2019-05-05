#scroll1.py
#simple example of a scrolling background.
#The program uses just one picture (4000x500)
#We are drawing the background at a negative position
from pygame import *
from math import *
init()
size = width, height = 800, 600
screen = display.set_mode(size)
BLACK=(0,0,0,255)
backPic=image.load("back1.png") #4000x500
guyPic=image.load("guy.png")#29x31

X=0
Y=1
VY=2
    #X  Y  VY
guy=[0,0,0]
def checkPixelX(x,y,w,col):
    '''returns the colour of the pixel at current (x,y)'''
    cond=True
    for i in range(w):
        if screen.get_at((x+i,y))==col:
            cond=False
    return cond
    #return (-1,-1,-1)
def checkPixelY(x,y,h,col):
    '''returns the colour of the pixel at current (x,y)'''
    cond=True
    for i in range(h):
        if screen.get_at((x,y+i))==col:
            cond=False
    return cond
def drawScene(screen,guy):
##    draw.circle(screen,(255,0,0),(479,440),2)
##    draw.circle(screen,(255,0,0),(532,440),2)
##    draw.circle(screen,(255,0,0),(505,399),2)
##    draw.circle(screen,(255,0,0),(505,481),2)
    screen.blit(backPic,(-guy[X],-guy[Y]))
    screen.blit(guyPic,(480,400))
##    draw.circle(screen,(255,0,0),(479,440),2)
##    draw.circle(screen,(255,0,0),(532,440),2)
##    draw.circle(screen,(255,0,0),(505,399),2)
##    draw.circle(screen,(255,0,0),(505,481),2)
    display.flip()

def moveGuy(guy):
    keys=key.get_pressed()
    
    #print(guy[X],guy[Y])
    #print(getPixel(480,400))
    #print(screen.get_at((guy[X]+480,guy[Y]+400)))
   # if guy[X]+480<800 or guy[Y]+400<800:
   #     if screen.get_at((guy[X],guy[Y]))!=(255,255,255,255):
    if keys[K_LEFT] and guy[X]>-400:
        if checkPixelY(479,400,guyPic.get_height(),BLACK):
            guy[X]-=10
            #print(getPixel(479,440))
    if keys[K_RIGHT] and guy[X]<2267:
        if checkPixelY(532,400,guyPic.get_height(),BLACK):
            guy[X]+=10
            #print(getPixel(532,440))
           
           
    if keys[K_UP] and guy[Y]>-480:
        if checkPixelX(480,399,guyPic.get_width(),BLACK):
            guy[Y]-=10
            #print(getPixel(505,399))
    if keys[K_DOWN] and guy[Y]<800:
        if checkPixelX(480,481,guyPic.get_width(),BLACK):
            guy[Y]+=10
            #print(getPixel(505,481))
            #if keys[K_SPACE] and guy[Y]==450:#jumping only if ON GROUND
             #   guy[VY]=-15 #jupming power
            #print(guy[X],guy[Y])
            #guy[Y]+=guy[VY]
            
            #if guy[Y]>=450:
             #   guy[Y]=450   #set it on ground
              #  guy[VY]=0    #stop falling

            #guy[VY]+=0.7 #apply gravity

running = True         
myClock = time.Clock()
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
##    points=[(guy[X]-1,guy[Y]),(guy[X]+52,guy[Y]),(guy[X],guy[Y]+80),(guy[X],guy[Y]-1)]
##    for p in points:
##        if screen
                
    moveGuy(guy)
    drawScene(screen,guy)
##    draw.circle(screen,(255,0,0),(479,440),2)
##    draw.circle(screen,(255,0,0),(532,440),2)
##    draw.circle(screen,(255,0,0),(505,399),2)
##    draw.circle(screen,(255,0,0),(505,481),2)
    myClock.tick(60) 
quit()
