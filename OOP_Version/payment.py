import time
from menu import Menu

menu = Menu()


class Payment:

    def make_payment(self, coffee_type, amount, coffee_brewer):
        coffee_type = menu.get_item_by_name(coffee_type)
        print("Please make payment!")
        user_money = int(input("Your money: "))
        if user_money < coffee_type.cost * amount:
            print(f"Sorry, your money is not enough!\n")
        else:
            coffee_brewer.update_report(coffee_type.name.lower(), amount)
            print(f"Your {coffee_type.name} is being made...")
            time.sleep(2)
            print(f"Here is your change: {user_money-coffee_type.cost*amount} IDR")
            print(f"Your {coffee_type.name} is ready☕, enjoy!\n")
