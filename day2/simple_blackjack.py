
import random as rd
# Basic Variables
beginning_set = True 

deck = {
    "Ace": {
        "scores": [1, 11],
        "amount": 4
        },
    "2": {
        "scores": 2,
        "amount": 4
    },
    "3": {
        "scores": 3,
        "amount": 4
    },
    "4": {
        "scores": 4,
        "amount": 4
    },
    "5":{
        "scores": 5,
        "amount": 4
    },
    "6":{
        "scores": 6,
        "amount": 4
    },
    "7":{
        "scores": 7,
        "amount": 4
    },
    "8":{
        "scores": 8,
        "amount": 4
    },
    "9":{
        "scores": 9,
        "amount": 4
    },
    "10":{
        "scores": 10,
        "amount": 4
    },
    "Jack":{
        "scores": 10,
        "amount": 4
    },
    "Queen":{
        "scores": 10,
        "amount": 4
    },
    "King":{
        "scores": 10,
        "amount": 4
    }
}

def reset_deck(deck):
    for i in deck: 
        deck[i]["amount"] = 4
def pick_a_card(deck):
    decision_needed = True 
    card = rd.choice(list(deck.keys()))
    while deck[card]["amount"] == 0: 
        card = rd.choice(list(deck.keys()))
    deck[card]["amount"] -=1

    if card == "Ace":
        while decision_needed:
            score_selection = input("You have selected Ace. Please select whether you would like to have 1 or 11 for score \n Type '1' for 1 and '11' for 11: ")
            if score_selection == "1":
                score = 1
                decision_needed = False 
            elif score_selection == "11": 
                score = 11
                decision_needed = False 
            else:
                print("invalid decision made")
    else: 
        score = deck[card]["scores"]
    return score, card
def computer_pick_a_card(deck, ai_score):
    card = rd.choice(list(deck.keys()))
    while deck[card]["amount"] == 0: 
        card = rd.choice(list(deck.keys()))
    deck[card]["amount"] -=1
    if card == "Ace":
        if ai_score + 11 <=  21:
            score = 11
        else:
            score = 1
    else: 
        score = deck[card]["scores"]
    return score, card
def calculate_who_won(score, ai_score, ai_card_deck, user_card_deck):
    print(f"Your card deck: {user_card_deck}")
    print(f"Ai's card deck: {ai_card_deck}")
    print(f"Your score is : {score}")
    print(f"Ai's score is {ai_score}")
    
    if score > 21 and ai_score > 21:
        print("Tied")
    elif score == ai_score:
        print("Tied")
    elif score > 21 and ai_score < 21:
        print("You went over the 21. You have lost")
    elif score < 21 and ai_score > 21:
        print("You have won the game!")
    else: 
        score = 21 - score 
        ai_score = 21 - ai_score 
        if score > ai_score:
            print("You have lost the game!")
        
        else:
            print("you have won the game!")
    
    return True



while True: 
    answer = input("Hello do you want to play black jack? please type 'y' for yes and 'n' for no: \n ").lower() 
    if answer == "y":
        user_score = 0
        ai_score = 0 
        ai_card_deck = []
        user_card_deck = []
        beginning_set = True 
        pass 
    elif answer == "n":
        break
    else:
        print("invalid answer. quitting the program!")
        break
    while user_score < 21 and ai_score < 21:    
        if beginning_set: 
            
            
            for i in range(0,2):
                score, card = pick_a_card(deck)
                user_score += score 
                user_card_deck.append(card)
                print(f"You have drawed: {card}")
                score, card = computer_pick_a_card(deck,ai_score)
                ai_score +=score
                ai_card_deck.append(card)
            beginning_set = False
            print(f"Your cards: {user_card_deck}")
            print(f"computer's first card: {ai_card_deck[0]}")
        draw_decision = input("Do you want to draw another card? Please type 'y' for yes and 'n' for no : \n")
        if draw_decision == "y":
                score, card = pick_a_card(deck)
                user_score += score 
                user_card_deck.append(card)
                print(f"You have drawed: {card}")
                score, card = computer_pick_a_card(deck,ai_score)
                ai_score +=score
                ai_card_deck.append(card)
        elif draw_decision == "n":
            beginning_set = calculate_who_won(user_score, ai_score, ai_card_deck, user_card_deck)
            reset_deck(deck)
            break
    if user_score >= 21 or ai_score >= 21: 
        beginning_set = calculate_who_won(user_score, ai_score, ai_card_deck, user_card_deck)
        reset_deck(deck)
  

        
