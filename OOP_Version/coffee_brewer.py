from prettytable import PrettyTable
from menu import Menu
from payment import Payment

menu = Menu()
payment = Payment()


class CoffeeBrewer:
    def __init__(self):
        self.resources = {"water": 100000, "coffee": 100000, "milk": 100000, "money": 0}

    def get_resources(self):
        return self.resources

    def report(self):
        resources_table = PrettyTable(["Ingredients", "Amount"])
        resources_table.add_row(["Water", self.resources["water"]])
        resources_table.add_row(["Coffee", self.resources["coffee"]])
        resources_table.add_row(["Milk", self.resources["milk"]])
        resources_table.align = "l"
        money_table = PrettyTable()
        money_table.add_column("Money", [self.resources["money"]])
        print(resources_table)
        print(money_table)

    def update_report(self, coffee_type, amount):
        recipes = {
            "espresso": {"water": 50, "coffee": 18, "milk": 0, "cost": 15000},
            "latte": {"water": 200, "coffee": 24, "milk": 150, "cost": 25000},
            "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "cost": 35000},
        }
        recipe = recipes[coffee_type]

        for item in ["water", "coffee", "milk"]:
            self.resources[item] -= recipe[item] * amount

        self.resources["money"] += recipe["cost"] * amount

    def espresso_check(self, amount):
        espresso = menu.get_item_by_name("Espresso")
        if (
            self.resources["water"] < espresso.ingredients["water"] * amount
            or self.resources["coffee"] < espresso.ingredients["coffee"] * amount
        ):
            print(f"Sorry, there is not enough water and coffee!\n")
        elif self.resources["water"] < espresso.ingredients["water"] * amount:
            print(f"Sorry, there is not enough water!\n")
        elif self.resources["coffee"] < espresso.ingredients["coffee"] * amount:
            print(f"Sorry, there is not enough coffee!\n")
        else:
            espresso = menu.get_item_by_name("Espresso")
            print("\n~~~~~~~~YOUR ORDER~~~~~~~~")
            print(f"Espresso cost: {espresso.cost} IDR")
            print(f"{amount} Espresso: {espresso.cost*amount} IDR")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            payment.make_payment(espresso.name, amount, self)

    def latte_check(self, amount):
        latte = menu.get_item_by_name("Latte")
        if (
            self.resources["water"] < latte.ingredients["water"] * amount
            or self.resources["coffee"] < latte.ingredients["coffee"] * amount
        ):
            print(f"Sorry, there is not enough water and coffee!\n")
        elif self.resources["water"] < latte.ingredients["water"] * amount:
            print(f"Sorry, there is not enough water!\n")
        elif self.resources["coffee"] < latte.ingredients["coffee"] * amount:
            print(f"Sorry, there is not enough coffee!\n")
        else:
            latte = menu.get_item_by_name("Latte")
            print("\n~~~~~~~~YOUR ORDER~~~~~~~~")
            print(f"Latte cost: {latte.cost} IDR")
            print(f"{amount} Latte: {latte.cost*amount} IDR")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            payment.make_payment(latte.name, amount, self)

    def cappuccino_check(self, amount):
        cappuccino = menu.get_item_by_name("Cappuccino")
        if (
            self.resources["water"] < cappuccino.ingredients["water"] * amount
            or self.resources["coffee"] < cappuccino.ingredients["coffee"] * amount
        ):
            print(f"Sorry, there is not enough water and coffee!\n")
        elif self.resources["water"] < cappuccino.ingredients["water"] * amount:
            print(f"Sorry, there is not enough water!\n")
        elif self.resources["coffee"] < cappuccino.ingredients["coffee"] * amount:
            print(f"Sorry, there is not enough coffee!\n")
        else:
            cappuccino = menu.get_item_by_name("Cappuccino")
            print("\n~~~~~~~~YOUR ORDER~~~~~~~~")
            print(f"Cappuccino cost: {cappuccino.cost} IDR")
            print(f"{amount} Cappuccino: {cappuccino.cost*amount} IDR")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            payment.make_payment(cappuccino.name, amount, self)
