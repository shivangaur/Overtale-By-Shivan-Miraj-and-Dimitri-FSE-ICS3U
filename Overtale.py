#importing modules 
from pygame import *
from random import *
from math import *
from pprint import *
import os
from shiv import *
os.environ['SDL_VIDEO_CENTERED'] = '1'#centering the screen
#making a screen
size = width,height = 1000,750#size
screen = display.set_mode(size)

display.set_caption("Overtale")  # Setting the window title
display.set_icon(transform.scale(image.load("Pictures/heart.png"),(32,32)))  # Setting the screen icon
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
S  = 5#the index of the position in the 'guy' variable that determines which scene
#you're currently on
MAXX=7# max X value
MINX=11#min X value
MINY=13#min Y value
MAXY=9# max Y value
MOVEL=15#The point at which the background stops moving and the player starts
#moving when you go left
MOVER=17# same thing as above, but for right
MOVEUP=19# same thing as above but for up

'''
The 'guy' player list of all the important points and coordiantes for the
current scene. These points get updated every time you move to the next scene
'''
guy = [X,Y,480,400,S,2,MAXX,2267,MAXY,800,MINX,-480,MINY,-400,MOVEL,-190,MOVER,1220,MOVEUP,-50]

toriel=[470,155,480,500,480,500,370,400]#toriel list. Only has the x and y position for toriel on the screen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  #GX GY SX  SY  MX   MX  MY MOVEL MOVER MAXX MAXY
scenes=[[0,0,480,400,1490,1630,41,-190,1220,2267,800,-50],[0,600,480,400,-50,40,20,0,0,460,930,-50],[0,600,480,400,-50,40,20,0,0,460,930,-50],[10,650,480,650,-40,40,-310,0,-10,460,650,-1000],[0,0,450,570,-80,30,-310,1,1000,460,1000,1],[0,0,400,650,1780,1800,1000,1,1270,2400,2300,1],[0,0,0,450,400,540,-220,1,0,2400,2300,1],[0,0,400,650,3260,3360,1000,1,2720,2400,2300,1],[0,20,20,450,3480,3500,1000,1,2560,2400,2300,60],[0,0,20,300,410,520,-40,1,-1,2400,800,0],[0,0,500,630,400,700,1000,1,1000,2400,800,1],[0,0,500,230,400,500,1000,1,-1,2400,800,0],[0,0,20,320,860,900,1000,1,-1,2400,800,0],[0,0,20,320,1350,1450,1000,1,500,2400,800,0],[0,0,20,320,1650,1850,1000,1,760,2400,800,0],[0,0,20,340,1650,1850,1000,1,760,2400,800,0],[0,0,20,370,840,920,1000,1,0,2400,800,0],[0,0,20,370,840,920,1000,1,0,2400,800,0],[0,0,20,370,840,920,1000,1,0,2400,800,0],[0,0,880,400,-320,-160,-110,1,0,2400,800,0],[0,0,250,690,1460,1570,-130,1,790,2400,800,0],[0,0,20,230,1520,1670,1000,1,660,2400,800,0],[0,0,20,330,590,750,-1000,1,50,2400,800,0]]
''' ^^^^ probably one of the most important features in the code.
This 'scenes' list, is a 2d list of lists for each individual scene. Every
element in the list consists of the guyX,guyX, the screen Pos, and many other
important coordinates for the current scene.
'''
#print('GX GY SX  SY  MX   MX  MY MOVEL MOVER MAXX MAXY')
pprint(scenes)
move=0#variable for the current direction that the player is at e.g left,right,up,down---> 0,1,2,3
frame=0#the frame for each move
#initializing font
font.init()
consolas = font.SysFont("Consolas",40)#loading comic sans font
consolasPlay=font.SysFont('Consolas',12)

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



