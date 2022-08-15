from turtle import Turtle

MOVE = 30


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)


class Line(Paddle):
    def __init__(self, pos):
        super().__init__(pos)
        self.shapesize(stretch_wid=30, stretch_len=0.05)
        self.goto(pos)
