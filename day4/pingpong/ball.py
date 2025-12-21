from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = -10
        self.x_move = -10

    def reset(self):
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,0)
        self.showturtle()
    def move(self):
        self.bounce()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce(self):
        if self.ycor() > 290:
            self.y_move = -self.y_move
        elif self.ycor() < -290:
            self.y_move = -self.y_move
    def collide(self):
        self.y_move = -self.y_move
        self.x_move = -self.x_move

