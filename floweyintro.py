
from pygame import *
from random import *
from math import *
size = width,height = 1000,750
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
font.init()
comicSansFont = font.SysFont("Consolas",30)
mixer.init()
musicChannel = mixer.Channel(0)
musicChannel2 = mixer.Channel(1)
floweySound = mixer.Sound("Sound/characters/flowey.ogg")
floweyTheme = mixer.Sound("Sound/themes/flowey.ogg")

heart=image.load("Pictures/heart.png")
normalFlowey = image.load("Pictures/flowey/flowey.jpg")
X,Y=0,1
guy=[X,Y,480,400]
floweyCombat = image.load("Pictures/combat/floweyfight.jpg")
floweyText = open("combattext/flowey/floweyintro.txt")
floweyTalking = image.load("Pictures/flowey/floweyTalking.jpg")
textBox = image.load("Pictures/combat/text.jpg")
script = floweyText.readlines()

guy = image.load("Pictures/guy/guy009.png")

def floweyIntro():
    for i in range(2):
        screen.fill(BLACK)
        display.flip()
        time.wait(150)
        screen.blit(guy,(guy[2],guy[3]))
#        screen.blit(pics[2][2],(guy[2],guy[3]))
        display.flip()
        time.wait(150)
    #musicChannel2.play(floweyTheme)
    screen.blit(floweyCombat,(0,0))
    screen.blit(normalFlowey,(389,155))
    display.flip()

def drawFont(text):
    screen.blit(textBox,(600,175))
    fx = 650
    fy = 195
    count = 0
#    if text == script[8]:
    for char in text:
#        if not musicChannel2.get_busy():
#            musicChannel2.play(floweyTheme)
        if count%6 == 0:
            screen.blit(floweyTalking,(389,155))
        else:
            screen.blit(normalFlowey,(389,155))
        inc = 0
        if char == "\n":
            fx=fx
        elif char == "~":
            fx=650
            fy+=35
        else:
            if char == "," or char == "." or char == "!": 
                inc = 400
            char = comicSansFont.render(char,True,BLACK)
            screen.blit(char,(fx,fy))
            display.flip()
            #if count%30==0:
                #musicChannel.play(floweySound)
            count+=1
            fx+=15
            time.wait(65+inc)
    time.wait(3000)
    
floweyIntro()
time.wait(300)
for i in script:
    drawFont(i)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    print(mx,my)
floweyText.close()
quit()
 
