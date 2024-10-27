from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

window = Screen()
window.title("Ping Pong")
window.setup(800, 600)
window.bgcolor("black")
window.tracer(0)  # تعطيل التحديث التلقائي لتسريع الأداء

L_paddle = Paddle(-380)
R_paddle = Paddle(380)

window.listen()
window.onkeypress(L_paddle.move_up, "w")
window.onkeypress(L_paddle.move_down, "s")
window.onkeyrelease(L_paddle.stop, "w")
window.onkeyrelease(L_paddle.stop, "s")
window.onkeypress(R_paddle.move_up, "Up")
window.onkeypress(R_paddle.move_down, "Down")
window.onkeyrelease(R_paddle.stop, "Up")
window.onkeyrelease(R_paddle.stop, "Down")

ball = Ball()
score = Score()

def update_game():
    ball.moving(L_paddle, R_paddle, score)
    R_paddle.update()
    L_paddle.update()
    window.update()  # تحديث الشاشة
    window.ontimer(update_game, 10)  # تحديث اللعبة كل 10 ملي ثانية

update_game()  # بدء اللعبة
window.exitonclick()
