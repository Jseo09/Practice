from turtle import Turtle
import random

class Car:
    def __init__(self):
        self.cars = []

    def move(self, stage):
        new_speed = int(stage / 2) + 2
        for c in self.cars:
            c.goto(c.xcor() - new_speed, c.ycor())

    def draw(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(0.5, 1.5)
        new_car.color(self.randomcolor())
        new_car.goto(300, random.randint(-260, 260))
        self.cars.append(new_car)

    def cleanup_offscreen(self):
        for c in self.cars[:]:
            if c.xcor() < -320:
                c.hideturtle()
                self.cars.remove(c)

    def cleanup_onscreen(self):
        for c in self.cars[:]:
            c.hideturtle()
            self.cars.remove(c)

    def randomcolor(self):
        return (
            random.randint(0, 200),
            random.randint(0, 200),
            random.randint(0, 200),
        )
