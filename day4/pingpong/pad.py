from turtle import Turtle

PLAYER_SPEED = 20
class Pad(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.create(x,y)

    def create(self, x, y):
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.goto(x, y)
        self.shape("square")
        self.turtlesize(5,1)
        self.showturtle()


    def up(self):
        new_y = self.ycor() + PLAYER_SPEED
        if new_y >= 270:
            pass
        else:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - PLAYER_SPEED
        if new_y < -250:
            pass
        else:
            self.goto(self.xcor(), new_y)












