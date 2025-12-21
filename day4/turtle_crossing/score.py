from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"{self.score}", align= "center", font=("Courier", 18, "normal"))
    def score_add(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over. Final Stage : {self.score}", align= "center", font=("Courier", 18, "normal"))

