import random 
ai_choice = ["rock", "paper", "scissors"]
Running = True 
while Running:
    print("Welcome to rock paper scissors game!")
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        Running = False
        print("Thanks for playing!")
    elif user_input not in ai_choice:
        print("Invalid input, please try again.")
    elif user_input in ai_choice:
        ai_input = ai_choice[random.randint(0,2)]
        print(f"AI chose: {ai_input}")
        if user_input == ai_input:
            print("It's a tie!")
        elif (user_input == "rock" and ai_input == "scissors") or \
             (user_input == "paper" and ai_input == "rock") or \
             (user_input == "scissors" and ai_input == "paper"):
            print("You win!")
        else:
            print("AI wins!")

