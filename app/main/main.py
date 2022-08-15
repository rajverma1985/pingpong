from app.paddle.paddle import Paddle, Line
from app.ball.ball import Ball
from turtle import Screen
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# create paddle
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
line = Line((0, 0))
ball = Ball()

# move the paddles
screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    # detect wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect paddle collisions
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()
