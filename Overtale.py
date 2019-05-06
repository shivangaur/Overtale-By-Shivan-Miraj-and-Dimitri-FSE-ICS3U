from pygame import *
from random import *
from math import *
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
font.init()
comicSansFont=font.SysFont("Consolas",30)
mixer.init()
musicChannel=mixer.Channel(0)

slides = []

def addSlide(text1, text2, picture, sound):
    global slides
    slides.append({"text1": text1, "text2": text2, "picture": picture, "sound": sound})

class slide:
    def __init__(self,text1,text2,picture,sound):
        self.text1=text1
        self.text2=text2
        self.picture=picture
        self.sound=sound
        
        
def drawSlide(text,text2,picture,sound):
    screen.blit(picture,(100,100))
    fx=140
    fy=410
    counter = 0
    
    for char in text:
        inc=0
        if char=="." or char=="," or char==":" or char==";":
            inc=300
        char=comicSansFont.render(char,True,WHITE)
        screen.blit(char,(fx,fy))
        fx+=13
        display.flip()
        if counter % 18 == 0:
            musicChannel.play(firstIntro.sound)
        counter += 1
        time.wait(55+inc)
    fx=140
    fy+=40
    for char in text2:
        inc=0
        if char=="." or char=="," or char==":" or char==";":
            inc=300
        char=comicSansFont.render(char,True,WHITE)
        screen.blit(char,(fx,fy))
        display.flip()
        time.wait(55+inc)
        fx+=13
    screen.fill(BLACK)
    mixer.pause()
    time.wait(1000)

def drawPicture(picture):
    screen.blit(picture,(100,100))
    display.flip()
    time.wait(3000)
    screen.fill(BLACK)

class picture:
    def __init__(self,picture):
        self.picture=picture

firstIntro=slide("Long ago, two races ruled over Earth:","HUMANS and MONSTERS.",image.load("Pictures/firstSlidePicture.png"),mixer.Sound("Sound/Sans talking test.ogg"))
secondIntro=slide("One day, a war broke out between the","two races.",image.load("Pictures/secondSlidePicture.jpg"),firstIntro.sound)
thirdIntro=slide("After a long battle, the humans were", "victorious.",image.load("Pictures/thirdSlidePicture.png"),firstIntro.sound)
fourthIntro=slide("They sealed the monsters underground","with a magic spell.",thirdIntro.picture,firstIntro.sound)
fifthIntro=slide("Many years later . . .","",image.load("Pictures/fifthSlidePicture.png"),firstIntro.sound)
sixthIntro=slide("MT. Rumnis","2016",image.load("Pictures/sixthSlidePicture.jpg"),firstIntro.sound)
seventhIntro=slide("Many people say that those who","climb the mountain never return.",image.load("Pictures/seventhSlidePicture.jpg"),firstIntro.sound)
        
firstPicture=picture(image.load("Pictures/eighthSlidePicture.jpg"))
secondPicture=picture(image.load("Pictures/ninthSlidePicture.jpg"))
thirdPicture=picture(image.load("Pictures/tenthSlidePicture.jpg"))
    

drawSlide(firstIntro.text1,firstIntro.text2,firstIntro.picture,firstIntro.sound)
drawSlide(secondIntro.text1,secondIntro.text2,secondIntro.picture,firstIntro.sound)
drawSlide(thirdIntro.text1,thirdIntro.text2,thirdIntro.picture,firstIntro.sound)
drawSlide(fourthIntro.text1,fourthIntro.text2,fourthIntro.picture,firstIntro.sound)
drawSlide(fifthIntro.text1,fifthIntro.text2,fifthIntro.picture,firstIntro.sound)
drawSlide(sixthIntro.text1,sixthIntro.text2,sixthIntro.picture,firstIntro.sound)
drawSlide(seventhIntro.text1,seventhIntro.text2,seventhIntro.picture,firstIntro.sound)

drawPicture(firstPicture.picture)
drawPicture(secondPicture.picture)
drawPicture(thirdPicture.picture)


running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

quit()
 
