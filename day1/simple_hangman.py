import random
lives = 6

print("Welcome to the hangman!")
print('''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"        ''')

word = ["apple","bridge","candle","forest","planet","river","castle","shadow","mirror","ladder",
        "running","jumping","whisper","shouting","climbing","drawing","thinking","reading","writing","flying"]

correct = False
live = 6

word_to_guess = random.choice(word)
print(word_to_guess)
word_place_holder = []
for i in range(len(word_to_guess)):
    word_place_holder.append("_")
alphabet_guessed = []

while live > 0:
    print(f"Your left over lives: {live}")
    correct = False
    word_place_hold = "" 
    for word in word_place_holder:
        word_place_hold += word
    print(word_place_hold)
    user_guess = input("Please guess the alphabet!")
    if len(user_guess) > 1:
        print("Invalid length of the alphabet. Please retry")
    else:
        index = 0
        for i in word_to_guess:
            if user_guess == i:
                word_place_holder[index] = user_guess
                correct = True
            index+=1
        if correct == True: 
            print(" you have guessed this correct! moving onto next")
        else:
            live-=1
            print("you got it wrong! one live removed")
    if live == 0:
        print(f"you lost the game, the word was {word_to_guess}")

    if "-" in word_to_guess:
        print(f"You have won the game! The word was {word_to_guess}")
        exit
    else:
        pass
        
    
