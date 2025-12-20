from turtle import Turtle, Screen
from score import ScoreBoard
import time
from snake import Snake
from food import Food


# Basic set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# Import here
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect if snake have touched the apple
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scored()
    if snake.head.xcor() > 300:
        print("Game Over")
        game_on = False
        score.game_over()
    if snake.head.xcor() < -300:
        print("Game Over")
        game_on = False
        score.game_over()
    if snake.head.ycor() > 300:
        print("Game Over")
        game_on = False
        score.game_over()
    if snake.head.ycor() < -300:
        print("Game Over")
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.game_over()

screen.exitonclick()
