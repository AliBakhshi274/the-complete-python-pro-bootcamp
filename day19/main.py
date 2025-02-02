import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(random.choice(colors))
    colors.remove(new_turtle.fillcolor())
    new_turtle.penup()
    new_turtle.goto(x=10 - screen.window_width() / 2, y=turtle_index * 50 - screen.window_height() / 3)
    all_turtles.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > screen.window_width() / 2:
            winning_color = turtle.fillcolor()
            is_race_on = False
            print(f"The winner is {winning_color}")
            if winning_color == user_bet:
                print("You win!")
            else:
                print("You lose!")
        turtle.forward(random.randint(1, 10))



screen.exitonclick()
