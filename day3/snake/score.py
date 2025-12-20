from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.show()
    def show(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "bold"))

    def scored(self):
        self.score += 1
        self.show()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "bold"))
