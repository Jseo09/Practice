import turtle

class State(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.states = []

    def create_another_state(self, state,x,y):
        new_state = turtle.Turtle()
        new_state.penup()
        new_state.color("black")
        new_state.speed("fastest")
        new_state.hideturtle()
        new_state.goto(x, y)
        new_state.write(state, align="center", font=("Courier", 10, "normal"))

        self.states.append(new_state)
    def game_over(self, correct, wrong ):
        game_over = turtle.Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(0,0)
        game_over.write(f"Game Over.\n Your score: {correct}/{wrong}", align="center", font=("Courier", 20, "bold"))
    def show_answers(self, state,x,y):
        answer_states = turtle.Turtle()
        answer_states.penup()
        answer_states.color("red")
        answer_states.speed("fastest")

        answer_states.hideturtle()
        answer_states.goto(x, y)
        answer_states.write(state, align="center", font=("Courier", 10, "normal"))


    #
    # def location(self,x,y,input):
    #
    #     self.speed("fastest")
    #     self.write()
    #
    #     self.goto(x,y)
