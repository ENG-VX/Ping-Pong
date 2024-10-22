from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball

window = Screen()
window.title("Ping Pong")
window.setup(800,600)
window.bgcolor("black")


L_paddle = Paddle(-380)
R_paddle = Paddle(380)

window.listen()
window.onkey(L_paddle.move_up, "w")
window.onkey(L_paddle.move_down, "s")
window.onkey(R_paddle.move_up, "Up")
window.onkey(R_paddle.move_down, "Down")

ball = Ball()
ball.moving()

window.exitonclick()