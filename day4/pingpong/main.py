from turtle import Turtle, Screen
from pad import Pad
from ball import Ball
import time
from score import Score

# Basic Set up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong game")
screen.listen()

pad1 = Pad(350,0)
pad2 = Pad(-350,0)

screen.onkeypress(pad1.up, "Up")
screen.onkeypress(pad1.down, "Down")
screen.onkeypress(pad2.up, "w")
screen.onkeypress(pad2.down, "s")

ball = Ball()
score1 = Score(100, 200)
score2 = Score(-100, 200)

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    if ball.distance(pad1) < 30:
        ball.collide()
    if ball.distance(pad2) < 30:
        ball.collide()
    if ball.xcor() > 500:
        ball.reset()
        score2.increase_score()
    if ball.xcor() < -500:
        ball.reset()
        score1.increase_score()

















screen.exitonclick()

