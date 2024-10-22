from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(x,0)

    def move_up(self):
        while True:
            self.goto(self.xcor(),self.ycor()+5)

    def move_down(self):
        while True:
            self.goto(self.xcor(),self.ycor()-5)
           


