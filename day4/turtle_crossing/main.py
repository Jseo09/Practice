from turtle import Screen, colormode
from character import Player
from car import Car
import time
import random
from score import Score

screen = Screen()
colormode(255)
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

player = Player()
score = Score()
cars = Car()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.03)
    spawn_chance = 0.05 + score.score * 0.01
    spawn_chance = min(spawn_chance, 0.3)

    if random.random() < spawn_chance:
        cars.draw()

    cars.move(score.score+2)
    cars.cleanup_offscreen()

    if player.ycor() > 280:
        score.score_add()
        player.reset()
        cars.cleanup_onscreen()

    if player.ycor() < -280:
        player.goto(player.xcor(), -280)

    for c in cars.cars:
        if player.distance(c) < 20:
            score.game_over()
            game_is_on = False
            break

    screen.update()

screen.exitonclick()
