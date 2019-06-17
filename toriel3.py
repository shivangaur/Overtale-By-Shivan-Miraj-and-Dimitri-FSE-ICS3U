from pygame import *
from math import *

startTime=time.get_ticks()

init()
size = width, height = 1000,750
screen = display.set_mode(size)

heartPic=image.load("Pictures/heart.png")

badPic=image.load("Pictures/combat/torielFightSpikes.png")

heart=[500,335,0,True, 0]

BLACK=(0,0,0)

WHITE=(255,255,255)

X=0
Y=1

badGuys = [[0,0], [200,0], [400,0], [600, 0],[800, 0],[1000, 0]]

myClock = time.Clock()
myClock.tick(60)


def moveBadGuys(badGuys, goodX, goodY):
    ''' The AI for the badGuys is real simple. If the goodGuy is left/right
        they move left/right. Same with up/down.
        badGuys - A list of bad guy positions ([x,y] lists)
        goodX, goodY - good guy position
    '''
    for guy in badGuys:
        if goodX > guy[0]:
            guy[0]+=3                   
        elif goodX < guy[0]-25:   
            guy[0]-=3        
        if goodY > guy[1]:
            guy[1]+=3
        elif goodY < guy[1]-25:
            guy[1]-=3

def drawScene(screen, badGuys, goodX, goodY):
    ''' The scene is very simple. Each bad guy is a red circle, and the good guy is
        a green circle.
    '''
    screen.fill((0,0,0))
    for guy in badGuys:
        draw.circle(screen, WHITE, guy, 10)

    screen.blit(heartPic,(heart[X],heart[Y]))
    display.flip
    
def moveHeart(heart):
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



def checkCollide(guy):
    X, Y = 0, 1
    count=0
    collideCenter = (int(guy[X]), int(guy[Y]))
    if screen.get_at(collideCenter) == WHITE:
        print("ur ded")

#def badGuys


running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    showTime = (time.get_ticks()-startTime)//1000

    print(showTime)

    moveHeart(heart)
    drawScene(screen,badGuys,heart[X]+25,heart[Y]-25)
    moveBadGuys(badGuys, heart[X], heart[Y])
    checkCollide(heart)
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    myClock.tick(60)
    display.flip() 

quit()
