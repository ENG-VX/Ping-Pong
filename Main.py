from turtle import Turtle,Screen
from paddle import Paddle

window = Screen()
window.title("Ping Pong")
window.setup(800,600)
window.bgcolor("black")


L_paddle = Paddle(-380)
R_paddle = Paddle(380)


window.onkey(lambda: L_paddle.move("up"), "w")
window.onkey(lambda: L_paddle.move("down"), "s")

window.listen()
window.exitonclick()