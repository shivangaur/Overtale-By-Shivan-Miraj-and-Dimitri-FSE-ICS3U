#importing modules 
from pygame import *
from random import *
from math import *
from pprint import *
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'#centering the screen
#making a screen
size = width,height = 1000,750#size
screen = display.set_mode(size)

startTime=time.get_ticks()
showTime = (time.get_ticks()-startTime)//1000


display.set_caption("Overtale")  # Setting the window title
display.set_icon(transform.scale(image.load("Pictures/heart.png"),(32,32)))  # Setting the screen icon
#making basic colors  
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
k = 0
j = 0
i = 0
VY=2
BACKX=4
onGround=3

'''
The 'guy' player list of all the important points and coordiantes for the
current scene. These points get updated every time you move to the next scene
'''
guy = [X,Y,480,400,S,0,MAXX,2267,MAXY,800,MINX,-480,MINY,-400,MOVEL,-190,MOVER,1220,MOVEUP,-50]

toriel=[470,155,480,500,480,500,680,150,680,350]#toriel list. Only has the x and y position for toriel on the screen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  #GX GY SX  SY  MX   MX  MY MOVEL MOVER MAXX MAXY
scenes=[[0,0,480,400,1490,1630,41,-190,1220,2267,800,-50],[0,600,480,400,-50,40,20,0,0,460,930,-50],[0,600,480,400,-50,40,20,0,0,460,930,-50],[10,650,480,650,-40,40,-310,0,-10,460,650,-1000],[0,0,450,570,-80,30,-310,1,1000,460,1000,1],[0,0,400,650,1780,1800,1000,1,1270,2400,2300,1],[0,0,0,450,400,540,-220,1,0,2400,2300,1],[0,0,400,650,3260,3360,1000,1,2720,2400,2300,1],[0,20,20,450,3480,3500,1000,1,2560,2400,2300,60],[0,0,20,300,410,520,-40,1,-1,2400,800,0],[0,0,500,630,400,700,1000,1,1000,2400,800,1],[0,0,500,230,400,500,1000,1,-1,2400,800,0],[0,0,20,320,860,900,1000,1,-1,2400,800,0],[0,0,20,320,1350,1450,1000,1,500,2400,800,0],[0,0,20,320,1650,1850,1000,1,760,2400,800,0],[0,0,20,340,1650,1850,1000,1,760,2400,800,0],[0,0,20,370,840,920,1000,1,0,2400,800,0],[0,0,20,370,840,920,1000,1,0,2400,800,0],[0,0,20,370,840,920,1000,1,0,2400,800,0],[0,0,880,400,-320,-160,-110,1,0,2400,800,0],[0,0,250,650,1460,1570,-130,1,790,2400,800,0],[0,0,20,230,1520,1670,1000,1,660,2400,800,0],[0,0,20,330,590,750,-1000,1,50,2400,800,0],[0,0,170,40,590,750,-1000,1,50,2400,800,0]]


''' ^^^^ probably one of the most important features in the code.
This 'scenes' list, is a 2d list of lists for each individual scene. Every
element in the list consists of the guyX,guyX, the screen Pos, and many other
important coordinates for the current scene.
'''
#Lists used in combat
heart1=[250,650,0,True, 0] 
heart2=[500,335,0,True, 0]
heart = [475,600,50,50]
heart1=[250,650,0,True, 0]
heart3=[600,650]
heartRect = Rect(heart[X],heart[Y],50,50)
HX = 475
HY = 475
heart = [HX,HY,100,100]
badGuys = [[0,0], [200,0], [400,0], [600, 0],[800, 0],[1000, 0]]
introPics = []
balls=[i*75 for i in range (0,15)] 
balls1=[]
for ba in balls:
    balls1.append([ba,0])
move=0#variable for the current direction that the player is at e.g left,right,up,down---> 0,1,2,3
frame=0#the frame for each move
#initializing font
font.init()
consolas = font.SysFont("Consolas",40)#loading comic sans font
consolasPlay=font.SysFont('Consolas',12)
consolas2 = font.SysFont("Consolas",29)

#initializing sounds
mixer.init()
musicChannel = mixer.Channel(0)#making a mixer
musicChannel2 = mixer.Channel(1)
introMusic = mixer.Sound("Sound/introMusic/intro.ogg")
#musicChannel.play(introMusic)

#making a clock
myClock = time.Clock()
myClock.tick(60)#making the program run 60 times per second

