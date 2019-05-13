#importing what the program needs
from pygame import *
from random import *
from math import *

#making a screen
size = width,height = 1000,750
screen = display.set_mode(size)

#making basic colors
#RED = (255,0,0)   
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED=(237,28,36,255)
#declaring basic vraiables

#declaring character's x and y position and making a list of them
X = 0 #character's x position
Y = 1 #character's y position
S  = 0
#there is no "vy" or jumping power because there is no jumping in the game
    #X  Y 
guy = [X,Y,480,400]

move=0
frame=0
#initializing font
font.init()
comicSansFont = font.SysFont("Consolas",40)#loading comic sans font

#initializing sounds
mixer.init()
musicChannel = mixer.Channel(0)#making a mixer
introMusic = mixer.Sound("Sound/introMusic/intro.ogg")
#musicChannel.play(introMusic)

#making a clock
myClock = time.Clock()
myClock.tick(60)#making the program run 60 times per second

#opening text files
introText = open("text/intro/intro text.txt","r")#opening intro slides' text
slideTexts = introText.readlines()#getting a list of each line(slide) of dialogue

backPics=[]
unloadedPics=["Pictures/back/back1.png",'Pictures/back/back2.png']
for unload in unloadedPics:
    backPics.append(image.load(unload))
guyPic = image.load("Pictures/guy/guy.png")#29x31
heartPic = image.load("pictures/heart.png")
HX = 475
HY = 475
heart = [HX,HY,100,100]

maskPic=image.load('Pictures/mask/mask1.png')
#defining functions
def drawSlides(text,picture):#defining a function that draws intro slides
    screen.blit(picture,(175,100))#blitting the picture for the slide
    fx = 100#font x position
    fy = 550#font y position
    count = 0#a counter that is used to make sure that the audio doesnt get cut off
    for char in text:#for the character in the text
        count+=1#increase the count by 1
        if char == "~":#if the character is "~", this means that the program needs to start a new line. This is in the text files so that we can use .readlines() more easily, as we can fit everything that should be said in one text box in one line
            fx = 100
            fy+=50
        elif char=="\n":
            fx+=0
        else:
            inc = 0#increment so that letters appear 1 by 1, also reseting it so that the increment only increases for pauses
            count+=1#counter increases by 1
            if char == "." or char == ",":#if the character is punctuation
                inc = 400#increase the amount of time the program waits after displaying the letter
            char = comicSansFont.render(char,True,WHITE)#render the character
            screen.blit(char,(fx,fy))#blit the font at font x and font y
            display.flip()#show everything
            time.wait(65+inc)#wait so that letters show 1 by 1
            fx+=20#move the next character 13 pixels over
    time.wait(1500)#at the end of the slide, wait 1500 millaseconds
    screen.fill(BLACK)#fill the screen with black color so that the next slide doesnt overlap

def drawPictures(picture):#defining function that will blit the picture of the slides
    screen.blit(picture,(175,100))#blit the picture
    display.flip()
    time.wait(2500)#wait so that they user can see the picture
    screen.fill(BLACK)#fill the screen with black color so that the next slide doesnt overlap

def checkPixelX(back,x,y,w,col):
    '''returns the colour of the pixel at current (x,y)'''
    cond = True
    for i in range(w):
        if back.get_at((x+i,y)) == col:
            cond = False
    return cond
    #return (-1,-1,-1)

def checkPixelY(back,x,y,h,col):
    '''returns the colour of the pixel at current (x,y)'''
    cond = True
    for i in range(h):
       # print(screen.get_at((x,y+i)))
        if back.get_at((x,y+i))== col:
            
            cond = False
    return cond        
        
def addPics(name,start,end):
    '''this function will return a LIST OF PICTURES
    They must be in a folder named 'name' and all the pictures must start with 'name'
    start,end-the range of picture numbers
    '''
    myPics=[]
    for i in range(start,end+1):
        myPics.append(image.load("Pictures/%s/%s%03d.png"%(name,name,i)))
    return myPics

