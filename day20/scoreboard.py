import turtle
from turtle import Turtle


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.screen_x , self.screen_y = turtle.screensize()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))
        self.goto(0, self.screen_y - 30)
        self.color("white")
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score += 1