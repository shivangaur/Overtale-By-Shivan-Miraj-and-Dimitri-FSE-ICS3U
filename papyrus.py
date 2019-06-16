from pygame import *
from math import *
from random import *
init()
size = width, height = 1000,700
screen = display.set_mode(size)

WHITE=(255,255,255)


backPic=image.load("Pictures/combat/papyrusFight.jpg") #4000x500
heartPic=image.load("Pictures/heart.png")#29x31

X=0
Y=1
VY=2
BACKX=4

onGround=3

    #X  Y   VY onGround BACKGROUND
heart=[250,650,0,True, 0]



def drawScene(screen,guy):
    #rec=Rect(250,guy[Y],29,31)
    screen.blit(backPic,(guy[BACKX],0))
    #screen.blit(heartPic,(guy[X],guy[Y]))
    offset=250-guy[X]

    
    display.flip()



def moveGuy(guy):
    
    keys=key.get_pressed()

    if guy[BACKX] > -4700:
        guy[BACKX]-=10

    if keys[K_UP] and guy[onGround]:#jumping only if ON GROUND
        guy[VY]=-15 #jupming power
        guy[onGround]=False
        
    guy[Y]+=guy[VY]
    
    if guy[Y]>=650:
        guy[Y]=650   #set it on ground
        guy[VY]=0    #stop falling
        guy[onGround]=True

    guy[VY]+=0.7 #apply gravity


    display.flip()

def checkCollide(guy):
    X, Y = 0, 1
    count=0
    collideCenter = (int(heart[X]) + 25, int(heart[Y] + 25))
    if screen.get_at(collideCenter) == WHITE:
        print("ur ded")

    if screen.get_at(collideCenter) == (128,255,255):
        print("u win")


    screen.blit(heartPic, (guy[X], guy[Y]))
    display.flip()


running = True         
myClock = time.Clock()
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    moveGuy(heart)
    drawScene(screen,heart)
    checkCollide(heart)
    #checkCollision(guy,plats)
    myClock.tick(60) 
quit()
