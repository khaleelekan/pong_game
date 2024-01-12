from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
score = Scoreboard()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

# bounce on wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# bounce on paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# if ball is out of bounds
    if ball.xcor() > 380:
        ball.reset_ball()
        score.add_score_a()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.add_score_b()
screen.exitonclick()
