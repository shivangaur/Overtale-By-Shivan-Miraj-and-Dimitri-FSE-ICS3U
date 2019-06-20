from pygame import *
from math import *

startTime=time.get_ticks()

init()
size = width, height = 1000,750
screen = display.set_mode(size)

heartPic=image.load("Pictures/heart.png")




heart2=[500,335,0,True, 0]



BLACK=(0,0,0)

WHITE=(255,255,255)


X=0
Y=1
VY=2
BACKX=4
onGround=3

badGuys = [[0,0], [200,0], [400,0], [600, 0],[800, 0],[1000, 0]]

myClock = time.Clock()
myClock.tick(60)


def moveBadGuys(badGuys, goodX, goodY): #the enemy balls (put in the
                                        #badguys list) will follow the
                                        #heart's position (goodX,goodY)

    for guy in badGuys:
        if goodX > guy[0]:
            guy[0]+=3                   
        elif goodX < guy[0]-25:   
            guy[0]-=3        
        if goodY > guy[1]:
            guy[1]+=3
        elif goodY < guy[1]-25:
            guy[1]-=3

def drawTorielFight(screen, badGuys, goodX, goodY):#draws the heart and background

    screen.fill((0,0,0))
    for guy in badGuys:
        draw.circle(screen, WHITE, guy, 10)

    screen.blit(heartPic,(heart2[X],heart2[Y]))
    display.flip
    
def moveHeart(heart):#keys used to move the heart
    keys = key.get_pressed()
    if (keys[K_a] or keys[K_LEFT]):
        if heart[X]>=50:
            heart[X]-=5
    if (keys[K_d] or keys[K_RIGHT]):
        if heart[X]<=950:
            heart[X]+=5
    if (keys[K_w] or keys[K_UP]):
        if heart[Y]>=50:
            heart[Y]-=5
    if (keys[K_s] or keys[K_DOWN]):
        if heart[Y]<=650:
            heart[Y]+=5



def checkCollideToriel(guy): #checks if the heart collides with
                       #any white areas
    X, Y = 0, 1
    count=0
    collideCenter = (int(guy[X]), int(guy[Y]))
    if screen.get_at(collideCenter) == WHITE:
        print("ur ded")

def toriel():
    myClock=time.Clock()
    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        moveHeart(heart2)
        drawScene(screen,badGuys,heart2[X]+25,heart2[Y]-25)
        moveBadGuys(badGuys, heart2[X], heart2[Y])
        checkCollide(heart2)

        myClock.tick(60)
        showTime = (time.get_ticks()-startTime)//1000

        print(showTime)

        if key.get_pressed()[27]:
            running=False

        

        display.flip()
    return "m"
        

#def badGuys




##    moveHeart(heart2)
##    drawScene(screen,badGuys,heart2[X]+25,heart2[Y]-25)
##    moveBadGuys(badGuys, heart2[X], heart2[Y])
##    checkCollide(heart2)


page = "m"
while page != "exit":
    if page == "m":
        page=toriel()



quit()
