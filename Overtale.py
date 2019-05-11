
#importing what the program needs
from pygame import *
from random import *
from math import *

#making a screen
size = width,height = 1000,750
screen = display.set_mode(size)

#making basic colors
RED = (255,0,0)   
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

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

#loading pictures
#backPic = image.load() #4000x500
#backPic2= image.load()
backPics=[]
unloadedPics=["Pictures/backPics/back1.png",'Pictures/backPics/back2.png']
for unload in unloadedPics:
    backPics.append(image.load(unload))
guyPic = image.load("Pictures/guy/guy.png")#29x31


#defining functions
def drawSlides(text,picture):#defining a function that draws intro slides
    screen.blit(picture,(100,100))#blitting the picture for the slide
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
    screen.blit(picture,(100,100))#blit the picture
    display.flip()
    time.wait(2500)#wait so that they user can see the picture
    screen.fill(BLACK)#fill the screen with black color so that the next slide doesnt overlap

def checkPixelX(x,y,w,col):
    '''returns the colour of the pixel at current (x,y)'''
    cond = True
    for i in range(w):
        if screen.get_at((x+i,y)) == col:
            cond = False
    return cond
    #return (-1,-1,-1)

def checkPixelY(x,y,h,col):
    '''returns the colour of the pixel at current (x,y)'''
    cond = True
    for i in range(h):
       # print(screen.get_at((x,y+i)))
        if screen.get_at((x,y+i))== col:
            
            cond = False
    return cond
def floweyScene(guy,picsList):
    frame=0
    guy[X]=0
    guy[Y]=0
    guy[2]=480
    guy[3]=500
    print(guy[3])
    while guy[3]>480:
       # frame+=0.2
        guy[3]-=1
    screen.blit(picsList[2][int(frame)],(guy[2],guy[3]))
    
        
        
def addPics(name,start,end):
    '''this function will return a LIST OF PICTURES
    They must be in a folder named 'name' and all the pictures must start with 'name'
    start,end-the range of picture numbers
    '''
    myPics=[]
    for i in range(start,end+1):
        myPics.append(image.load("Pictures/%s/%s%03d.png"%(name,name,i)))
    return myPics

def drawScene(screen,picsList,backPics,guy):
    #print(S)
    global S
    if guy[X]<=-190 and guy[Y]<=-50:
        screen.blit(backPics[S],(190,50))
    elif 1510<guy[X]<1620 and guy[Y]<=41:
        S+=1
        floweyScene(guy,picsList)
        #screen.blit(backPics[S],(190,50))
        #screen.blit(backPics[S],(0,0))
        #draw.rect(screen,BLACK,(0,0,width,height))
    elif guy[X]<=-190:
        screen.blit(backPics[S],(190,-guy[Y]))
    

    elif guy[X]>=1220:
        screen.blit(backPics[S],(-1220,-guy[Y]))
    elif guy[Y]<=-50:
        screen.blit(backPics[S],(-guy[X],50))
    
    else:
        screen.blit(backPics[S],(-guy[X],-guy[Y]))
    #print(guy[X],guy[Y],guy[2],guy[3])
   # print(guy)
    screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
    display.flip()
    
def moveGuy(guy):
    global move,frame
    newMove=-1
    keys = key.get_pressed()
    if keys[K_LEFT] and guy[X]>-480:
        if checkPixelY(guy[2]-1,guy[3],guyPic.get_height(),BLACK):
            if guy[X]<=-190:
                guy[2]-=10
            if guy[X]>=1220:
                guy[2]-=10

            guy[X]-=10
            newMove=3
            #else:
            
                #guy[X]-=10
                #newMove=3
            
    elif keys[K_RIGHT] and guy[X]<2267:
        if checkPixelY(guy[2]+52,guy[3],guyPic.get_height(),BLACK):
            
            if guy[X]<=-190:
                guy[2]+=10
            if guy[X]>=1220:
                guy[2]+=10
            guy[X]+=10
            newMove=0
            
            
            
    elif keys[K_UP] and guy[Y]>-480:
        if checkPixelX(guy[2],guy[3]-1,guyPic.get_width(),BLACK):
            if guy[Y]<=-50:
                guy[3]-=10
            #if guy[X]<=-190:
             #    guy[Y]-=10   
            
            guy[Y]-=10
            newMove=2
            
    elif keys[K_DOWN] and guy[Y]<800:
        if checkPixelX(guy[2],guy[3]+81,guyPic.get_width(),BLACK):
            
            if guy[Y]<=-50:
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

##for i in range(8):
##    drawSlides(slideTexts[i],image.load("Pictures/introPics/intro"+str(i+1)+".jpg"))#draw the slides 1 through 6, adding 1 because the for loop starts at 0 and ends at 5
##   
##for i in range(3):
##    drawPictures(image.load("Pictures/introPics/intro"+str(i+8)+".jpg"))#drawing the pictures 7 through 9,adding 7 because the pictures are labeled in the folder in order of the slides
##
##intro11 = image.load("Pictures/introPics/intro11.jpg")#loading final image, this does not get a function because it is simpler to just do it without one, as it is only one picture
##screen.blit(intro11,(100,-828))#blit the picture at 100,-928, as the picture is 1368 tall, and we only want to 500 pixels at this point so it matches the other pictures
##draw.rect(screen,BLACK,(100,0,800,100))
##display.flip()
##time.wait(2000)#wait 2000 millaseconds
##
##for i in range(828):
##    screen.blit(intro11,(100,-828+i))#draw the picture 1 pixel lower
##    draw.rect(screen,BLACK,(100,0,800,100))
##    draw.rect(screen,BLACK,(100,540,800,400))#draw a rect below the picture so that when it starts coming down you only see 297 vertical pixels of picture
##    display.flip()#show all this
##time.wait(10000)
##musicChannel.pause()

pics=[addPics('guy',1,3),
    addPics("guy",4,6),addPics('guy',7,9),addPics('guy',10,12)]            
running = True         
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
            
    moveGuy(guy)
    drawScene(screen,pics,backPics,guy)
    myClock.tick(60)

quit()

