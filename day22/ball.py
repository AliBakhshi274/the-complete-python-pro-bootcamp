from turtle import Turtle
import random

BALL_SPEED = 30

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setheading(random.randint(0, 360))

    def move_and_reflection(self, r_paddle: tuple, l_paddle: tuple):
        if self.is_wall_collision():
            self.setheading(360 - self.heading())
        elif self.is_paddle_collision(r_paddle, l_paddle):
            self.setheading(180 - self.heading())
        self.forward(BALL_SPEED)

    def is_paddle_collision(self, r_p: tuple, l_p: tuple):
        r_x, r_y = r_p
        l_x, l_y = l_p
        return (self.xcor() <= -320 and l_y - 50 < self.ycor() < l_y + 50) or (self.xcor() >= 320 and r_y - 50 < self.ycor() < r_y + 50)

    def is_wall_collision(self) -> bool:
        return self.ycor() > 280 or self.ycor() < -280

    def reset_position(self):
        self.goto(0,0)
        self.setheading(random.randint(0, 360))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    