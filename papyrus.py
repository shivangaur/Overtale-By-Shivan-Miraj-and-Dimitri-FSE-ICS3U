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
heart1=[250,650,0,True, 0]



def papyrus():
    myClock=time.Clock()
    running=True
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
        
        screen.blit(backPic,(heart1[BACKX],0))
        #screen.blit(heartPic,(guy[X],guy[Y]))
        offset=250-heart1[X]
            
        keys=key.get_pressed()

        if heart1[BACKX] > -4700:
            heart1[BACKX]-=10   #the background is what is moving

        if keys[K_UP] and heart1[onGround]:#jumping only if ON GROUND
            heart1[VY]=-15 #jupming power
            heart1[onGround]=False                
        heart1[Y]+=heart1[VY]
            
        if heart1[Y]>=650:
            heart1[Y]=650   #set it on ground
            heart1[VY]=0    #stop falling
            heart1[onGround]=True

        heart1[VY]+=0.7 #apply gravity


        collideCenter = (int(heart1[X]) + 25, int(heart1[Y] + 25))
        if screen.get_at(collideCenter) == WHITE:
            print("ur ded")

        if screen.get_at(collideCenter) == (128,255,255):
            print("u win")


        screen.blit(heartPic, (heart1[X], heart1[Y]))

        myClock.tick(60)
        
        if key.get_pressed()[27]:
            running=False
            
        display.flip()
    return "m"
    
        


page= "m"
while page!="exit":
    if page == "m":
        page = papyrus()




quit()
