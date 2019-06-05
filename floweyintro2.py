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
screenVar = False
screenshot = screen.copy()
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

def make3D(text):
    script = text.readlines()
    box = []
    sentence = []
    word = []
    for i in script:
        for j in i:
            if j.isalpha() or j == "?" or j == "!" or j == "'" or j == "," or j == ".":
                word.append(j)
            else:
                if len(word)>0:
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

def moveHeart(heart):
    keys = key.get_pressed()
    if (keys[K_a] or keys[K_LEFT]):
        if heart[X]>=305:
            heart[X]-=5
    if (keys[K_d] or keys[K_RIGHT]):
        if heart[X]<=680:
            heart[X]+=5
    if (keys[K_w] or keys[K_UP]):
        if heart[Y]>=385:
            heart[Y]-=5
    if (keys[K_s] or keys[K_DOWN]):
        if heart[Y]<=615:
            heart[Y]+=5

def drawFloweyScene(count,fx,fy,text,k,j,i,floweyScript,heart):
    global screenVar
    global screenshot
    screen.blit(floweyCombat,(0,0))
    screen.blit(textBox,(600,175))
    screen.blit(heartPic,(heart[X]-25,heart[Y]-25))
    if j == 0 and i == 0 and count % 12 == 0:
        screen.blit(textBox,(600,175))
        #draw.rect(screen,WHITE,(650,190,285,141))
    else:
        if screenVar:
            screen.blit(screenshot,(600,175))
    if count % 30 == 0 and text:
        screen.blit(floweyTalking,(389,155))
    else:
        screen.blit(normalFlowey,(389,155))
    if text:
##        if count % 100 == 0:
##            musicChannel.play(floweySound)
##        if not musicChannel2.get_busy():
##            musicChannel2.play(floweyTheme)
        if count % 12 == 0:
            character = consolas.render(floweyScript[k][j][i],True,BLACK)
            screen.blit(character,(fx,fy))
            screenVar = True
    display.flip()
    screenshot = screen.copy().subsurface(600,175,362,171)

def floweyFight():
    hp = 20
    count = 0
    i = 0
    j = 0
    k = 0
    fx = 650
    fy = 200
    x = 0
    floweyScript = make3D(floweyText)
    text = True
    running = True
#600 175
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        keys = key.get_pressed()
        moveHeart(heart)
        drawFloweyScene(count,fx,fy,text,k,j,i,floweyScript,heart)
        count+=1
        if fx>=900:
            fx = 650
            fy+=35
        else:
            if count % 12 == 0: 
                fx+=15
        print(fx)
        if count % 12 == 0:
            if not i+1 == len(floweyScript[k][j]):
                i+=1
            else:
                i = 0
                if not j+1 == len(floweyScript[k]):
                    j+=1
                    if fx != 650:
                        fx+=18
                else:
                    j = 0
                    if not k+1 == len(floweyScript):
                        k+=1
                        fx = 650
                        fy = 200
                    else:
                        k = 0
                        text = False
                    
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
 
