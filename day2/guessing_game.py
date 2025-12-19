import os
import random 

keep_playing = True 
correct = False 


def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
def game_guessing(lives, answer, input):
    global correct
    if input > answer:
        print("Too high!")
        correct = False 
        lives -=1
    elif input < answer:
        print("Too low!")
        correct = False 
        lives -=1
    elif input == answer:
        print(f"correct! the answer was {answer}")
        correct = True 
    else:
        print("error occurred!")
    return lives, correct 

while keep_playing:
    answer =  random.randint(1,100)
    correct = False 
    print("Welcome to the Number guessing game! \n" \
    "I'm Thinking of a number between 1 and 100. ")
    print(f"Psst, the correct number is {answer}")
    difficulty_choice = input("choose a difficulty please. Type 'easy' or 'hard': ").lower()
    if difficulty_choice == 'easy':
        live = 10
    elif difficulty_choice == 'hard':
        live = 5
    else: 
        print("invalid input")
    
    while not correct and live > 0: 
        print(f"You have {live} amount of live left")
        input_guess = int(input("Make a guess!: "))
        live, correct = game_guessing(live, answer, input_guess)
    if not correct and live == 0: 
        print(f"You lost! The number was {answer}")
    continue_game = input("Do you want to keep playing the game? type 'y' for yes and 'n' for no : ")
    if continue_game == "y":
        clear_terminal()
        pass
    else:
        keep_playing = False
        print("Thank you for playing game with us. Bye for now!")    



    



    


