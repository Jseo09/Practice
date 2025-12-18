print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want? S - Small, M - Medium, L - Large ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")
bill = 0 

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else: 
    print("Invalid size selected.")
    exit()

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1

print(f"Your final bill is: $" + str(bill))
