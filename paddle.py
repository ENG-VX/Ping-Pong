from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(x,0)
        self.moveUP = True
        self.moveDOWN = True

    def move_up(self):
        self.moveUP = True
        self.moveDOWN = False
        while self.ycor()<250 and self.moveUP:
            self.goto(self.xcor(),self.ycor()+5)

    def move_down(self):
        self.moveUP = False
        self.moveDOWN = True
        while self.ycor()>-250 and self.moveDOWN:
            self.goto(self.xcor(),self.ycor()-5)
           


