from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y ):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.showturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score}", move= True, font=("Arial", 24, "normal"))
        self.hideturtle()
    def increase_score(self):
        self.score += 1
        self.update()