guyPic = image.load("Pictures/guy/guy.png")#29x31
openPic=image.load('Pictures/introPics/opening.jpg')
heartPic = image.load("Pictures/heart.png")
##toriel Script Images
torielScript2=image.load('text/characters/toriel/torielScript2.png')
torielScript3=image.load('text/characters/toriel/torielScript3.png')
#toriel=image.load("Pictures/toriel/toriel.png")
HX = 475
HY = 475
heart = [HX,HY,100,100]
floweyPic=image.load('Pictures/flowey/flowey001.png')
#maskPic=image.load('Pictures/mask/mask1.png')

#flowey
floweyText=open('text/characters/flowey/flowey.txt')

script=floweyText.readlines()

#defining functions
def addPics(name,start,end):
    '''
    This function takes a string name, a start position and an end position,
    and returns a list of pictures
    '''
    myPics=[] #empty list
    for i in range(start,end+1):
        myPics.append(image.load("Pictures/%s/%s%03d.png"%(name,name,i)))
        #loading and adding the image in the pictures folder, from a folder with
        #the name of the string
    return myPics#returns list of pictures

def checkCombat():
    return False
#backPics=[]
backPics=addPics('back',1,23)
maskPics=addPics('mask',1,23)
#maskPics=[]
#unloadedPics=["Pictures/back/back1.png",'Pictures/back/back2.png']
#unloadedMaskPics=['Pictures/mask/mask1.png','Pictures/mask/mask2.png']

#for unload in unloadedPics:
#   backPics.append(image.load(unload))
#for unload in unloadedMaskPics:
 #   maskPics.append(image.load(unload))

def drawFont(ofx,ofy,fx,fy,count,moveText,k,j,i,running,screenVar):
    #draw.rect(screen,WHITE,(0,0,width,height))
    
    global script
    
    #time.wait(2000)
    if count % 8 == 0:
        if k < len(script):
            if j < len(script[k]):
                if i < len(script[k][j]):
                    if script[k][j][i] != "~":
                        if screenVar:
                            screen.blit(screenshot,(100,100))
                        character = consolas.render(script[k][j][i],True,WHITE)
                        screen.blit(character,(fx,fy))
   # if count % 120 == 0:
    #    musicChannel.play(sound)
    
    display.flip()
    #time.wait(2000)
    return fx,fy,count,moveText,k,j,i,running,screenVar

def update(fx,fy,count,moveText,k,j,i,running):
    global script
    if script[k][j][i] == "~":
        fx = ofx
        fy += 20
        moveText = False
    else:
        screenVar = True
    if moveText:
        fx += 10
    if count % 12 == 0:
        if not i+1 == len(script[k][j]):
            i+=1
            moveText = True
            screenVar = True
        else:
            i = 0
            if not j+1 == len(script[k]):
                j+=1
            else:
                j = 0
                if not k+1 == len(script):
                    k+=1
                    fx = ofx
                    fy = ofy
                    moveText = False
                    screenVar = False
                else:
                    running = False
    count += 1
    display.flip()
    screenshot = screen.copy().subsurface(ofx,ofy,800,100)
    return fx,fy,count,moveText,k,j,i,running

def make3d(text):
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

scriptList=[make3d(open("text/characters/toriel/torielScript001.txt","r")),make3d(open("text/characters/toriel/torielScript002.txt","r")),make3d(open("text/characters/toriel/torielScript003.txt","r")),make3d(open("text/characters/toriel/torielScript004.txt","r")),make3d(open("text/characters/toriel/torielScript005.txt","r")),make3d(open("text/characters/toriel/torielScript006.txt","r")),make3d(open("text/characters/toriel/torielScript007.txt","r")),make3d(open("text/characters/toriel/torielScript008.txt","r")),make3d(open("text/characters/toriel/torielScript009.txt","r")),make3d(open("text/characters/toriel/torielScript010.txt","r"))]

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
            char = consolas.render(char,True,WHITE)#render the character
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
        