#opening text files
introText = open("text/intro/intro text.txt","r")#opening intro slides' text
slideTexts = introText.readlines()#getting a list of each line(slide) of dialogue


floweySound = mixer.Sound("Sound/characters/flowey.ogg")
floweyTheme = mixer.Sound("Sound/themes/flowey.ogg")
floweyLaugh = mixer.Sound("Sound/characters/floweyLaugh.ogg")
torielSound = mixer.Sound("Sound/characters/toriel.ogg")
floweyIntro = open("combattext/flowey/floweyintro.txt")
floweyEnd = open("combattext/flowey/floweyend.txt")
floweyToriel = open("combattext/flowey/floweytoriel.txt")
screenVar = False
screenshot = screen.copy()


heartPic=image.load("Pictures/heart.png")
torielPic = transform.scale(image.load("Pictures/toriel/Toriel22.png"),(225,225))
normalFlowey = image.load("Pictures/flowey/flowey.jpg")
#guy=[X,Y,480,400]
heart=[460,450,50,50]
floweyCombat = image.load("Pictures/combat/floweyfight.jpg")
floweyTalking = image.load("Pictures/flowey/floweyTalking.jpg")
floweyLaughing = image.load("Pictures/flowey/floweyLaughing.png")
fireballPic = transform.scale(image.load("Pictures/combat/fireball.png"),(50,50))
textBoxPic = image.load("Pictures/combat/text.jpg")
fightBox = image.load("Pictures/combat/fightBox.png")
papyrusPic=image.load("Pictures/combat/papyrusFight.jpg") #4000x500

guyPic = image.load("Pictures/guy/guy.png")#29x31
openPic=image.load('Pictures/introPics/opening.jpg')
heartPic = image.load("Pictures/heart.png")
#backPic=image.load("Pictures/combat/papyrusFight.jpg") #4000x500

##toriel Script Images
torielScript2=image.load('text/characters/toriel/torielScript2.png')
torielScript3=image.load('text/characters/toriel/torielScript3.png')
torielScript4=image.load('text/characters/toriel/torielScript4.png')
torielScript5=image.load('text/characters/toriel/torielScript5.png')
torielScript6=image.load('text/characters/toriel/torielScript6.png')
torielScript7=image.load('text/characters/toriel/torielScript7.png')
torielScript8=image.load('text/characters/toriel/torielScript8.png')
torielScript9=image.load('text/characters/toriel/torielScript9.png')
#######Other script Images
brainwash=image.load('text/other/brainwash.png')
sansSign=image.load('text/other/sansSign.png')
decoy=image.load('text/other/decoy.png')
candy=image.load('text/other/candy.png')
sansScript=image.load('text/characters/other/sansScript.png')
cheese=image.load('text/characters/other/cheese.png')
endScript=image.load('text/other/endScript.png')
frog1=image.load('text/characters/other/frog1.png')
frog2=image.load('text/characters/other/frog2.png')
frog3=image.load('text/characters/other/frog3.png')
floweySceneScript=image.load('text/characters/flowey/floweyScript.png')





#flowey
floweyText=open('text/characters/flowey/flowey.txt')
floweyPic=image.load('Pictures/flowey/flowey001.png')
script=floweyText.readlines()






#####DEFINING FUNCTIONS
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
def drawIntroScene(count,k,j,i,fx,fy,script,introPics,picture,running):
    '''
    this function draws the picture, text and also keeps track of the music
    '''
    if not musicChannel.get_busy():# if there isnt any music playing
        musicChannel.play(introMusic) # play the background music
    if count % 12 == 0 and picture < 7: # if there is text in the slide and it is supposed to show up
        if k < len(script): # making sure the program doesnt crash by accessing the list with a counter that is too high
            if j < len(script[k]): # ^^
                if i < len(script[k][j]): # ^^
                    if not script[k][j][i] == "~": # if the program isnt suppposed to go to the next line
                        character = consolas2.render(script[k][j][i],True,WHITE) # render the letter
                        screen.blit(character,(fx,fy)) # blit the letter
    else: # if the slide doesnt have text
        if count % 12 ==0:
            if k < len(script):
                if j < len(script[k]):
                    if i < len(script[k][j]):
                        character = consolas2.render(script[k][j][i],True,BLACK) # render the letter in BLACK so that the user doent see it
                        screen.blit(character,(fx,fy)) # blit it (this is to prevent an error that would happen without any text on a slide
    character = consolasPlay.render("Press Enter To Skip",True,WHITE) # rendering text
    screen.blit(character,(800,25)) # blitting the text
    try: # the program crashes if it reaches the end, so this is a try and except statement that prevents it from crashing and just blits the last picture when neccessary
        screen.blit(introPics[picture],(175,100)) # blit the picture
    except: # if the program crashes
        screen.fill(BLACK) # fill the screen with black
        screen.blit(character,(800,25)) # blit the charater, which is "press enter to skip"
        screen.blit(introPics[-1],(175,-555)) # blit the last intro pic
        time.wait(1000)
        running = False
    display.flip() # show all the above

    return running
