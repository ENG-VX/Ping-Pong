from turtle import Turtle,Screen
from paddle import Paddle

window = Screen()
window.title("Ping Pong")
window.setup(800,600)
window.bgcolor("black")


L_paddle = Paddle(-380)
R_paddle = Paddle(380)


window.onkey(L_paddle.move_up, "w")
window.onkey(L_paddle.move_down, "s")
window.onkey(R_paddle.move_up, "Up")
window.onkey(R_paddle.move_down, "Down")

window.listen()
window.exitonclick()