def transScene():
    ''' creates a transition scene that can be used when navigating between
screens
    '''
    #global myclock
    for i in range(10):
        for k in range(75):
            draw.circle(screen,RED,(i*150,k*10),100)#drawing a circle
            display.update()#updating screen immediately 
            #myClock.tick(60)
def textBox(x,y,width,length,character):
    ''' General text box function used to create in-game text boxes, with the
icon of whatever character string is entered in. E.g 'flowey' would use the flowey
icon for the text box
    '''
    draw.rect(screen,BLACK,(x,y,width,length))#Text box
    draw.rect(screen,WHITE,(x,y,width,length),4)#border
    person=image.load('Pictures/textbox/'+character+'box'+'.jpg')#icon
    screen.blit(person,(x+15,y+20))#blitting icon

writing=True
def drawFont(text,charSound,x,y):
    sound=mixer.music.load('Sound/characters/'+charSound+'.ogg')
    count=0
    fx=x
    fy=y
    for char in text:
        inc=0
        #print(char)
        if char=='\n':
            fx+=0
        elif char=='~':
            fx=x
            fy+=y
        else:
            #if count%6==0:
                #mixer.music.play(1)
            if char==',' or char=='.' or char=='!':
                inc=400
                
            char=consolas.render(char,True,WHITE)
            screen.blit(char,(fx,fy))
            display.flip()
            fx+=22
            screenShot=screen.copy().subsurface(0,0,1000,150)
            time.wait(65+inc)
        count+=1
    time.wait(1000)
    draw.rect(screen,BLACK,(x,y-15,int(width-230),130))
    
    #screen.fill(BLACK)
#writing=True
#for text in script:
 #   drawFont(text,'flowey')
#writing=False
writing=True
def fade(width, height,col):
    '''Fade transition to make going to the next scene smoother'''
    fade = Surface((width, height))# creating new surface
    fade.fill(col)#filling new surface with colour 
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))#blitting the new surface at (0,0)
        display.update()#updating screen
        time.delay(5)#delaying screen
        
def transCool(width,height,col):
    for i in range(0,width+50,50):
        for j in range(0,height+50,50):
            #draw.rect(screen,BLACK,(0,0,i,j))
            draw.circle(screen,col,(i,j),29)
            #draw.circle(screen,BLACK,(i-50,j),25)
            time.wait(1)
            display.flip()
    for i in range(0,height+50,50):
        for j in range(0,width+50,50):
            #draw.rect(screen,BLACK,(0,0,i,j))
            draw.circle(screen,WHITE,(j,i),35)
            #draw.circle(screen,BLACK,(i-50,j),25)
            time.wait(1)
            display.flip()
    fade(width,height,BLACK)
    text=consolas.render('SUCCESS!!!',True,(255,255,0))
    screen.blit(text,(400,300))
    display.flip()
    time.wait(1000)
