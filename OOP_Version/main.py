import time
from menu import Menu
from coffee_brewer import CoffeeBrewer

menu = Menu()
coffee_brewer = CoffeeBrewer()

print("COFFEE MACHINE PROGRAM")
run_program = True
while run_program:
    user_input = input(
        f"what kind of coffee do you want? espresso/latte/cappuccino: "
    ).lower()
    if user_input == "report":
        coffee_brewer.report()
    elif user_input == "off":
        print("Cleaning system...")
        time.sleep(2)
        print("Coffee machine turned off. Goodbye!")
        run_program = False
    elif user_input == "espresso":
        user_amount = int(input(f"How many {user_input}?: "))
        coffee_brewer.espresso_check(user_amount)
    elif user_input == "latte":
        user_amount = int(input(f"How many {user_input}?: "))
        coffee_brewer.latte_check(user_amount)
    elif user_input == "cappuccino":
        user_amount = int(input(f"How many {user_input}?: "))
        coffee_brewer.cappuccino_check(user_amount)
    else:
        print("Sorry, that item is not available!")