def checkSkip(running,keys):
    if keys[K_RETURN]:
        musicChannel.pause()
        running = False
    return running
def updateIntro(count,k,j,i,fx,fy,running,script,moveText,switch,picture):
    '''
    fuinction that updates all variables that need to be updated
    '''
    if count % 12 == 0 and k < len(script) and j < len(script[k]): # if text is supposed to appear
        if not i+1 == len(script[k][j]): # this is commented later on in the program
            i+=1 
            moveText = True 
        else: 
            i = 0
            if not j+1 == len(script[k]):
                j+=1
                if fx != 175:
                    fx+=15
            else:
                j = 0
                if not k+1 == len(script):
                    k+=1
                    fx = 175
                    fy = 500
                    switch = True
                    draw.rect(screen,BLACK,(100,500,800,200))
                else:
                    running = False
    else: # this makes the program go through the intro code
        if count % 12 == 0:
            if not k+1 == len(script):  # if its not the end of the code
                switch = True # switch the scene
                time.wait(1000) # wait so that the user can see the picture
    if switch: # if its supposed to switch to the next picture
        picture += 1 # go to the next one
        switch = False # make sure it doesnt skip too many times
    if k < len(script): # already explained
        if j < len(script[k]):
            if i < len(script[k][j]):
                if script[k][j][i] == "~" and count % 12 ==0: # if the prgoram is supposed to show text on the next line
                    fx = 175 # reset the font x position
                    fy += 40 # increase the font y so that it goes to the next line
                    moveText = False # dont move the next letter
    if moveText and count % 12 == 0: # if the next lettter is supposed to be moved
        fx += 15 # incrase the font x position
    count += 1 # increase count
    return count,k,j,i,fx,fy,running,moveText,switch,picture

def intro():
    introPics = []
    for i in range(11):
        introPics.append(image.load("Pictures/introPics/intro%s.jpg"%str(i+1)))
    text = open("text/intro/intro text.txt","r") # making the intro pics a list
    script = make3D(text) # making the script
    count = 0 # count variable to keep track of text 
    running = True 
    moveText = False # variable to move letters over
    switch = False # variable to check if the picture is supposed to change
    picture = 0 # the index used to blit pictures
    k = 0 # indexes used for blitting text
    j = 0 # ^^
    i = 0 # ^^
    fx = 175 # starting font x position
    fy = 500 # starting font y position
    while running:
        for evnt in event.get():                
            if evnt.type == QUIT:
                running = False
                
        mx,my = mouse.get_pos() # getting input from the user
        mb = mouse.get_pressed()
        keys = key.get_pressed()
        myClock.tick(60) # 60 fps
        running = checkSkip(running,keys)
        running = drawIntroScene(count,k,j,i,fx,fy,script,introPics,picture,running) # drawing scene
        count,k,j,i,fx,fy,running,moveText,switch,picture = updateIntro(count,k,j,i,fx,fy,running,script,moveText,switch,picture) # updating variables
    text.close() # closing the script
    return "intro" # returning the next part of the game

def drawSans(screen,balls1,heart):#draws the scene
                                   #gravity is the speed and direction
                                   #of the balls' x and y coordinates
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

floweyIntroScript = make3D(floweyIntro)
floweyEndScript = make3D(floweyEnd)
floweyTorielScript = make3D(floweyToriel)

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
    if keys[K_ESCAPE]:
        quit()
def moveHeartSans(heart):
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
        
def checkCollision(heart,els):
    if els[0].colliderect(heart) or els[1].colliderect(heart) \
       or els[2].colliderect(heart) or els[3].colliderect(heart) \
       or els[4].colliderect(heart):
        return True
    return False

def checkCollide(guy,guyReal):
    X, Y = 0, 1
    count=0
    collideCenter = (int(guy[X]), int(guy[Y]))
    if screen.get_at(collideCenter) == WHITE:
        gameOver()
        return 'over'
        