casex=casey=0
difx=dify=0
def moveGuy(guy):
    ''' Main function for player movement'''
    #globalizing variables needed
    global move,frame,casex,casey,difx,dify,writing
    
    difx=guy[X]-guy[2]
    dify=guy[Y]-guy[3]
    newMove=-1#
    keys = key.get_pressed() #variable for all key codes
    if writing: #variable 
        if (keys[K_a] or keys[K_LEFT]): # if the left or 'a' keys are clicked
            if checkPixelY(maskPics[guy[S]],guy[X]+guy[2]+casex-10,guy[Y]+guy[3]+casey,guyPic.get_height(),RED):
            #This function checks the mask of the current background, to see if
            #the character is entering a prohibited area.
                if guy[X]<=guy[MOVEL]:# if guyX is less than the Move Left
                    #coordinate, then start moving the character instead of
                    #the background
                    guy[2]-=10#subtracting the player's screen position (X pos)
                    casex+=10#the difference when you stop moving the backgroun
                    #and start moving the player
                if guy[X]>=guy[MOVER]+10:#if guyX is greater than the point at which
                    #you stop moving the background then move the player left on the screen
                    guy[2]-=10
                    casex+=10
                guy[X]-=10 #at the end of everything update guyX
                newMove=3
        elif (keys[K_d] or keys[K_RIGHT]):# if the right or 'd' keys are clicked
            if checkPixelY(maskPics[guy[S]],guy[X]+guy[2]+casex+60,guy[Y]+guy[3]+casey,guyPic.get_height(),RED):
                if guy[X]<=guy[MOVEL]-10:
                    guy[2]+=10
                    casex-=10
                if guy[X]>=guy[MOVER]:
                    guy[2]+=10
                    casex-=10
                guy[X]+=10
                newMove=0
        elif (keys[K_w] or keys[K_UP]):
            # and guy[Y]>-480
            if checkPixelX(maskPics[guy[S]],guy[X]+guy[2]+casex,guy[Y]-10+guy[3]+casey,guyPic.get_width(),RED):
                if guy[Y]<=guy[MOVEUP]:
                    guy[3]-=10
                    casey+=10
                guy[Y]-=10
                newMove=2
        elif (keys[K_s] or keys[K_DOWN]):
            # and guy[Y]<guy[MAXY]
            if checkPixelX(maskPics[guy[S]],guy[X]+guy[2]+casex,guy[Y]+guy[3]+casey+82,guyPic.get_width(),RED):
                if guy[Y]<=guy[MOVEUP]-10:
                    guy[3]+=10
                    casey-=10
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
##def floweyScene(guy,script):
##    guy[X]=0
##    guy[Y]=600
##    guy[2]=480
##    guy[3]=400
##    guy[MOVEL]=0
##    guy[MOVER]=0
##    guy[MAXX]=460
##    guy[MAXY]=930
##    guy[S]+=1
##    return True
    
    
   # screen.blit(backPics[guy[S]]
    #screen.blit(floweyPic,(guy[X]+480,guy[Y]-550+400))
def drawPellets(heartRect,pellets):
    
    for pell in pellets:
        draw.ellipse(screen,WHITE,pell)

#def movePellets(pellets):
    
    
def floweyEncounter(picsList,guy,mono2):
    '''drawing everything for the flowey scene including the text box, text, and
the heart phase transition scene
    '''
            
##    if mono2:
##        writing=False
##        textBox(40,20,width-80,150,'flowey')
##        for text in script:
##            drawFont(text,'flowey',180,50)
##            writing=False
##            x=script.index(text)
##                    
##            if x==len(script)-1:
##                mono2=False
    #for i in range(3):
    heartPhase(guy,picsList)
    guy[S]+=1
##    guy[X]=0
##    guy[Y]=600
##    guy[2]=480
##    guy[3]=400
bet=True
def drawMenu():
    '''Function for drawing a menu whenever a character interacts with an object
    '''
    global bet
    running=True
    while running:
        for evnt in event.get():                
            if evnt.type == QUIT:
                running = False
        textBox(200,100,200,150,'black')#text box
        textBox(200,300,200,150,'black')# text box
        keys=key.get_pressed()

        if keys[K_RETURN]:#exiting the menu
            bet=False
            return
            
        display.flip()
cond=False
drawTor=True
torielMovements=['up','up','up','up','up']
#list of toriel movements 

count=0
position=0# position in the toriel movemenets list
moveTor=frameTor=0 #move and frame variables for the Toriel picsList
def moveToriel(x,y):
        global moveTor,frameTor,count,position,writing
        newMove=-1
        keys=key.get_pressed()# keys codes list
        if torielMovements[position]=='left':

                toriel[x]-=10

                newMove=3
        elif torielMovements[position]=='right':

                toriel[x]+=10

                newMove=0
        elif torielMovements[position]=='up':

                toriel[y]-=10

                newMove=2
        elif torielMovements[position]=='down':

                toriel[y]+=10

                newMove=1
        else:
            frameTor=0
        if moveTor==newMove:
            frameTor=frameTor+0.2
            if frameTor>=len(torielPics[move]):
                frameTor=1
        elif newMove!=-1:
            moveTor=newMove
            frameTor=1
        count+=1
        writing=False
        if count%10==0:
            if position<len(torielMovements)-1:
                position+=1
        if position==len(torielMovements)-1:
            writing=True
        if toriel[1]<-50:
            torielMovements[-1]='None'
        
        
    
    
    