def moveGuy(guy):
    global move,frame
    newMove=-1
    keys = key.get_pressed()
    print(guy)
    if keys[K_LEFT] and guy[X]>-480:
        if checkPixelY(maskPic,guy[X]+480-10,guy[Y]+400,guyPic.get_height(),RED):
            if guy[X]<=-190:
                guy[2]-=10
            if guy[X]>=1230:
                guy[2]-=10
            guy[X]-=10
            newMove=3
    elif keys[K_RIGHT] and guy[X]<2267:
        if checkPixelY(maskPic,guy[X]+480+60,guy[Y]+400,guyPic.get_height(),RED):
            if guy[X]<=-200:
                guy[2]+=10
            if guy[X]>=1220:
                guy[2]+=10
            guy[X]+=10
            newMove=0
    elif keys[K_UP] and guy[Y]>-480:
        if checkPixelX(maskPic,guy[X]+480,guy[Y]-10+400,guyPic.get_width(),RED):
            if guy[Y]<=-50:
                guy[3]-=10
            guy[Y]-=10
            newMove=2
    elif keys[K_DOWN] and guy[Y]<800:
        if checkPixelX(maskPic,guy[X]+480,guy[Y]+400+82,guyPic.get_width(),RED):
            if guy[Y]<=-60:
                guy[3]+=10
            guy[Y]+=10
            newMove=1
    else:
        frame=0
    if move==newMove:
        frame=frame+0.2
        if frame>=len(pics[move]):
            frame=1
    elif newMove!=-1:
        move=newMove
        frame=1

def drawScene(screen,picsList,backPics,guy):
    global S #what scene the character is in
    #if gateRect.collideRect(guy):#if they are moving to the next level
        #S+=1#mvoe to the next scene
    if guy[X]<=-190 and guy[Y]<=-50:#the rest of the lines are chekcing where the character is, because if they are too far into one part of the scene we want to move the CHARACTER and NOT the background picture
        screen.blit(backPics[S],(190,50))
    elif guy[X]<=-190:
        screen.blit(backPics[S],(190,-guy[Y]))
    elif guy[X]>=1220:
        screen.blit(backPics[S],(-1220,-guy[Y]))
    elif guy[Y]<=-50:
        screen.blit(backPics[S],(-guy[X],50))
    else:
        screen.blit(backPics[S],(-guy[X],-guy[Y]))
    screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
    display.flip()
    
##
##for i in range(8):
##    if i!=7:
##        drawSlides(slideTexts[i],image.load("Pictures/introPics/intro"+str(i+1)+".jpg"))#draw the slides 1 through 6, adding 1 because the for loop starts at 0 and ends at 5
##   
##for i in range(3):
##    drawPictures(image.load("Pictures/introPics/intro"+str(i+8)+".jpg"))#drawing the pictures 7 through 9,adding 7 because the pictures are labeled in the folder in order of the slides
##
##intro11 = image.load("Pictures/introPics/intro11.jpg")#loading final image, this does not get a function because it is simpler to just do it without one, as it is only one picture
##screen.blit(intro11,(175,-550))#blit the picture at 100,-550, as the picture is 1368 tall, and we only want to 500 pixels at this point so it matches the other pictures
##draw.rect(screen,BLACK,(175,0,800,100))
##display.flip()
##time.wait(2000)#wait 2000 millaseconds
##
##for i in range(550):
##    screen.blit(intro11,(175,-550+i))#draw the picture 1 pixel lower
##    draw.rect(screen,BLACK,(175,0,800,100))
##    draw.rect(screen,BLACK,(175,550,800,400))#draw a rect below the picture so that when it starts coming down you only see 297 vertical pixels of picture
##    display.flip()#show all this
##time.wait(5000)
##musicChannel.pause()
pics=[addPics('guy',1,3),
    addPics("guy",4,6),addPics('guy',7,9),addPics('guy',10,12)]            

running = True         
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
            
    moveGuy(guy)
##    mb=mouse.get_pressed()
##    mx,my=mouse.get_pos()
##    if mb[0]==1:
##        print(screen.get_at((mx,my)))
        
    drawScene(screen,pics,backPics,guy)
    myClock.tick(60)

quit()

