import data

def print_report(dataset):
    print(f"Water : {dataset.resources.get('water')} ml")
    print(f"Milk : {dataset.resources.get('milk')} ml")
    print(f"Coffee : {dataset.resources.get('coffee')} g")
    print(f"Money : ${dataset.resources.get('money', 0):.2f}")

def money_calculation(quarter_input, dime_input, nick_input, pen_input):
    quarter = int(quarter_input) * 0.25
    dime = int(dime_input) * 0.10
    nick = int(nick_input) * 0.05
    pen = int(pen_input) * 0.01
    return quarter + dime + nick + pen

def check_resources_available(water_required, coffee_required, milk_required, dataset):
    water_available = dataset.resources.get("water", 0)
    milk_available = dataset.resources.get("milk", 0)
    coffee_available = dataset.resources.get("coffee", 0)

    if water_available < water_required:
        print("Sorry there is not enough water.")
        return False
    if milk_available < milk_required:
        print("Sorry there is not enough milk.")
        return False
    if coffee_available < coffee_required:
        print("Sorry there is not enough coffee.")
        return False

    return True

def deduct_resources(water_required, coffee_required, milk_required):
    data.resources["water"] -= water_required
    data.resources["milk"] -= milk_required
    data.resources["coffee"] -= coffee_required

def handle_drink(drink_name, money):
    drink = data.MENU[drink_name]
    ingredients = drink["ingredients"]
    cost = drink["cost"]

    water_required = ingredients.get("water", 0)
    milk_required = ingredients.get("milk", 0)
    coffee_required = ingredients.get("coffee", 0)

    # check resources first (spec order)
    if not check_resources_available(water_required, coffee_required, milk_required, data):
        return

    # then check money
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return

    # success: update profit + deduct resources
    data.resources["money"] = data.resources.get("money", 0) + cost
    deduct_resources(water_required, coffee_required, milk_required)

    change = money - cost
    if change > 0:
        print(f"Here is ${change:.2f} dollars in change.")
    print(f"Here is your {drink_name}! Enjoy!")

print_report(data)

while True:
    user_input = input("What would you like to drink? (espresso/latte/cappuccino) : ")
    if user_input == "off":
        break
    elif user_input == "report":
        print_report(data)
    elif user_input in ["espresso", "latte", "cappuccino"]:
        quarter_input = input("Please insert coins. \n How many quarters?: ")
        dime_input = input("How many dimes?: ")
        nick_input = input("How many nickles?: ")
        pen_input = input("How many pennies?: ")
        input_money = money_calculation(quarter_input, dime_input, nick_input, pen_input)
        handle_drink(user_input, input_money)
    else:
        print("Invalid input. Please try again.")