def drawToriel(picsList):
    '''This function draws the toriel character whenever she appears in scenes,
because he only appears in certain scenes.
    '''
    print(toriel[4],toriel[5])
    global drawTor,moveTor,frameTor,torielMovements,toriel,writing#globalizing variables
    keys=key.get_pressed()
    if guy[S]==2 and drawTor:# third scene
        #screen.blit(torielPics[1][0],(470,155))#blitting the front toriel picture
        #on the flower bed
        torielScene()#calling the toriel Scene
        #time.wait(2000)
        moveToriel(0,1)
        screen.blit(torielPics[moveTor][int(frameTor)],(toriel[0],toriel[1]))
    if guy[S]==3:#4th scene

         torielMovements=['up','up','up','up','up','up','right','right','up','up']
         #screen.blit(torielPics[1][0],(470,155))#blitting the front toriel picture
         #time.wait(2000)
         moveToriel(2,3)#moving toriel
         screen.blit(torielPics[moveTor][int(frameTor)],(toriel[2],toriel[3]))
         #blitting the propper toriel pic for whichever direction she's traveling
    if guy[S]==4 and drawTor:
        torielMovements=['right','right','up','up','left','left','left','down','None','None']
        moveToriel(4,5)#moving toriel
        screen.blit(torielPics[moveTor][int(frameTor)],(toriel[4],toriel[5]))
        if writing :
            textBox(140,150,width-300,170,'toriel')#making textbox
            screen.blit(torielScript2,(300,165))
            screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
            display.flip()
            time.wait(10000)
            fade(width,height,BLACK)
            drawTor=False
    if guy[S]==5 and not drawTor:
        textBox(140,150,width-300,170,'toriel')#making textbox
        screen.blit(torielScript3,(300,165))
        display.flip()
        time.wait(10000)
        fade(width,height,(128,0,128))
        drawTor=True
        
        
            
        
fontDr=True
def torielScene():
    '''This function draws the font for toriel and blits the text while the
character can't move'''
    global writing
    #writing=False
    #fontDr=True
    if not writing:
        textBox(150,550,width-300,150,'toriel')#making textbox
        text=consolas.render('This Way.',True,WHITE)
        screen.blit(text,(300,600))
    #for text in scriptsList:
def levers(cond):
    keys=key.get_pressed()
    if keys[K_RETURN]:
        if guy[Y]<-400:
            if 720<=guy[X]<=790:
                cond=True
            elif 1320<=guy[X]<=1420:
                cond=True
            elif 1480<=guy[X]<=1540:
                cond=True
    if cond:
        transCool(width,height,(randint(0,255),randint(0,255),randint(0,255)))
def room11(guy):
    '''This function is for the 11th scene, so that when you reach the center,
the entrance becomes the exit'''
    global cond,bet
    if -40<=guy[X]<=10 and guy[Y]<-260:#if the player reaches the center
        cond=True#condition becomes true
    if cond and bet:
        textBox(120,600,width-80,150,'black')#draws textbox
        drawMenu()#draws menu
    if not bet and guy[Y]>-20:#only works after the menu has been drawn (bet must be False)
#changing the coordinates at which you move to the next scene to be at the entrance
        scenes[guy[S]][4]=-70
        scenes[guy[S]][5]=40
        scenes[guy[S]][6]=410

