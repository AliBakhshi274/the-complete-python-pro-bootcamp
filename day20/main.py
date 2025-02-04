import time
from turtle import Screen

from scoreboard import Scoreboard
from day20.food import Food
from snake import Snake
from directions import Direction

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.move_up, Direction.UP.value)
screen.onkey(snake.move_down, Direction.DOWN.value)
screen.onkey(snake.move_left, Direction.LEFT.value)
screen.onkey(snake.move_right, Direction.RIGHT.value)

food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food.xcor(), food.ycor()) < 15:
        scoreboard.increase_score()
        scoreboard.display_score()
        snake.add_to_tail(snake.snake_length + 1)
        food.refresh()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for t in snake.turtle_object_list[1::1]:
        if snake.head.distance(t) < 10:
            game_is_on = False
            scoreboard.game_over()


















screen.exitonclick()
