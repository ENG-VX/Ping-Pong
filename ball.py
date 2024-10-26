from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def moving(self, L_paddle, R_paddle, score):

        x,y = self.pos()
        if y>=280 or y<=-280:
            self.y_move *= -1


            
        if x>=380:
            score.L_scoer += 1
            score.update_score()
            self.goto(0,0)
            self.x_move *= -1


        if x<=-380:
            score.R_scoer += 1
            score.update_score()
            self.goto(0,0)
            self.x_move *= -1


  

        if (self.distance(L_paddle)<=50 and x<=-360) or (self.distance(R_paddle)<=50 and x>=360 ) :
            self.x_move *= -1.2
            self.y_move *= -1.2

            
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
    