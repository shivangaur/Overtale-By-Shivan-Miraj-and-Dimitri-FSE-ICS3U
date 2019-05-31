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
heart = [475,600,50,50]
heartRect = Rect(heart[X],heart[Y],50,50)
heartPic=image.load("Pictures/heart.png")
normalFlowey = image.load("Pictures/flowey/flowey.jpg")
guy=[X,Y,480,400]
heart=[460,450,50,50]
floweyCombat = image.load("Pictures/combat/floweyfight.jpg")
floweyText = open("combattext/flowey/floweyintro.txt")
floweyTalking = image.load("Pictures/flowey/floweyTalking.jpg")
textBox = image.load("Pictures/combat/text.jpg")
fightBox = image.load("Pictures/combat/fightBox.png")
floweyScript = floweyText.readlines()



##def combatIntro():
##    for i in range(2):
##        screen.fill(BLACK)
##        display.flip()
##        time.wait(150)
##        screen.blit(pics[2][2],(guy[2],guy[3]))
##        display.flip()
##        time.wait(150)
##    screen.blit(floweyCombat,(0,0))
##    display.flip()

##def drawPellets():
##    for i in range(50,250,5):
##        ellipseRect1=Rect(485-i,130,20,20)
##        ellipseRect2=Rect(485+i,130,20,20)
##        draw.ellipse(screen,WHITE,(ellipseRect1),10)
##        draw.ellipse(screen,WHITE,(ellipseRect2),10)
##        display.flip()
##        screenshot = screen.copy()
##        screen.blit(floweyCombat,(0,0))
##        screen.blit(textBox,(600,175))
##        screen.blit(normalFlowey,(389,155))
##        display.flip()
##    for i in range(50,80,5):
##        screen.blit(screenshot,(0,0))
##        ellipseRect3=Rect(485-2*i,130-i,20,20)
##        ellipseRect4=Rect(485+2*i,130-i,20,20)
##        ellipseRect5=Rect(485,150-i-50,20,20)
##        draw.ellipse(screen,WHITE,(ellipseRect3),10)
##        draw.ellipse(screen,WHITE,(ellipseRect4),10)
##        draw.ellipse(screen,WHITE,(ellipseRect5),10)
##        display.flip()
##        screen.blit(textBox,(600,175))
##        screen.blit(normalFlowey,(389,155))
##        display.flip()
##    screenshot = screen.copy()
##    pellets = True

##def floweyFont(text):
##    screenshotVar = False
##    screen.blit(textBox,(600,175))
##    fx = 650
##    fy = 195
##    count = 0
##    if text == floweyScript[7]:
##        drawPellets()
##    for char in text:
##        if pellets:
##            screen.blit(screenshot,(0,0))
##        inc = 0
##        if screenshotVar:
##            screen.blit(screenshot2,(600,175))
##        if char == "\n":
##            fx = fx
##        elif char == "~":
##            fx = 650
##            fy+=35
##        else:
##            if char == "," or char == "." or char == "!": 
##                inc = 400
##            char = consolas.render(char,True,BLACK)
##            screen.blit(char,(fx,fy))
##            if not musicChannel2.get_busy():
##                musicChannel2.play(floweyTheme)
##            if count%6 == 0:
##                screen.blit(floweyTalking,(389,155))
##            else:
##                screen.blit(normalFlowey,(389,155))
##            if count%15==0:
##                musicChannel.play(floweySound)
##            display.flip()
##            count+=1
##            fx+=15
##            screenshot2 = screen.copy().subsurface(600,175,362,171)
##            screenshotVar = True
##            time.wait(65+inc)
##    screenshot = screen.copy()
##    time.wait(1500)

##def drawFight():
##    screen.blit(fightBox,(500,600))
##    screen.blit(heartPic,(heart[X],heart[Y]))
##    display.flip()

def make3D(text):
    script = text.readlines()
    box = []
    sentence = []
    word = []
    for i in script:
        for j in i:
            if not j == " " and not j == "\n":
                word.append(j)
            else:
                sentence.append(word)
                word =  []
        box.append(sentence)
        sentence = []
    return box

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

def movePellets(k):
    if k == 7 and ellipseRect1[0] >=250:
        ellipseRect1=Rect(485-x,130-x,20,20)
        ellipseRect2=Rect(485+x,130-x,20,20)
        ellipseRect3=Rect(485-2*x,130-x,20,20)
        ellipseRect4=Rect(485+2*x,130-x,20,20)
        ellipseRect5=Rect(485,100-x,20,20)
        x+=1
        return True
    return False
        
def checkInteraction():
    if heartRect.colliderect(ellipseRect1) or heartRect.colliderect(ellipseRect2) \
    or heartRect.collideRect(ellipseRect3) or heartRect.collideRect(ellipseRect4) \
    or heartRect.collideRect(ellipseRect5):
        return True
    return False

    
def moveHeart():
    global heart
    keys = key.get_pressed()
    if (keys[K_a] or keys[K_LEFT]):
        if heart[X]>=405:
            heart[X]-=5
    if (keys[K_d] or keys[K_RIGHT]):
        if heart[X]<=795:
            heart[X]+=5
    if (keys[K_w] or keys[K_UP]):
        if heart[Y]>=505:
            heart[Y]-=5
    if (keys[K_s] or keys[K_DOWN]):
        if heart[Y]<=695:
            heart[Y]+=5

def drawScene(var,el1,el2,el3,el4,el5):
    screen.blit(floweyCombat,(0,0))
    if count%15==0:
        musicChannel.play(floweySound)
    if count%6 == 0:
        screen.blit(floweyTalking,(389,155))
    else:
        screen.blit(normalFlowey,(389,155))
    if not musicChannel2.get_busy():
        musicChannel2.play(floweyTheme)
    if text:
        character = consolasFont.render(floweyScript[k][j][i],BLACK,True)
        screen.blit(textBox,(600,175))
        screen.blit(character,(fx,fy))
        fx+=13
        if fx>=730:
            fx = 650
            fy+=35
        if i+1 == len(floweyScript[k][j]):
            i = 0
            j+=1
        if j+1 == len(floweyScript[k]):
            k+=1
            j = 0
        if k+1 == len(floweyScript):
            text = False
    if var:
        draw.ellipse(screen,WHITE,el1)
        draw.ellipse(screen,WHITE,el2)
        draw.ellipse(screen,WHITE,el3)
        draw.ellipse(screen,WHITE,el4)
        draw.ellipse(screen,WHITE,el5)
    screen.blit(heartPic,(heart[X]-25,heart[Y]-25))
    display.flip()
    
def floweyFight():
    text = False
    music = False
    hp = 20
    count = 0
    i = 0
    j = 0
    k = 0
    fx = 650
    fy = 195
    x = 0
    running = True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        keys = key.get_pressed()
        
        moveHeart()
        movePellets(k)
        if checkInteraction():
            hp = 1
            musicChannel2.pause()
        drawScene(drawPellets())
            
floweyFight()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
floweyText.close()
quit()
 
