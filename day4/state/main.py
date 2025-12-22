import turtle, pandas as pd
import time
import states

screen = turtle.Screen()
screen.title("U.S. State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


# Basic set up
states_name = []
database = pd.read_csv("50_states.csv")
for x in database["state"]:
    states_name.append(x)


state = states.State()
states_lower = [states.lower() for states in states_name]
guessed = set()

game_is_on = True
while game_is_on:
    user_input = screen.textinput(title=f"Guess the state", prompt="Enter a state: ")
    if user_input is None:
        break
    user_input = user_input.strip().lower()

    if user_input in states_lower:
        answer = user_input.title()
        if answer in guessed:
            continue
        guessed.add(answer)
        row = database[database["state"] == answer]
        x = (row['x'].values[0])
        y = (row['y'].values[0])
        state.create_another_state(answer,x, y)
    else:
        state.game_over(len(guessed), len(states_lower))
        for state_name in states_lower:
            if state_name not in guessed:
                row = database[database['state'] == state_name.title()]
                x = int(row['x'].values[0])
                y = int(row['y'].values[0])
                state.show_answers(state_name.title(),x,y)
        with open("Result.txt", 'w') as result_files:
            result_files.write(f"Result: {len(guessed)}/{len(states_lower)}")
            result_files.write(f"*************************************")
            result_files.write(f"*************************************")
            result_files.write("\nYou got: " )
            for _ in guessed:
                result_files.write(f"{_.title()}\n")
            result_files.write("\nRight. \nAnd you got:")
            result_files.write(f"*************************************")
            result_files.write(f"*************************************")
            for _ in states_lower:
                if _ not in guessed:
                    result_files.write(f"\n{_.title()}\n")
            result_files.write("\nWrong.")
            result_files.close()
        game_is_on = False

    screen.update()


screen.exitonclick()
