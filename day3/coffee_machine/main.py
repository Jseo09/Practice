from menu import Menu, MenuItem
from coffee_machine import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

while True:
    user_input = input("What would you like to drink? (espresso/ latte/ cappuccino) : ")
    if user_input == "off":
        break
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        # if drink.name in menu.get_items() == drink:
        #     if coffee_machine.is_resource_sufficient(drink):
        #         if money_machine.make_payment(drink.cost):
        #             coffee_machine.make_coffee(drink.name)
        #         else:
        #             print("Sorry, that's not enough money.")
        if user_input == "espresso":
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
                else:
                    print("Sorry that's not enough money. Money refunded")
        elif user_input == "latte":
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
                else:
                    print("Sorry that's not enough money. Money refunded")
        elif user_input == "cappuccino":
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
                else:
                    print("Sorry that's not enough money. Money refunded")
        else:
            print("invalid input. Please try again")

