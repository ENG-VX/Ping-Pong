from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 1
        self.y_move = 1

    def moving(self, L_paddle, R_paddle, score):
        # اذا ضربت الكرة باحد الحدود الرأسية
        x,y = self.pos()
        if y>=280 or y<=-280:
            self.y_move *= -1

        # اذا تعدت الجد الايمن    
        if x>=415:
            score.L_scoer += 1
            score.update_score()
            self.goto(0,0)
            self.x_move = -1
            self.y_move = 1

        # اذا تعدت الحد الايسر
        if x<=-415:
            score.R_scoer += 1
            score.update_score()
            self.goto(0,0)
            self.x_move = 1
            self.y_move = -1

        # اذا ضربت بالمضارب
        if (self.distance(L_paddle)<=50 and x<=-360) or (self.distance(R_paddle)<=50 and x>=360 ) :
            self.x_move *= -1

            if self.x_move > 0:
                self.x_move += 1
            else:
                self.x_move -= 1

            if self.y_move > 0:
                self.y_move += 1
            else:
                self.y_move -= 1
           
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
    