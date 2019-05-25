from pygame import *
from random import *
from math import *
writing = True
size = width,height = 1000,750
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
font.init()
consolas = font.SysFont("Consolas",30)
mixer.init()
musicChannel = mixer.Channel(0)
musicChannel2 = mixer.Channel(1)
floweySound = mixer.Sound("Sound/characters/flowey.ogg")
floweyTheme = mixer.Sound("Sound/themes/flowey.ogg")
pellets = False
X,Y=0,1
hp = 20
lv = 1 
heart = [475,600,50,50]
heartRect = Rect(heart[X],heart[Y],50,50)
heartPic=image.load("Pictures/heart.png")
normalFlowey = image.load("Pictures/flowey/flowey.jpg")
guy=[X,Y,480,400]
heart=[460,450,50,50]
floweyCombat = image.load("Pictures/combat/floweyfight.jpg")
floweyText = open("combattext/flowey/floweyintro.txt")
floweyTextDeath = open("combattext/flowey/floweydeath.txt")
floweyTextLife = open("combattext/flowey/floweylife.txt")
floweyTalking = image.load("Pictures/flowey/floweyTalking.jpg")
textBox = image.load("Pictures/combat/text.jpg")
fightBox = image.load("Pictures/combat/fightBox.png")
floweyScript = floweyText.readlines()
floweyScriptLife = floweyTextLife.readlines()
floweyScriptDeath = floweyTextDeath.readlines()
print(floweyScriptDeath)
for text in floweyScriptDeath:
    print(text)
collision = False

def addPics(name,start,end):
    '''this function will return a LIST OF PICTURES
    They must be in a folder named 'name' and all the pictures must start with 'name'
    start,end-the range of picture numbers
    '''
    myPics=[]
    for i in range(start,end+1):
        myPics.append(image.load("Pictures/%s/%s%03d.png"%(name,name,i)))
    return myPics

pics=[addPics('guy',1,3),addPics("guy",4,6),addPics('guy',7,9),addPics('guy',10,12)]

def combatIntro():
    screen.blit(floweyCombat,(0,0))
    screen.blit(heartPic,(heart[X],heart[Y]))
    display.flip()
    
def drawPellets():
    for i in range(50,250,5):
        ellipseRect1=Rect(485-i,130,20,20)
        ellipseRect2=Rect(485+i,130,20,20)
        draw.ellipse(screen,WHITE,(ellipseRect1))
        draw.ellipse(screen,WHITE,(ellipseRect2))
        display.flip()
        screenshot = screen.copy()
        screen.blit(floweyCombat,(0,0))
        screen.blit(textBox,(600,175))
        screen.blit(normalFlowey,(389,155))
        display.flip()
    for i in range(50,80,5):
        screen.blit(screenshot,(0,0))
        ellipseRect3=Rect(485-2*i,130-i,20,20)
        ellipseRect4=Rect(485+2*i,130-i,20,20)
        ellipseRect5=Rect(485,150-i-50,20,20)
        draw.ellipse(screen,WHITE,(ellipseRect3))
        draw.ellipse(screen,WHITE,(ellipseRect4))
        draw.ellipse(screen,WHITE,(ellipseRect5))
        display.flip()
        screen.blit(textBox,(600,175))
        screen.blit(normalFlowey,(389,155))
        screen.blit(heartPIc,(heart[X],heart[Y]))
        display.flip()
    screenshot = screen.copy()
    pellets = True
    
def attackPellets(heartRect):
    ellipseRect1 = Rect(235,130,20,20)
    ellipseRect2 = Rect(735,130,20,20)
    ellipseRect3 = Rect(325,50,20,20)
    ellipseRect4 = Rect(645,50,20,20)
    ellipseRect5 = Rect(485,70,20,20)
    for i in range(120):
        screen.blit(floweyCombat,(0,0))
        ellipseRect1 = Rect(235+i,130+4*i,20,20)
        ellipseRect2 = Rect(735-i,130+4*i,20,20)
        ellipseRect3 = Rect(325+i,130+4*i,20,20)
        ellipseRect4 = Rect(645-i,130+4*i,20,20)
        ellipseRect5 = Rect(485,130+4*i,20,20)
        screen.blit(normalFlowey,(389,155))
        draw.ellipse(screen,WHITE,ellipseRect1)
        draw.ellipse(screen,WHITE,ellipseRect2)
        draw.ellipse(screen,WHITE,ellipseRect3)
        draw.ellipse(screen,WHITE,ellipseRect4)
        draw.ellipse(screen,WHITE,ellipseRect5)
        moveHeart()
        screen.blit(heartPic,(heart[X]-25,heart[Y]-25))
        display.flip()
        if heartRect.colliderect(ellipseRect1) or heartRect.colliderect(ellipseRect2)\
        or heartRect.colliderect(ellipseRect3) or heartRect.colliderect(ellipseRect4)\
        or heartRect.colliderect(ellipseRect5):
            return True
    return False
    
def floweyFont(text,hp,lv):
##    screenshotVar = False
    screen.blit(textBox,(600,175))
    fx = 650
    fy = 195
    count = 0
    if text == floweyScript[7]:
        drawPellets()
    for char in text:
##        if pellets:
##            screen.blit(screenshot,(0,0))
        inc = 0
##        if screenshotVar:
##            screen.blit(screenshot2,(600,175))
        if char == "\n":
            fx = fx
        elif char == "~":
            fx = 650
            fy+=35
        else:
            if char == "," or char == "." or char == "!": 
                inc = 400
            char = consolas.render(char,True,BLACK)
            screen.blit(char,(fx,fy))
            char = consolas.render(str(hp),True,BLACK)
            screen.blit(char,(400,700))
            char = consolas.render(str(lv),True,BLACK)
            screen.blit(char,(450,700))
            if not musicChannel2.get_busy():
                musicChannel2.play(floweyTheme)
            if count%6 == 0:
                screen.blit(floweyTalking,(389,155))
            else:
                screen.blit(normalFlowey,(389,155))
            if count%15==0:
                musicChannel.play(floweySound)
            display.flip()
            count+=1
            fx+=15
##            screenshot2 = screen.copy().subsurface(600,175,362,171)
##            screenshotVar = True
            time.wait(65+inc)
    screenshot = screen.copy()
    time.wait(1500)
    
def moveHeart():
    global heart
    keys = key.get_pressed()
    if (keys[K_a] or keys[K_LEFT]):
        if heart[X]>=305:
            heart[X]-=2
    if (keys[K_d] or keys[K_RIGHT]):
        if heart[X]<=681:
            heart[X]+=2
    if (keys[K_w] or keys[K_UP]):
        if heart[Y]>=381:
            heart[Y]-=2
    if (keys[K_s] or keys[K_DOWN]):
        if heart[Y]<=593:
            heart[Y]+=2
            
def drawFight():
    screen.blit(heartPic,(heart[X],heart[Y]))
    display.flip()

combat = True
flowey = True
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    if combat:
        if flowey:
            flowey = False
            combatIntro()
            musicChannel2.play(floweyTheme)
            #for text in floweyScript:
                #floweyFont(text,hp,lv)
        mx,my = mouse.get_pos()
        moveHeart()
        drawFight()
        if attackPellets(heartRect):
            hp = 1
            musicChannel2.pause()
            for text in floweyScriptDeath:   
                floweyFont(text,hp,lv)
        else:
            for text in floweyScriptLife:
                floweyFont(text,hp,lv)
            
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    
floweyTextDeath.close()
floweyTextLife.close()
floweyText.close()
quit()
 