def gameOver():
    global guy,writing,balls1,BACKX,heart1,heart3,onGround,scenes,casex,casey,toriel,position,heart2,badGuys
    screen.fill(BLACK)
    go=consolas.render('GAME OVER',True,RED)
    display.flip()
    time.wait(5000)
    screen.blit(go,(450,400))
    casex=casey=0
    guy = [X,Y,480,400,S,0,MAXX,2267,MAXY,800,MINX,-480,MINY,-400,MOVEL,-190,MOVER,1220,MOVEUP,-50]
    BACKX=4
    onGround=3
    writing=True
    balls=[i*75 for i in range (0,15)] 
    balls1=[]
    for ba in balls:
        balls1.append([ba,0])
    toriel=[470,155,480,500,480,500,680,150,680,350]
    position=0
    heart1=[250,650,0,True, 0]
    heart2=[500,335,0,True, 0]
    badGuys = [[0,0], [200,0], [400,0], [600, 0],[800, 0],[1000, 0]]
    
    

def finish():
    '''Function to end the game. This just constantly blits THE END to show that
the player has completed the game'''
    end=consolas.render('THE END',True,WHITE)
    running=True
    keys=key.get_pressed()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        if keys[K_RETURN]:
            quit()
        screen.fill(BLACK)
        screen.blit(end,(450,300))
        
        display.flip()
def sans(guy):
    '''Function for final encounter of the game which is the most difficult
one. If the player touches any white objects they have to restart the game'''
    global writing
    writing=False
    myClock=time.Clock()
    startTime=time.get_ticks()
    running=True
    keys=key.get_pressed()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        drawSans(screen,balls1,heart3)#drawing
        moveHeartSans(heart3)#moving heart
        if checkCollide(heart3,guy)=='over':#checking is player hit obstacles
            gameOver()#restarting the player
            return 'lose'

        myClock.tick(60)
        showTime = (time.get_ticks()-startTime)//1000

        if showTime >= 25:#if the player lasts 25 seconds they win
            return 'win'


        
    
        display.flip()

   
def movePellets(move,els,k,count,done,graphic,torielBool,torielRect,fireballRect):
    '''Function to move the flowey pellets'''
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
            if count >= 1360:
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
        if els[0][1] >= 750:
            done = True
            pellets = False
    if graphic:
        if not torielBool:
            if fireballRect[0] >= 580:
                fireballRect[0] -= 3
                screen.blit(floweyLaughing,(389,155))
                display.flip()
            else:
                torielBool = True
        else:
            torielRect[0] -= 3
    return els,count,done,graphic,torielBool,torielRect,fireballRect

def update(count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount,script,floweyScript,done,running,graphic,torielBool,torielRect,fireballRect):
    if checkCollision(heart,els):
        pellets = False
        done = True
    if pellets == False:
        text = True
    count+=1
    els,pelletCount,done,graphic,torielBool,torielRect,fireballRect = movePellets(pellets,els,k,pelletCount,done,graphic,torielBool,torielRect,fireballRect)
    if k < len(floweyScript):
        if j < len(floweyScript[k]):
            if i < len(floweyScript[k][j]):
                if floweyScript[k][j][i] == "~":
                    if count % 12 == 0:
                        fx = 640
                        fy += 35
                        moveText = False
    if moveText:
        if count % 12 == 0:
            fx+=16 
    if count % 12 == 0 and text:
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
                    if k == 8 and not done:
                        pellets = True
                else:
                    k = 0
                    text = False
                    if floweyScript == floweyIntroScript:
                        floweyScript = floweyEndScript
                    elif floweyScript == floweyEndScript:
                        floweyScript = floweyTorielScript
                        graphic = True
                    elif floweyScript == floweyTorielScript:
                        running = False
    if torielRect[0] <= 379:
        graphic = False
        text = True
    moveText = True
    return count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount,script,floweyScript,done,running,graphic,torielBool,torielRect,fireballRect

