from turtle import Turtle
SPEED = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset()
    def reset(self):
        self.setheading(90)
        self.hideturtle()
        self.goto(0,-250)
        self.speed("fastest")
        self.showturtle()
    def up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor() , new_y)


