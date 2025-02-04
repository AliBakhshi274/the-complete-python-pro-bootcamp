from turtle import Turtle

from directions import Direction

MOVE_DISTANCE = 20
current_direction = Direction.RIGHT


def get_opposite_direction(direction):
    if direction == Direction.UP:
        return Direction.DOWN
    elif direction == Direction.DOWN:
        return Direction.UP
    elif direction == Direction.LEFT:
        return Direction.RIGHT
    elif direction == Direction.RIGHT:
        return Direction.LEFT


def change_direction(new_direction):
    global current_direction
    if new_direction != get_opposite_direction(current_direction):
        current_direction = new_direction


class Snake:

    def __init__(self):
        self.turtle_object_list = []
        self.snake_length = 0
        self.create_snake()
        self.head = self.turtle_object_list[0]

    def create_snake(self):
        for i in range(0, 3):
            self.snake_length += 1
            self.add_to_tail(self.snake_length)


    def add_to_tail(self, snake_length):
        self.snake_length += snake_length
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(snake_length * -20, 0)
        self.turtle_object_list.append(new_turtle)

    def move(self):
        for index in range(len(self.turtle_object_list) - 1, 0, -1):
            new_x = self.turtle_object_list[index - 1].xcor()
            new_y = self.turtle_object_list[index - 1].ycor()
            self.turtle_object_list[index].goto(new_x, new_y)
        self.turtle_object_list[0].forward(MOVE_DISTANCE)

    def move_up(self):
        change_direction(Direction.UP)
        if current_direction == Direction.UP:
            self.head.setheading(90)
    def move_down(self):
        change_direction(Direction.DOWN)
        if current_direction == Direction.DOWN:
            self.head.setheading(270)
    def move_left(self):
        change_direction(Direction.LEFT)
        if current_direction == Direction.LEFT:
            self.head.setheading(180)
    def move_right(self):
        change_direction(Direction.RIGHT)
        if current_direction == Direction.RIGHT:
            self.head.setheading(0)






















