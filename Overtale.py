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
#declaring basic vraiables

#declaring character's x and y position and making a list of them
X = 0 #character's x position
Y = 1 #character's y position
S  = 5
MAXX=7
MINX=11
MINY=13
MAXY=9
MOVEL=15
MOVER=17
MOVEUP=19

#there is no "vy" or jumping power because there is no jumping in the game
    #X  Y  PLAYER
#          POS ON
#          SCREEN
#          ITSELF
#           (x,y) #Scene#, Max x and Y
#                          coordinates
#                           for scene
guy = [X,Y,480,400,S,2,MAXX,2267,MAXY,800,MINX,-480,MINY,-400,MOVEL,-190,MOVER,1220,MOVEUP,-50]
                                                                                                                                                                                                                                                                                                                                                                                                                                #GX GY SX  SY  MX   MX  MY MOVEL MOVER MAXX MAXY
scenes=[[0,0,480,400,1490,1630,41,-190,1220,2267,800,-50],[0,600,480,400,-50,40,20,0,0,460,930,-50],[0,600,480,400,-50,40,20,0,0,460,930,-50],[10,650,480,650,-30,30,-310,0,-10,460,650,-1000],[0,0,450,500,-60,20,-220,1,1000,460,1000,1],[0,0,400,650,1780,1800,1000,1,1270,2400,2300,1],[0,0,0,450,400,540,-220,1,0,2400,2300,1],[0,0,400,650,3260,3360,1000,1,2720,2400,2300,1],[0,20,20,450,3480,3500,1000,1,2560,2400,2300,60],[0,0,20,300,900,1000,1000,1,-1,2400,800,0],[0,0,500,630,900,1000,1000,1,1000,2400,800,1]]
print('GX GY SX  SY  MX   MX  MY MOVEL MOVER MAXX MAXY')
pprint(scenes)
move=0
frame=0
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
    myPics=[]
    for i in range(start,end+1):
        myPics.append(image.load("Pictures/%s/%s%03d.png"%(name,name,i)))
    return myPics

def checkCombat():
    return False
#backPics=[]
backPics=addPics('back',1,21)
maskPics=addPics('mask',1,21)
#maskPics=[]
#unloadedPics=["Pictures/back/back1.png",'Pictures/back/back2.png']
#unloadedMaskPics=['Pictures/mask/mask1.png','Pictures/mask/mask2.png']

#for unload in unloadedPics:
#   backPics.append(image.load(unload))
#for unload in unloadedMaskPics:
 #   maskPics.append(image.load(unload))
    
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
    #global myclock
    for i in range(10):
        for k in range(75):
            draw.circle(screen,RED,(i*150,k*10),100)
            display.update()
            #myClock.tick(60)
def textBox(x,y,character):
    draw.rect(screen,BLACK,(x,y,width-80,150))
    draw.rect(screen,WHITE,(x,y,width-80,150),4)
    person=image.load('Pictures/'+character+'/'+character+'box'+'.jpg')
    screen.blit(person,(x+15,y+20))

writing=False
def drawFont(text,charSound,x,y):
    sound=mixer.music.load('Sound/characters/'+charSound+'.ogg')
    count=0
    fx=180
    fy=40
    for char in text:
        inc=0
        #print(char)
        if char=='\n':
            fx+=0
        elif char=='~':
            fx=180
            fy+=50
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
    fade = Surface((width, height))
    fade.fill(col)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        #redrawWindow()
        screen.blit(fade, (0,0))
        display.update()
        time.delay(5)
        
def transCool(width,height,col):
    for i in range(0,width+50,50):
        for j in range(0,height+50,50):
            #draw.rect(screen,BLACK,(0,0,i,j))
            draw.circle(screen,BLUE,(i,j),29)
            #draw.circle(screen,BLACK,(i-50,j),25)
            time.wait(5)
            display.flip()
    for i in range(0,height+50,50):
        for j in range(0,width+50,50):
            #draw.rect(screen,BLACK,(0,0,i,j))
            draw.circle(screen,WHITE,(j,i),35)
            #draw.circle(screen,BLACK,(i-50,j),25)
            time.wait(5)
            display.flip()
    fade(width,height,BLACK)
casex=casey=0
difx=dify=0
def moveGuy(guy,writing):
    #print(guy[2],guy[3])
    global move,frame,casex,casey,difx,dify
    difx=guy[X]-guy[2]
    dify=guy[Y]-guy[3]
    #print(guy[X],guy[Y],casex,casey)
    newMove=-1
    keys = key.get_pressed()
    #print(guy[S],len(backPics))
    if writing:
        if (keys[K_a] or keys[K_LEFT]):
            # and guy[X]>-480
            if checkPixelY(maskPics[guy[S]],guy[X]+guy[2]+casex-10,guy[Y]+guy[3]+casey,guyPic.get_height(),RED):
                if guy[X]<=guy[MOVEL]:
                    guy[2]-=10
                    casex+=10
                if guy[X]>=guy[MOVER]+10:
                    guy[2]-=10
                    casex+=10
                guy[X]-=10
                newMove=3
        elif (keys[K_d] or keys[K_RIGHT]):
            # and guy[X]<guy[MAXX]
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
    
            
##    if mono2:
##        writing=False
##        textBox(40,20,'flowey')
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
    
mono2=True
def heartPhase(guy,picsList):
    for i in range(5):
        screen.fill(BLACK)
        time.wait(200)
        display.flip()
        screen.blit(picsList[2][0],(guy[2]-2*i,guy[3]-2*i))
        time.wait(200)
        display.flip()
        screen.fill(BLACK)
        time.wait(200)
        display.flip()
        screen.blit(heartPic,(guy[2]+5-2*i,guy[3]+5-2*i))
        
        
        
        display.flip()
        
def drawScene(screen,picsList,backPics,guy,combat):
    global mono2,casex,casey
    #screen.fill(BLACK)
    #print(guy[X],guy[Y],guy[2],guy[3])
    print(guy[X],guy[Y],guy[2],guy[3],guy[MOVER],guy[MOVEUP],guy[MOVEL])
    mono=False
    
        
    if scenes[guy[S]][4]<guy[X]<scenes[guy[S]][5] and guy[Y]<scenes[guy[S]][6]:
        fade(1000,750,BLACK)
        guy[S]+=1
        guy[X]=scenes[guy[S]][0]
        guy[Y]=scenes[guy[S]][1]
        #print('b',guy[X],guy[Y])
        guy[2]=scenes[guy[S]][2]
        guy[3]=scenes[guy[S]][3]
        guy[MOVEL]=scenes[guy[S]][7]
        guy[MOVER]=scenes[guy[S]][8]
        guy[MAXX]=scenes[guy[S]][9]
        guy[MAXY]=scenes[guy[S]][10]
        guy[MOVEUP]=scenes[guy[S]][11]
        casex=casey=0
        #guy[MOVEUP]=scenes[guy[S]][11]
        print(1)
    elif guy[X]<=guy[MOVEL]-10 and guy[Y]<=guy[MOVEUP]:#the rest of the lines are chekcing where the character is, because if they are too far into one part of the scene we want to move the CHARACTER and NOT the background picture
        screen.blit(backPics[guy[S]],(-guy[MOVEL],-guy[MOVEUP]))
        print(2)
    elif guy[X]<=guy[MOVEL]-10:
        screen.blit(backPics[guy[S]],(-(guy[MOVEL]-10),-guy[Y]))
        print(3)
    elif guy[X]>=guy[MOVER] and guy[Y]<=guy[MOVEUP]:
        screen.blit(backPics[guy[S]],(-guy[MOVER],-guy[MOVEUP]))
    elif guy[X]>=guy[MOVER]:
        screen.blit(backPics[guy[S]],(-guy[MOVER],-guy[Y]))
        print(4)
        
    elif guy[Y]<=guy[MOVEUP]:
        screen.blit(backPics[guy[S]],(-guy[X],-guy[MOVEUP]))
        print(5)
    else:
        screen.blit(backPics[guy[S]],(-guy[X],-guy[Y]))
        print(6)
    screen.blit(picsList[move][int(frame)],(guy[2],guy[3]))
    checkEncounter(guy,mono2,picsList)
    #draw.circle(screen,RED,(gu,10)
    display.flip()
def checkEncounter(guy,mono2,picsList):
    if guy[S]==1:
        if guy[Y]<550:
            floweyEncounter(picsList,guy,mono2)
def drawIntro():
   myClock=time.Clock()
   running=True
   while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    screen.blit(openPic,(0,0))
    keys=key.get_pressed()
    if keys[K_RETURN]:
        transCool(width,height,BLUE)
        break

    
    myClock.tick(60)
    display.flip()
def chooseName():
    screen.fill(BLACK)
    lets=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ?!')
    lows=list('abcdefghijklmnopqrstuvwxyz?!')
    lowers=[]
    letters=[]
    count=0
    for i in range(1,5):
        letters.append(lets[7*(i-1):7*i])
        lowers.append(lows[7*(i-1):7*i])
    pprint(letters)
    pprint(lowers)
    coords=[]
    myClock=time.Clock()
    running=True
    posr=0
    posc=0
    lowr=lowc=0
    name=''
    case=0
    store=letters[:]
    while running:
        for evnt in event.get():                
            if evnt.type == QUIT:
                running = False
       
        keys=key.get_pressed()
        for i in range(1,5):
            for j in range(1,8):
                
                coords.append((100*((j%8)+1),50*i+100))
        
        for coor in coords:
            x=coords.index(coor)
            let=consolas.render(lets[x],True,WHITE)
            screen.blit(let,(coor[0]+7,coor[1]))
            draw.rect(screen,WHITE,(coor[0],coor[1],40,40),2)
            let=consolas.render(lets[x].lower(),True,WHITE)
            screen.blit(let,(coor[0]+7,coor[1]+302))
            draw.rect(screen,WHITE,(coor[0],coor[1]+300,40,40),2)
        text=consolas.render("Name the fallen human.",True,WHITE)
        screen.blit(text,(300,80))
        if not keys[K_CAPSLOCK]:
            letters=lowers
            case=302
        else:
            letters=store
            case=0
        
        if keys[K_TAB]:
            fade(width,height,WHITE)
        
            break
        
        
        
  
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
        high=consolas.render(letters[posr][posc],True,(255,255,0))
        #screen.blit(high,(coords
        #print(posr,posc)
        screen.blit(high,(coords[posc][0]+7,coords[posr*7][1]+case))
        if keys[K_RETURN]:
            if len(name)<11: 
                name+=letters[posr][posc]
        if keys[K_BACKSPACE]:
            name=name[:-1]
            draw.rect(screen,BLACK,(0,700,width,50))
        
        nameText=consolas.render(name,True,WHITE)
        screen.blit(nameText,(370,700))
        
            #screen.blit(nameText,(400,700))
        myClock.tick(60)
        
        display.flip()

screen.fill(BLACK)


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
pics=[addPics('guy',1,3),
    addPics("guy",4,6),addPics('guy',7,9),addPics('guy',10,12)]            

combat=False
running=True
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    
           
    moveGuy(guy,writing)
##    mb=mouse.get_pressed()
##    mx,my=mouse.get_pos()
##    if mb[0]==1:
##        print(screen.get_at((mx,my)))
    if checkCombat:
        combat=True
    drawScene(screen,pics,backPics,guy,combat)
    
    myClock.tick(60)
introText.close()
floweyText.close()
quit()

