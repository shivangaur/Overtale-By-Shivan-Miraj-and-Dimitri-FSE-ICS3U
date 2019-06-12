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
consolas = font.SysFont("Consolas",29)
mixer.init()
musicChannel = mixer.Channel(0)
musicChannel2 = mixer.Channel(1)
floweySound = mixer.Sound("Sound/characters/flowey.ogg")
floweyTheme = mixer.Sound("Sound/themes/flowey.ogg")
screenVar = False
screenshot = screen.copy()
X,Y=0,1
k = 0
j = 0
i = 0
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
            if j.isalpha() or j == "?" or j == "!" or j == "'" or j == "," or j == "." or j == "~":
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

def movePellets(move,els,k,count):
    if move:
        if count <= 100:
            els[0][0]-= 2
            els[1][0]+= 2
            els[2][0]-= 4
            els[2][1]-= 1
            els[3][0]+= 4
            els[3][1]-= 1
            els[4][1]-= 1
        else:
            if count >= 1200:
                els[0][0] += 1
                els[1][0] -= 1
                els[2][0] += 1
                els[3][0] -= 1
                els[0][1] += 2
                els[1][1] += 2
                els[2][1] += 2
                els[3][1] += 2
                els[4][1] += 2
        count += 1
    return els,count

def update(count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount):
    floweyText = open("combattext/flowey/floweyintro.txt")
    floweyScript = make3D(floweyText)
    count+=1
    els,pelletCount = movePellets(pellets,els,k,pelletCount)
    if floweyScript[k][j][i] == "~":
        if count % 12 == 0:
            fx = 650
            fy += 35
            moveText = False
    if moveText:
        if count % 12 == 0:
            fx+=15
    if count % 12 == 0:
        if not i+1 == len(floweyScript[k][j]):
            i+=1
            moveText = True
        else:
            i = 0
            if not j+1 == len(floweyScript[k]):
                j+=1
                if fx != 650:
                    fx+=15
            else:
                j = 0
                if not k+1 == len(floweyScript):
                    k+=1
                    fx = 650
                    fy = 200
                    if k == 8:
                        pellets = True
                else:
                    k = 0
                    text = False
    return count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount

def drawFloweyScene(count,fx,fy,text,k,j,i,floweyScript,heart,moveText,pellets,els):
    global screenVar
    global screenshot
    screen.blit(floweyCombat,(0,0))
    draw.rect(screen,BLACK,(0,650,1000,100))
    screen.blit(textBox,(600,175))
    screen.blit(heartPic,(heart[X]-25,heart[Y]-25))
    if pellets:
        draw.ellipse(screen,WHITE,els[0])
        draw.ellipse(screen,WHITE,els[1])
        draw.ellipse(screen,WHITE,els[2])
        draw.ellipse(screen,WHITE,els[3])
        draw.ellipse(screen,WHITE,els[4]) 
    if j == 0 and i == 0 and count % 12 == 0:
        screen.blit(textBox,(600,175))
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
            if floweyScript[k][j][i] != "~":
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
    floweyScript = make3D(floweyText)
    text = True
    running = True
    moveText = True
    pellets = False
    els = [Rect(485,130,20,20),Rect(485,130,20,20),Rect(485,130,20,20),Rect(485,130,20,20),Rect(485,150,20,20)]
    pelletCount = 0
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
                
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        keys = key.get_pressed()
        moveHeart(heart)
        drawFloweyScene(count,fx,fy,text,k,j,i,floweyScript,heart,moveText,pellets,els)
        count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount = update(count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount)      
                    
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
 
