from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(1, 1)
        self.color("black")
        self.setheading(90)
        self.starting_point()

    def starting_point(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reached_to_top(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.starting_point()
            return True
        return False





















