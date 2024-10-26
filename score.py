from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,250)
        self.L_scoer = 0
        self.R_scoer = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.L_scoer}     {self.R_scoer}",align="center" , font=["Didone Room Numbers",24,"bold"])