from turtle import Turtle

FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color("black")
        self.penup()
        self.goto(-250, 270)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0 , 0)
        self.write("GAME OVER", align="center", font=FONT)




