from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def moving(self):
        x_add = 5
        y_add = 5
        while True:
            x,y = self.pos()
            if y>=280 or y<=-280:
                y_add *= -1
                
            elif x>=380 or x<=-380:
                x_add *= -1
                
            self.goto(self.xcor()+x_add, self.ycor()+y_add)
        