def room19(guy):
    '''This function is similar to the room11 function,but it's for the 19th
scene'''
    global cond,bet#globalizing
    if guy[X]>430 and guy[Y]>0:
        cond=False# since cond and bet were already made variables, I used those
        #except I used opposite conditional statments
    if not cond and not bet:
        textBox(120,600,width-80,150,'black')#text box
        drawMenu()#drawing menu
        cond=True
        bet=True
    if bet:
#changing the coordinates at which you move to the next scene to be at the entrance
        scenes[guy[S]][4]=-20
        scenes[guy[S]][5]=10
        scenes[guy[S]][6]=1000
def room22(guy):
    '''Function for room 22 that simply changed the Y coordiate of the point at which
to move to the next scene, to be 1000.'''
    # I need to do this because unlike the rest of the scenes, the exit of this
    #scene is at the bottom of the screen, so I can't use the same technique I
    #did for the other scenes
    if guy[Y]>600:#if the player reaches above 600 then they're about
        #to reach the entrance
        scenes[guy[S]][6]=1000# make it from 600 to 1000 so the player changes scenes
        
    
        
        
        
        
mono2=True
def heartPhase(guy,picsList):
    '''This function makes a transition into the flowey fight that makes
it look like the player's heart is phasing, similar to the actual game'''
    for i in range(5):#5 phases
        screen.fill(BLACK)#filling screeen with black
        time.wait(200)#pausing screen
        display.flip()#showing the screen
        screen.blit(picsList[2][0],(guy[2]-2*i,guy[3]-2*i))#blitting the character
        #picture at where it last was, moving it slightly up diagonally
        time.wait(200)#delaying screen
        display.flip()#updating screen
        screen.fill(BLACK)#filling screen with black
        time.wait(200)#delaying again
        display.flip()#updating
        screen.blit(heartPic,(guy[2]+5-2*i,guy[3]+5-2*i))#blitting the heart pic
        
        display.flip()#updating screen again
back=True     
def drawScene(screen,picsList,backPics,guy,combat):
    '''This is the main drawScene function where the background, and player are blitted.
    There are many different cases for how the background can be blitted'''
    global mono2,casex,casey,cond,bet,script,position,back
    print(guy[X],guy[Y],guy[2],guy[3])
    
    mono=False
    
    #If statement to update all the 'guy' list elements once the player enters
    #a new scene
    #If the players X value is between the given values, and it's Y value is below
    #the given value, then switch scenes
    if back:
        if scenes[guy[S]][4]<guy[X]<scenes[guy[S]][5] and guy[Y]<scenes[guy[S]][6]:
            fade(1000,750,BLACK)#fade transition
            guy[S]+=1#move to the next scene
            guy[X]=scenes[guy[S]][0]#update guyX
            guy[Y]=scenes[guy[S]][1]#update guyY
            #update player screen pos
            guy[2]=scenes[guy[S]][2]
            guy[3]=scenes[guy[S]][3]
            #update points to stop moving background and start moving the player
            guy[MOVEL]=scenes[guy[S]][7]
            guy[MOVER]=scenes[guy[S]][8]
            guy[MAXX]=scenes[guy[S]][9]
            guy[MAXY]=scenes[guy[S]][10]
            guy[MOVEUP]=scenes[guy[S]][11]
            casex=casey=0#resetting the difference for when you stop moving the background
            #and start moving the player
            position=0
        elif guy[X]<=guy[MOVEL]-10 and guy[Y]<=guy[MOVEUP]:
            #if the player is before the X and Y positions, then stop moving the background completely
            screen.blit(backPics[guy[S]],(-guy[MOVEL],-guy[MOVEUP]))

        elif guy[X]<=guy[MOVEL]-10:#if you move to the far left, then stop moving the background horizontally
            # and only move the background vertically.
            screen.blit(backPics[guy[S]],(-(guy[MOVEL]-10),-guy[Y]))

        elif guy[X]>=guy[MOVER] and guy[Y]<=guy[MOVEUP]:#background doesn't move
            screen.blit(backPics[guy[S]],(-guy[MOVER],-guy[MOVEUP]))

        elif guy[X]>=guy[MOVER]:#background moves vertically not horizontally when the player is greater
            #than a certain X pos (far right)
            screen.blit(backPics[guy[S]],(-guy[MOVER],-guy[Y]))
        
            
        elif guy[Y]<=guy[MOVEUP]:#background moves horizontally but not vertically when player is
            #above a certain position
            screen.blit(backPics[guy[S]],(-guy[X],-guy[MOVEUP]))
          
        else:#only background moves
            screen.blit(backPics[guy[S]],(-guy[X],-guy[Y]))
       
    drawToriel(picsList)#calling the draw toriel function, which will draw toriel if the scene has him
    screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))# blitting the character at the correct
    #move and frame
    checkEncounter(guy,mono2,picsList)#calling the check encouter function.
   
    display.flip()#updating the whole screen
