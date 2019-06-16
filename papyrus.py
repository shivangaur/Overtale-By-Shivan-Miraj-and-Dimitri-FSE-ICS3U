from pygame import *
from math import *
from random import *
init()
size = width, height = 500,500
screen = display.set_mode(size)

backPic=image.load("Pictures/combat/papyrusFight.jpg") #4000x500
guyPic=image.load("Pictures/heart.png")#29x31

X=0
Y=1
VY=2

onGround=3

    #X  Y   VY onGround
heart=[250,450,0,True]


def drawScene(screen,guy):
    #rec=Rect(250,guy[Y],29,31)
    screen.blit(backPic,(250-guy[X],0))
    screen.blit(guyPic,(250,guy[Y]))
    offset=250-guy[X]

    
    display.flip()



def moveGuy(guy):
    
    keys=key.get_pressed()
    
    guy[X]+=10
    
    if keys[K_UP] and guy[onGround]:#jumping only if ON GROUND
        guy[VY]=-10 #jupming power
        guy[onGround]=False
        
    guy[Y]+=guy[VY]
    
    if guy[Y]>=450:
        guy[Y]=450   #set it on ground
        guy[VY]=0    #stop falling
        guy[onGround]=True

    guy[VY]+=0.7 #apply gravity


running = True         
myClock = time.Clock()
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    moveGuy(heart)
    drawScene(screen,heart)
    #checkCollision(guy,plats)
    myClock.tick(60) 
quit()
