# import colorgram
#
# colors = colorgram.extract('image.jpeg', 20)
#
# extractedColors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     extractedColors.append((r,g,b))
# print(extractedColors)
import random
import turtle
from random import Random
from turtle import Screen

t = turtle.Turtle()

# Constant variables
PEN_SIZE = 20
FORWARD_DISTANCE = 50
START_POINT_X = -200

color_list = [(18, 247, 240), (239, 250, 5), (251, 241, 247), (6, 243, 250), (235, 45, 87), (210, 161, 109),
              (113, 177, 212), (201, 5, 68), (12, 52, 128), (196, 77, 19), (65, 133, 177), (193, 164, 15)]

def normalize_color_list(list_of_colors) -> list:
    new_color_list = []
    for color in list_of_colors:
        r = color[0]/255
        g = color[1]/255
        b = color[2]/255
        new_color_list.append((r, g, b))
    return new_color_list

def start_point(lineup):
    t.penup()
    t.setpos(START_POINT_X, lineup)
    t.pendown()

def push_forward():
    for step in range(10):
        t.dot(PEN_SIZE, random.choice(color_list))
        t.penup()
        t.forward(FORWARD_DISTANCE)
        t.pendown()

color_list = normalize_color_list(color_list)
t.speed(5)

for line in range(0, 600, 40):
    start_point(line)
    push_forward()



















this_screen = Screen()
this_screen.exitonclick()