def checkEncounter(guy,mono2,picsList):
    '''This function is pretty important because it acts like a sort of database to organize all the encounters.
it is called in the drawScene function and calls the other specfic encoutner functions''' 
    if guy[S]==1:#first scene
        if guy[Y]<550:#moving close to flowey
            floweyEncounter(picsList,guy,mono2)#flowey encounter
    if guy[S]==5:
        levers(False)
    if guy[S]==10:#11th scene
        room11(guy)
    if guy[S]==18:#19th scene
        room19(guy)
    if guy[S]==22:#23rd scene
        room22(guy)
def drawIntro():
   '''This function draws the title screen of the game'''
   myClock=time.Clock()
   running=True
   while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    screen.blit(openPic,(0,0))#intro picture
    keys=key.get_pressed()
    if keys[K_RETURN]:#If the user presses enter
        transCool(width,height,BLUE)#cool transition
        break#exit function

    
    myClock.tick(60)
    display.flip()
def chooseName():
    '''This function allows the user to enter their name into the game'''
    screen.fill(BLACK)#filling the screen with black
    lets=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ?!')#list of capital alphabets
    lows=list('abcdefghijklmnopqrstuvwxyz?!')#lists of lowercase alphabets
    lowers=[]#empty list that'll become a 2d list of alphabets
    letters=[]#empty list that'll become a 2d list of alphabets
    count=0#counter
    for i in range(1,5):#loop to add the alphabets into a 7x4 grid.
        letters.append(lets[7*(i-1):7*i])
        lowers.append(lows[7*(i-1):7*i])
    pprint(letters)
    pprint(lowers)
    coords=[]#list of coordinates
    myClock=time.Clock()#clock
    running=True
    posr=0#
    posc=0
    lowr=lowc=0
    name=''
    case=0
    store=letters[:]#copy of uppercase letter list
    while running:
        for evnt in event.get():                
            if evnt.type == QUIT:
                running = False
       
        keys=key.get_pressed()
        for i in range(1,5):#rows
            for j in range(1,8):#columns
                
                coords.append((100*((j%8)+1),50*i+100))#adding the coordinates of where the letter rects
                #are gonna be to the coords list
        
        for coor in coords:# for each coordinate
            x=coords.index(coor)#find the index of it
            let=consolas.render(lets[x],True,WHITE)#the letter will be the original lets list at the
            #index of coords
            screen.blit(let,(coor[0]+7,coor[1]))#blitting the letter
            draw.rect(screen,WHITE,(coor[0],coor[1],40,40),2)#drawing a white rect for the letter
            let=consolas.render(lets[x].lower(),True,WHITE)#redefining let as the lowercase version
            screen.blit(let,(coor[0]+7,coor[1]+302))#blitting the lowercase version
            draw.rect(screen,WHITE,(coor[0],coor[1]+300,40,40),2)#rect for lowercase version
        text=consolas.render("Name the fallen human. Click Tab when finished.",True,WHITE)#text at the top of the screen
        screen.blit(text,(250,80))#blitting text
        if not keys[K_CAPSLOCK]:#if capslock is off 
            letters=lowers#replace letters with lowercase version
            case=302#blit the rects 302 pixels down
        else:
            letters=store#letters=capital copy
            case=0#adding nothing
        
        if keys[K_TAB]:#tab ends the  
            fade(width,height,WHITE)#fade Transition 
        
            break#exit
        #navigating through the 2d list when the user uses the arrow keys
        if keys[K_UP]:
            if posr>0:
                posr-=1
        if keys[K_DOWN]:
            if posr<3:
                posr+=1
        if keys[K_LEFT]:
            if posc>0:
                posc-=1
        if keys[K_RIGHT]:
            if posc<6:
                posc+=1
        high=consolas.render(letters[posr][posc],True,(255,255,0))#highlighted letter
        screen.blit(high,(coords[posc][0]+7,coords[posr*7][1]+case))#blitting highlighted letter
        if keys[K_RETURN]:#if enter
            if len(name)<11: #max 11 characters
                name+=letters[posr][posc]#adding letter to name
        if keys[K_BACKSPACE]:#backspace
            name=name[:-1]#removing letter
            draw.rect(screen,BLACK,(0,700,width,50))#covering up old name
        
        nameText=consolas.render(name,True,WHITE)#name
        screen.blit(nameText,(370,700))#blitting name
        

        myClock.tick(60)
        
        display.flip()#displaying

