
import art, random, game_data, os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

score = 0

while True:
    clear_terminal()
    print(art.logo)
    a = random.randint(0, len(game_data.data)-1)
    b = random.randint(0, len(game_data.data)-1)
    while a == b:
        b = random.randint(0, len(game_data.data)-1)
    print(f"Compare A: {game_data.data[a]['name']} a {game_data.data[a]['description']}, from {game_data.data[a]['country']}\n\n")
    print(art.vs)
    print(f"Against B: {game_data.data[b]['name']} a {game_data.data[b]['description']}, from {game_data.data[b]['country']}\n")
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input == 'a':
        if game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            clear_terminal()
            print(art.logo)
            print(f"Sorry you are wrong. Final score : {score}")
            running = False
            break
    elif user_input == 'b':
        if game_data.data[b]['follower_count'] > game_data.data[a]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            clear_terminal()
            print(f"Sorry you are wrong. Final score : {score}")
            break
    else:
        print("Please type 'A' or 'B'.")
