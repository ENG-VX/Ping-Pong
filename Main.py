from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score

window = Screen()
window.title("Ping Pong")
window.setup(800,600)
window.bgcolor("black")


L_paddle = Paddle(-380)
R_paddle = Paddle(380)

window.listen()
window.onkeypress(L_paddle.move_up, "w")
window.onkeypress(L_paddle.move_down, "s")
window.onkeypress(R_paddle.move_up, "Up")
window.onkeypress(R_paddle.move_down, "Down")

ball = Ball()
score = Score()
while True:
    ball.moving(L_paddle, R_paddle, score)
    R_paddle.update()
    L_paddle.update()
    
    




window.exitonclick()