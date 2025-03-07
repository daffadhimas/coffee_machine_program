class MenuItems:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "coffee": coffee, "milk": milk}


class Menu:
    def __init__(self):
        self.menu = [
            MenuItems(name="Espresso", cost=15000, water=50, coffee=18, milk=0),
            MenuItems(name="Latte", cost=25000, water=200, coffee=24, milk=15),
            MenuItems(name="Cappuccino", cost=35000, water=250, coffee=24, milk=100),
        ]

    def get_item_by_name(self, name):
        for item in self.menu:
            if item.name.lower() == name.lower():
                return item
        return None