def drawFloweyScene(count,fx,fy,text,k,j,i,floweyScript,heart,moveText,pellets,els,graphic,torielBool,torielRect,fireballRect,done):
    ''''Drawing the actual flowey scene'''
    global screenVar
    global screenshot
    screen.blit(floweyCombat,(0,0))
    if not graphic:
        screen.blit(textBoxPic,(600,175))
    else:
        if not text:
            draw.rect(screen,BLACK,(600,175,400,250))
    if pellets:
        draw.ellipse(screen,WHITE,els[0])
        draw.ellipse(screen,WHITE,els[1])
        draw.ellipse(screen,WHITE,els[2])
        draw.ellipse(screen,WHITE,els[3])
        draw.ellipse(screen,WHITE,els[4])
    if graphic:
        screen.blit(floweyCombat,(0,0))
        if not torielBool:
            screen.blit(fireballPic,(fireballRect[0],205))
            screen.blit(floweyLaughing,(389,155))
        else:
            screen.blit(torielPic,(torielRect[0],120))
    if j == 0 and i == 0 and count % 12 == 0:
        screen.blit(textBoxPic,(600,175))
    else:
        if screenVar:
            if not graphic:
                screen.blit(screenshot,(600,175))
    if not floweyScript == floweyEndScript:
        if not torielBool:
            if graphic:
                screen.blit(floweyLaughing,(389,155))
            elif count % 30 == 0 and text:
                screen.blit(floweyTalking,(389,155))
            else:
                screen.blit(normalFlowey,(389,155))
        else:
            if not graphic:
                screen.blit(torielPic,(torielRect[0],120))
    else:
        if done:
            screen.blit(floweyLaughing,(389,155))
            if count % 300 == 0 and not graphic:
                musicChannel.play(floweyLaugh)
    if pellets and not done:
        screen.blit(normalFlowey,(389,155))
    screen.blit(heartPic,(heart[X]-25,heart[Y]-25))
    if done == True:
        musicChannel2.pause()
    if text and not graphic:
        if count % 100 == 0:
            if not torielBool:
                if floweyScript == floweyEndScript:
                    if k > 0 or j >= 1:
                        musicChannel.play(floweySound)
                else:
                    musicChannel.play(floweySound)
            else:
                if k >= 1:
                    musicChannel.play(torielSound)
        if not musicChannel2.get_busy():
            musicChannel2.play(floweyTheme)
        if count % 12 == 0:
            if k < len(floweyScript):
                if j < len(floweyScript[k]):
                    if i < len(floweyScript[k][j]):
                        if floweyScript[k][j][i] != "~":
                            character = consolas.render(floweyScript[k][j][i],True,BLACK)
                            screen.blit(character,(fx,fy))
                            screenVar = True
                            if floweyScript == floweyEndScript:
                                moveText = True
    display.flip()
    if not text:
        musicChannel.pause()
    else:
        musicChannel.unpause()
    screenshot = screen.copy().subsurface(600,175,362,171)

def floweyFight():
    ''''Single function to call the flowey fight. All helper functions are
called in this.
    '''
    count = 0
    i = 0
    j = 0
    k = 0
    fx = 630
    fy = 200
    text = True
    running = True
    moveText = True
    pellets = False
    script = False
    done = False
    graphic = False
    torielBool = False
    floweyScript = floweyIntroScript
    torielRect = [1000,100]
    fireballRect = [1000,205]
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
        drawFloweyScene(count,fx,fy,text,k,j,i,floweyScript,heart,moveText,pellets,els,graphic,torielBool,torielRect,fireballRect,done)
        count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount,script,floweyScript,done,running,graphic,torielBool,torielRect,fireballRect = update(count,fx,fy,moveText,k,j,i,text,pellets,els,pelletCount,script,floweyScript,done,running,graphic,torielBool,torielRect,fireballRect)                                                                                                                                                                    
    return "x"              

###Backgrounds and Masks
backPics=addPics('back',1,24)
maskPics=addPics('mask',1,24)





def drawSlides(text,picture):#defining a function that draws intro slides
    '''Drawing the intro picture sequence'''
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

def drawPictures(picture):
    '''Defining function that will blit the picture of the slides'''
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
def transCooler(width,height):
    '''Function that makes a unique transition into the final fight'''
    for i in range(2000):
        col=(randint(0,255),randint(0,255),randint(0,255))
        end=(randint(0,1000),randint(0,750))
        draw.line(screen,col,(500,325),end)
        display.flip()
    
def transCool(width,height,col):
    '''Function that makes a cool trasition scene and blits 'Success' to tell
the player they have pulled down the lever correctly'''
    for i in range(0,width+50,50):
        for j in range(0,height+50,50):
            draw.circle(screen,col,(i,j),29)
            time.wait(1)
        display.flip()
    for i in range(0,height+50,50):
        for j in range(0,width+50,50):
            draw.circle(screen,WHITE,(j,i),35)
            time.wait(1)
        display.flip()
    fade(width,height,BLACK)
    text=consolas.render('SUCCESS!!!',True,(255,255,0))
    screen.blit(text,(400,300))
    display.flip()
    time.wait(1000)
    
