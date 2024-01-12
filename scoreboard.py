from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_a = 0
        self.score_b = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"{self.score_a}", align="center", font=("Courier", 30, "normal"))
        self.goto(100, 260)
        self.write(f"{self.score_b}", align="center", font=("Courier", 30, "normal"))

    def add_score_a(self):
        self.score_a += 1
        self.update_score()

    def add_score_b(self):
        self.score_b += 1
        self.update_score()
