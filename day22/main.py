import time
from turtle import Screen
from ball import Ball
from day22.scoreboard import Scoreboard
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_and_reflection((r_paddle.xcor(), r_paddle.ycor()), (l_paddle.xcor(), l_paddle.ycor()))

    if ball.xcor() > 400:
        scoreboard.l_score_increase()
        ball.reset_position()
        print(f"r score : {scoreboard.l_score}")
    elif ball.xcor() < -400:
        scoreboard.r_score_increase()
        print(f"l score : {scoreboard.r_score}")
        ball.reset_position()




























screen.exitonclick()