screen.fill(BLACK)#filling BLACK


##for i in range(8):
##        if i!=7:
##            drawSlides(slideTexts[i],image.load("Pictures/introPics/intro"+str(i+1)+".jpg"))#draw the slides 1 through 6, adding 1 because the for loop starts at 0 and ends at 5
##           
##for i in range(3):
##        drawPictures(image.load("Pictures/introPics/intro"+str(i+8)+".jpg"))#drawing the pictures 7 through 9,adding 7 because the pictures are labeled in the folder in order of the slides
##
##intro11 = image.load("Pictures/introPics/intro11.jpg")#loading final image, this does not get a function because it is simpler to just do it without one, as it is only one picture
##screen.blit(intro11,(175,-550))#blit the picture at 100,-550, as the picture is 1368 tall, and we only want to 500 pixels at this point so it matches the other pictures
##draw.rect(screen,BLACK,(175,0,800,100))
##display.flip()
##time.wait(2000)#wait 2000 millaseconds
##
##for i in range(550):
##        screen.blit(intro11,(175,-550+i))#draw the picture 1 pixel lower
##        draw.rect(screen,BLACK,(175,0,800,100))
##        draw.rect(screen,BLACK,(175,550,800,400))#draw a rect below the picture so that when it starts coming down you only see 297 vertical pixels of picture
##        display.flip()#show all this
##time.wait(5000)
##musicChannel.pause()

#drawIntro()
#chooseName()


pics=[addPics('guy',1,3),#2d list of guy pictures
    addPics("guy",4,6),addPics('guy',7,9),addPics('guy',10,12)]            

torielPics=[addPics('toriel',1,4),addPics('toriel',5,8),#2d list of toriel pictures
            addPics('toriel',9,12),addPics('toriel',13,16)]

combat=False
running=True
#while running loop
##ofx,ofy=150,550
##fx,fy=ofx,ofy
##fontCount=0
##moveText=False
##k=j=i=0
##screenVar=False
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    
    #print(writing,fontDr)       
    moveGuy(guy)
    if checkCombat:
        combat=True
    drawScene(screen,pics,backPics,guy,combat)
    #if not writing and fontDr:
        #print(111)
  #      drawFont(ofx,ofy,fx,fy,fontCount,moveText,k,j,i,running,screenVar)
   #     fx,fy,fontCount,moveText,k,j,i,running = update(fx,fy,fontCount,moveText,k,j,i,running)
    myClock.tick(60)#60 fps
#closing files
introText.close()
floweyText.close()
quit()

