#importing what the program needs
from pygame import *
from random import *
from math import *
from pprint import *
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
myClock = time.Clock()
myClock.tick(60)
font.init()
mixer.init()
musicChannel = mixer.Channel(0)#making a mixer
introMusic = mixer.Sound("Sound/introMusic/intro.ogg")
consolas2 = font.SysFont("Consolas",29)
consolasPlay = font.SysFont("Consolas",14)
introPics = []
                    
##def addPics(name,start,end):
##    myPics=[]
##    for i in range(start,end+1):
##        myPics.append(image.load("Pictures/%s/%s%03d.png"%(name,name,i)))
##    return myPics

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

##def skipIntro(keys):
##    if key
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
intro()
print("hi")
