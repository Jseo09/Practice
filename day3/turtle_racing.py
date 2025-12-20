from turtle import Turtle, Screen
import random


is_race_on = False

color = ["red","yellow", "green", "blue","purple"]
screen=Screen()
screen.setup(500,400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

def turtle_basic_setup(turtle,index):
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(color[index])


turtleA = Turtle()
turtle_basic_setup(turtleA,0)

turtleB = Turtle()
turtle_basic_setup(turtleB,1)

turtleC = Turtle()
turtle_basic_setup(turtleC,2)

turtleD = Turtle()
turtle_basic_setup(turtleD,3)

turtleE = Turtle()
turtle_basic_setup(turtleE,4)

turtle_lists = [turtleA, turtleB, turtleC, turtleD, turtleE]


if user_bet:
    is_race_on = True




turtleA.goto(-230, 100)
turtleB.goto(-230, 50)
turtleC.goto(-230, 0)
turtleD.goto(-230, -50)
turtleE.goto(-230, -100)

while is_race_on:
    for _ in turtle_lists:
        if _.xcor() > 230:
            if user_bet.lower() == _.color()[0]:
                print(f"You won the game! {_.color()[0]} won the race!")
            else:
                print(f"You lost the game! {_.color()[0]} won the race!")
            is_race_on = False
            break
        rand_distance = random.randint(0,10)
        _.forward(rand_distance)




