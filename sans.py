from pygame import *
from math import *
from random import *
size=width,height=1000,750
screen=display.set_mode(size)

startTime=time.get_ticks()

RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

heartPic=image.load("Pictures/heart.png")
X=0
Y=1


gameOver=image.load("Pictures/gameOver.png")

heart=[600,650]


balls=[i*75 for i in range (0,15)] 
balls1=[]
for ba in balls:
    balls1.append([ba,0])



##for ball in balls:
##    draw.circle(screen,WHITE,ball,11)
##
##    #if ball[Y]>=650:
        
    



myClock=time.Clock()

def drawScene(screen,balls1,heart):
    gravityY=7
    gravityX=7
    screen.fill((0,0,0))
    screen.blit(heartPic,(heart[X],heart[Y]))
    draw.line(screen,WHITE,(545,0),(545,750),10)
    for ball in balls1:
        draw.circle(screen,(255,255,255),ball,9)
        ball[Y]+=gravityY
        if ball[Y]>=700:
            gravityY *= -1
        if ball[Y]<=0:
            gravityY*= -1

        ball[X]+=gravityX
        if ball[X]>=700:
            gravityX *=-1
        if ball[X]<=0:
            gravityX*=-1

            
    display.flip()


def moveHeart(heart):
    keys = key.get_pressed()
    if (keys[K_a] or keys[K_LEFT]):
        if heart[X]>=550:
            heart[X]-=5
    if (keys[K_d] or keys[K_RIGHT]):
        if heart[X]<=950:
            heart[X]+=5
    if (keys[K_w] or keys[K_UP]):
        if heart[Y]>=60:
            heart[Y]-=5
    if (keys[K_s] or keys[K_DOWN]):
        if heart[Y]<=650:
            heart[Y]+=5
    if keys[K_ESCAPE]:
        quit()

def checkCollide(guy):
    X, Y = 0, 1
    count=0
    collideCenter = (int(guy[X]), int(guy[Y]))
    if screen.get_at(collideCenter) == WHITE:
        print("jhsdjfhhasdfjksdfbfdhdjasf")
        page = "game over"

def gameOver():
    screen.blit(gameOver,(0,0))
    

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    showTime = (time.get_ticks()-startTime)//1000

    print(showTime)

    if showTime >= 26:
        print("done")

                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    
    drawScene(screen,balls1,heart)
    moveHeart(heart)
    checkCollide(heart)
    myClock.tick(60)
    display.flip() 
page = "main"

if page == "game over":
    gameOver()

quit()
