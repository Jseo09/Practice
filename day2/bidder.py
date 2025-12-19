
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

        # Command for Linux/macOS/POSIX
# print('''XXXXXXXXXXXXXXXXXXFEDERAL RESERVE NOTEXXXXXXXXXXXXXXXXXXX
# XXX  XX       THE UNITED STATES OF AMERICA        XXX  XX
# XXXX XX  -------       ------------               XXXX XX
# XXXX XX              /   jJ===-\    \      C7675  XXXX XX
# XXXXXX     OOO      /   jJ - -  L    \      ---    XXXXXX
# XXXXX     OOOOO     |   JJ  |   X    |       __     XXXXX
# XXX    3   OOO      |   JJ ---  X    |      OOOO    3 XXX
# XXX                 |   J|\    /|    |     OOOOOO     XXX
# XXX     C36799887   |   /  |  |  \   |      OOOO      XXX
# XXX                 |  |          |  |       --       XXX
# XXX      -------    \ /            \ /                XXX
# X  XX                \ ____________ /               X  XX
# XX XXX 3_________        --------  ___   _______ 3 XXX XX
# XX XXX            ___   ONE DOLLAR  i              XXX XX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX''')

bid_informations = {}
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = int(bidding_dictionary[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while True: 
    clear_screen()
    name = input("What is your name? : ")
    bid_amount = input("What's your bid? : ")
    answer = input("Are there any other bidders? Type 'yes' or 'no'")
    bid_informations[name] = bid_amount
    if answer == "yes":
        pass
    else:
        find_highest_bidder(bid_informations)
        break
        