casex=casey=0#Variables for the difference when the scene goes from the background
#moving to the player moving

def moveGuy(guy):
    ''' Main function for player movement'''
    #globalizing variables needed
    global move,frame,casex,casey,difx,dify,writing
    

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

    
    

def drawPellets(heartRect,pellets):
    '''Function for drawing the flowey pellets'''
    for pell in pellets:
        draw.ellipse(screen,WHITE,pell)


    
    
def floweyEncounter(picsList,guy,mono2):
    '''drawing everything for the flowey scene including the text box, text, and
the heart phase transition scene
    '''
        
    if mono2:#boolean value to make the text blit only once
        writing=False#player cant move
        textBox(40,20,width-200,150,'flowey')
        screen.blit(floweySceneScript,(200,35))#script
        display.flip()#displaying
        time.wait(10000)#pausing so user can read
        mono2=False
    heartPhase(guy,picsList)#making the player transition to the first fight
    floweyFight()#flowey fight

        
    guy[S]+=1#moving to the next scene

bet=True


def papyrus(guy):
    '''Function for the easiest and first REAL fight of the game'''
    global writing
    writing=False
    myClock=time.Clock()
    running=True
    startTime=time.get_ticks()
   
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
        showTime = (time.get_ticks()-startTime)//1000
        screen.blit(papyrusPic,(heart1[BACKX],0))
        offset=250-heart1[X]
            
        keys=key.get_pressed()

        if heart1[BACKX] > -4700:
            heart1[BACKX]-=10   #the background is what is moving

        if keys[K_UP] and heart1[onGround]:#jumping only if ON GROUND
            heart1[VY]=-15 #jupming power
            heart1[onGround]=False                
        heart1[Y]+=heart1[VY]
            
        if heart1[Y]>=650:
            heart1[Y]=650   #set it on ground
            heart1[VY]=0    #stop falling
            heart1[onGround]=True

        heart1[VY]+=0.7 #apply gravity


        collideCenter = (int(heart1[X]) + 25, int(heart1[Y] + 25))
        if screen.get_at(collideCenter) == WHITE:
            gameOver()
            return 'lose'

        if showTime==8:#goes on for 8 seconds
            return 'win'


        screen.blit(heartPic, (heart1[X], heart1[Y]))

        myClock.tick(60)
        
        if key.get_pressed()[27]:
            running=False
            
        display.flip()
    return "m"
def moveBadGuys(badGuys, goodX, goodY):
    '''the enemy balls (put in the
    badguys list) will follow the
    heart's position (goodX,goodY)
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
def drawTorielFight(screen, badGuys, goodX, goodY):#draws the heart and background
    '''draws the toirel fight scene'''
    screen.fill((0,0,0))
    for guy in badGuys:
        draw.circle(screen, WHITE, guy, 10)

    screen.blit(heartPic,(heart2[X],heart2[Y]))
    display.flip()
    
def checkCollideToriel(guy):
    '''checks if the heart collides with
    any white areas
    '''
    X, Y = 0, 1
    count=0
    collideCenter = (int(guy[X]), int(guy[Y]))
    if screen.get_at(collideCenter) == WHITE:
        gameOver()
        return 'lose'
        
def torielFight():
    '''Single function for toriel fight that calls all other functions'''
    global writing
    writing=False
    myClock=time.Clock()
    running=True
    startTime=time.get_ticks()
    keys=key.get_pressed()
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        moveHeart(heart2)#moving heart
        drawTorielFight(screen,badGuys,heart2[X]+25,heart2[Y]-25)#drawing
        moveBadGuys(badGuys, heart2[X], heart2[Y])#enemies following
        if checkCollideToriel(heart2)=='lose':
            return
        myClock.tick(60)
        showTime = (time.get_ticks()-startTime)//1000
        if showTime>30:#The player must last 30 seconds without being touched
            return 'win'


        if key.get_pressed()[27]:
            running=False

        

        display.flip()

def drawMenu(pic1,pic2):
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
        screen.blit(pic1,(200,100))
        screen.blit(pic2,(200,300))
        keys=key.get_pressed()

        if keys[K_RETURN]:#exiting the menu
            bet=False
            return
            
        display.flip()
cond=False
drawTor=True#boolean value that will be used throught the entire drawToriel
#function. It restricts certain parts of the code from repeating
torielMovements=['up','up','up','up','up']
#list of toriel movements so toriel can move by itself without any key control

position=0# position in the toriel movemenets list
moveTor=frameTor=0 #move and frame variables for the Toriel picsList
count=0
def moveToriel(x,y):
        '''Function similar to moveGuy but for toriel'''
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
        writing=False#player cant move
        if count%10==0:
            if position<len(torielMovements)-1:#preventing index errors
                position+=1
        if position==len(torielMovements)-1:#if the position is the last
            #position, then the player can finally move
            writing=True
        if toriel[1]<-50:
            torielMovements[-1]='None'
        
        
    
    
    
def drawToriel(picsList):
    '''This function draws the toriel character whenever she appears in scenes,
