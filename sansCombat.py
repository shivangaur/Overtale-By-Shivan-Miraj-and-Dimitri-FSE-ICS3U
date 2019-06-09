import turtle
import random

#wn means window

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0)

balls=[]

for i in range(10):
    #adds the object [turtles(shapes)]
    balls.append(turtle.Turtle())

colors=["blue","white","red"]
shapes = ["circle","triangle","square"]

for ball in balls:
    
    #shape of ball
    ball.shape(random.choice(shapes))

    #color
    ball.color(random.choice(colors))

    #move the pen up(Turtle function draws turtles)
    ball.penup()

    #animation speed(not speed of movement)
    ball.speed(2)
    
    x=random.randint(-290,290)
    y=random.randint(200,400)
    
    #goes to x,y
    ball.goto(x,y)

    #change in y and x
    ball.dy=0
    ball.dx=random.randint(-3,3)
    
    ball.da=random.randint(-5,5)
    
gravity=0.1

while True:

    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy-=gravity
        ball.sety(ball.ycor()+ball.dy)

        ball.setx(ball.xcor()+ball.dx)

        if ball.xcor()>300:
            ball.dx*=-1
            ball.da*=1

        if ball.xcor()<-300:
            ball.dx*=-1

        if ball.ycor()<-300:
            ball.sety(-300)
            ball.dy*=-1
            ball.da*=-1

wn.mainloop()
