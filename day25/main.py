from turtle import Screen, Turtle
import pandas, os.path

current_guess_number = 0
data = pandas.read_csv("50_states.csv")
list_of_states = data.state.tolist()

screen = Screen()
screen.tracer(0)
screen.setup(width=725, height=500)
screen.bgpic("blank_states_img.gif")
screen.title("Name the States")

turtle = Turtle()
turtle.penup()
turtle.hideturtle()

guessed_states = []

is_game_running = True
while is_game_running:
    user_guess_textinput = screen.textinput(title=f"{current_guess_number}/{len(data)} States Correct", prompt="What's another state name?")

    if user_guess_textinput == "Exit":
        break
    elif user_guess_textinput in list_of_states:
        current_guess_number += 1
        state_row = data[data.state == user_guess_textinput]
        guessed_states.append(state_row)
        x = int(state_row.iloc[0].x)
        y = int(state_row.iloc[0].y)
        turtle.goto(x, y)
        turtle.write(state_row.iloc[0].state, align="center", font=("Arial", 10, "normal"))

    if user_guess_textinput == len(data):
        is_game_running = False

    screen.update()

state_col = []
x_col = []
y_col = []
for row in guessed_states:
    state_col.append(row.state.item())
    x_col.append(row.x.item())
    y_col.append(row.y.item())

data_to_dict = {'state': state_col, 'x': x_col, 'y': y_col}
pandas.DataFrame(data_to_dict).to_csv("learned_states.csv")




















