from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(x, 0)
        self.dy = 0

    def move_up(self):
        self.dy = 5

    def move_down(self):
        self.dy = -5

    def stop(self):
        self.dy = 0


    def update(self):
        self.sety(self.ycor() + self.dy)
        if self.ycor() > 250:
            self.sety(250)
            self.stop()

        elif self.ycor() < -240:
            self.sety(-240)
            self.stop()

        
