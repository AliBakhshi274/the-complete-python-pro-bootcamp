import time
from turtle import Screen

from day23.scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.create_scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


is_game_running = True
while is_game_running:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_car()
    if player.reached_to_top():
        car_manager.increase_speed()
        scoreboard.update_scoreboard()

    # Detect collision with cas
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_running = False
            scoreboard.game_over()





















screen.exitonclick()