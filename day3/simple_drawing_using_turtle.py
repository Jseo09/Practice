from turtle import Turtle, Screen, colormode
import random
colormode(255)
color_list = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59), (172, 204, 182), (108, 46, 38), (158, 204, 215), (76, 69, 37), (9, 87, 109)]
degree = [0, 90, 270]


tim = Turtle()
tim.speed("fastest")
tim.penup()
number_of_dots = 101
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
tim.hideturtle()
screen = Screen()
screen.exitonclick()
