from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position: tuple[int, int]):
        super().__init__()
        x, y = position
        self.create_paddle(x)

    def create_paddle(self, x):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, 0)

    def go_up(self):
        x = self.xcor()
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(x, new_y)
    def go_down(self):
        x = self.xcor()
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(x, new_y)

