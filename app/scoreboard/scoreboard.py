from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_player = 0
        self.l_player = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 240)
        self.write(self.l_player, align="center", font=("Courier", 40, "bold"))
        self.goto(50, 240)
        self.write(self.r_player, align="center", font=("Courier", 40, "bold"))

    def l_point(self):
        self.l_player += 1
        self.update_score()

    def r_point(self):
        self.r_player += 1
        self.update_score()