because he only appears in certain scenes.
    '''
   # print(toriel[4],toriel[5])
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
            textBox(140,150,width-230,170,'toriel')#making textbox
            screen.blit(torielScript2,(300,165))
            screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
            display.flip()
            time.wait(10000)
            fade(width,height,BLACK)
            drawTor=False
    if guy[S]==5 and not drawTor:
        textBox(140,150,width-230,170,'toriel')#making textbox
        screen.blit(torielScript3,(300,165))
        display.flip()
        time.wait(10000)
        fade(width,height,(128,0,128))
        drawTor=True
        
    if guy[S]==6:
         #screen.blit(torielPics[1][0],(260,150))
         if drawTor and guy[X]<80:
             screen.blit(backPics[guy[S]],(0,0))
             screen.blit(torielPics[1][0],(260,150))
             screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
             textBox(140,450,width-230,170,'toriel')
             screen.blit(torielScript4,(300,465))
             display.flip()
             time.wait(10000)
             drawTor=False
         if not drawTor:
            keys=key.get_pressed()
            if guy[Y]<=-130:
                textBox(140,450,width-230,170,'toriel')
                screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
                screen.blit(torielScript5,(300,465))
                display.flip()
                time.wait(10000)
                papyrus(guy)
                writing=True
                torielMovements=['right','right','down','down','left','left','up','up','right','right','down','down','left','left','up','up','right','right','down','down','left','left','up','up','right','left','None','None']
                drawTor=True
    
    if guy[S]==8:
        if drawTor and guy[X]>2400:
            moveToriel(6,7)
            screen.blit(torielPics[moveTor][int(frameTor)],(toriel[6],toriel[7]))
        if writing and drawTor and guy[X]>2400:
            textBox(140,450,width-230,170,'toriel')
            screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
            screen.blit(torielScript7,(300,465))
            display.flip()
            time.wait(5000)
            fade(width,height,BLACK)
            #torielFight()
            #writing=True
            drawTor=False
    if guy[S]==15:
        if not drawTor:
            moveToriel(8,9)#moving
            screen.blit(torielPics[moveTor][int(frameTor)],(toriel[8],toriel[9]))
        if not drawTor and writing:#right after the moving is done
            screen.blit(backPics[guy[S]],(0,0))
            textBox(140,450,width-230,170,'toriel')
            screen.blit(torielScript8,(300,465))
            screen.blit(torielPics[moveTor][int(frameTor)],(toriel[8],toriel[9]))
            screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
            display.flip()
            time.wait(10000)
            if torielFight()=='win' and not drawTor:#toriel fight
                screen.fill(BLACK)
                textBox(140,250,width-230,170,'toriel')
                screen.blit(torielScript9,(300,265))#toriel dying script
                display.flip()
                time.wait(10000)
                fade(width,height,BLACK)
            writing=True#player can move
            drawTor=True
    if guy[S]==16:
        #blitting cheese text,letting the player know that the cheese is actually
        #important
        if guy[X]>530 and drawTor:
            textBox(140,250,width-230,170,'toriel')
            screen.blit(cheese,(150,265))
            display.flip()
            time.wait(5000)
            drawTor=False
    if guy[S]==20:
        #blitting the frog texts at the right time
        if 200<guy[X]<500 and not drawTor:
            textBox(140,450,width-230,170,'toriel')
            screen.blit(frog1,(150,465))
            display.flip()
            time.wait(10000)
            drawTor=True
        if 590<guy[X]<720 and  drawTor:
            textBox(140,450,width-230,170,'toriel')
            screen.blit(frog2,(150,465))
            display.flip()
            time.wait(10000)
            drawTor=False

        if guy[X]>960 and not drawTor:
            textBox(140,450,width-230,170,'toriel')
            screen.blit(frog3,(150,465))
            display.flip()
            time.wait(10000)
            drawTor=True

    if guy[S]==22:#Final scene before battle
        keys=key.get_pressed()
        if guy[X]>=710 and guy[Y]>=390:#near red child
            if keys[K_RETURN]:#user clicks enter
                textBox(140,150,width-230,170,'toriel')
                screen.blit(sansScript,(145,165))
                screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
                display.flip()
                time.wait(5000)
                transCooler(width,height)#unique transition
                sans(guy)#Final boss fight
                writing=True#player can move
    if guy[S]==23:#toriels house
        if guy[Y]>100:
            screen.blit(backPics[guy[S]],(-guy[X],-guy[Y]))
            textBox(140,250,width-230,170,'toriel')
            screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
            screen.blit(endScript,(150,265))
            display.flip()
            time.wait(20000)
            finish()#ending the game
        
    
        
         
        
            
        
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
lev=0
def levers(cond):
    '''Function for scene with levers, not allowing the player to pass the scene
