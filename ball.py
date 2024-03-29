from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.xc = 10
        self.yc = 10
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.xc
        new_ycor = self.ycor() + self.yc
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.yc *= -1
        self.move_speed *= 0.5

    def bounce_x(self):
        self.xc *= -1
        self.move_speed *= 0.5

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.xc *= -1

