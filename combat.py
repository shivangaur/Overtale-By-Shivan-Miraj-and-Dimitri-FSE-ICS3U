from pygame import *
from math import*
from random import*

size=width,height=1000,750

screen=display.set_mode(size)




class Combat:
    def __init__(self,health,frame,attack1,attack2):
        #self.hx=screen.get_pos(heart
        self.health=health
        self.frame=0
        self.attack1=attack1
        self.attack2=attack2
        self.heartImage=image.load("Pictures/heart.png")

        attackRect=rect(283,358,417,286)
        


    def attack1(self,target):
        dist=int(sqrt(dx**2+dy**2))
        moveX = (target.x - self.x)*self.speed/dist
        moveY = (target.y - self.y)*self.speed/dist
        self.ang = math.degrees(math.atan2(-moveY, moveX))
        self.x += moveX
        self.y += moveY

    def attack2(self,target):
        for i in range (420):
            rectx=702-i
            recty=randint(357,642)
            rectStart=(rectx,recty)
            rectEnd=(randint(357,542),recty)
            rect1=draw.line(screen,(255,255,255),(rectStart),(rectEnd))
            rect2=draw.line(screen,(255,255,255),(rectStart),(rectEnd+100))
            
        
            
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    display.flip() 

quit()
