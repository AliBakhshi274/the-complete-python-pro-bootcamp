import random
from turtle import Turtle

COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0

    def create_car(self):
        if random.randint(0, 10) == 0:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(310, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.car_speed)



    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT