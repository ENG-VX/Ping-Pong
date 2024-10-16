from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(x,0)

    def move(self, direction=""):
        if direction == "up":
            self.goto(self.xcor(),self.ycor()+20)
            print("work")
        elif direction == "down":
            self.goto(self.xcor(),self.ycor()-20)



