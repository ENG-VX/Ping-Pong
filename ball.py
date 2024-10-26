from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def moving(self, L_paddle, R_paddle):

        x,y = self.pos()
        if y>=280 or y<=-280:
            self.y_move *= -1
            
        if x>=380 or x<=-380:
            self.x_move *= -1

        if self.distance(L_paddle)<=50 and x<=-360 :
            self.x_move *= -1

        if self.distance(R_paddle)<=50 and x>=360 :
            self.x_move *= -1
            
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
    