without pressing enter near a lever. They can also use the same lever 3 times
    '''
    global lev
    keys=key.get_pressed()
   # lev1=lev2=lev3=False
    if keys[K_RETURN]:
        if guy[Y]<-400:
            if 720<=guy[X]<=790:
                cond=True
              #  lev1=True
            elif 1320<=guy[X]<=1420:
                cond=True
               # lev2 =True
            elif 1480<=guy[X]<=1540:
                cond=True
                #lev3=True
    if cond:
        #transCooler(width,height)
        transCool(width,height,(randint(0,255),randint(0,255),randint(0,255)))
        lev+=1
        if lev>=3:
            return True
    return False
def room11(guy):
    '''This function is for the 11th scene, so that when you reach the center,
the entrance becomes the exit'''
    global cond,bet
    if -40<=guy[X]<=10 and guy[Y]<-260:#if the player reaches the center
        cond=True#condition becomes true
    if cond and bet:
       # textBox(120,600,width-80,150,'black')#draws textbox
        drawMenu(decoy,candy)#draws menu
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
        #textBox(120,600,width-80,150,'black')#text box
        drawMenu(sansSign,brainwash)#drawing menu
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
def drawScene(screen,picsList,backPics,guy):
    '''This is the main drawScene function where the background, and player are blitted.
    There are many different cases for how the background can be blitted'''
    global mono2,casex,casey,cond,bet,script,position,back
    #print(guy[X],guy[Y],guy[2],guy[3],guy[S])

    mono=False
    
    #If statement to update all the 'guy' list elements once the player enters
    #a new scene
    #If the players X value is between the given values, and it's Y value is below
    #the given value, then switch scenes
    if back:
        if scenes[guy[S]][4]<guy[X]<scenes[guy[S]][5] and guy[Y]<scenes[guy[S]][6]:
            fade(1000,750,BLACK)#fade transition
            #print('here')
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
trav=False
def checkEncounter(guy,mono2,picsList):
    global trav
    '''This function is pretty important because it acts like a sort of database to organize all the encounters.
it is called in the drawScene function and calls the other specfic encoutner functions''' 
    if guy[S]==1:#first scene
        if guy[Y]<550:#moving close to flowey
            floweyEncounter(picsList,guy,mono2)#flowey encounter
    if guy[S]==5:
        if levers(False):
            trav=True
        if not trav:
            if guy[X]>1690:
                guy[X]=1690
                guy[2]=820
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
        fade(width,height,BLACK)#cool transition
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
    #pprint(letters)
    #pprint(lowers)
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
        text=consolas.render("Name the fallen human & click Tab",True,WHITE)#text at the top of the screen
        screen.blit(text,(180,80))#blitting text
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
        screen.blit(nameText,(370,660))#blitting name
        

        myClock.tick(60)
        
        display.flip()#displaying

screen.fill(BLACK)#filling BLACK


intro()
drawIntro()
chooseName()


pics=[addPics('guy',1,3),#2d list of guy pictures
    addPics("guy",4,6),addPics('guy',7,9),addPics('guy',10,12)]            

torielPics=[addPics('toriel',1,4),addPics('toriel',5,8),#2d list of toriel pictures
            addPics('toriel',9,12),addPics('toriel',13,16)]


running=True
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    

    moveGuy(guy)

    drawScene(screen,pics,backPics,guy)

    myClock.tick(60)#60 fps
#Closing text Files
introText.close()
floweyText.close()
quit()

