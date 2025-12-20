from turtle import Turtle, Screen
import random

random_colors = ["seashell","tomato","yellow green","navajo white","steel blue",
                 "medium turquoise","aquamarine", "orchid", "pale violet red"]
tim = Turtle()
tim.shape("circle")
tim.color("DarkSeaGreen")

def draw_shape(sides):
    degree = 360/sides
    tim.color(random.choice(random_colors))
    for _ in range(sides):

        tim.forward(100)
        tim.right(degree)


for _ in range(3,10):
    draw_shape(_)


















screen = Screen()
screen.exitonclick()
