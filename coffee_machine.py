from program_data import menu, resources
import time


# Memanggil bahan baku yang tersedia di program mesin kopi
def report():
    return {
        "water": resources["water"],
        "milk": resources["milk"],
        "coffee": resources["coffee"],
        "money": resources["money"],
    }


# Memanggil bahan baku tiap kopi
def menu_ingredient():
    return {
        "espresso": menu["espresso"]["ingredients"],
        "latte": menu["latte"]["ingredients"],
        "cappuccino": menu["cappuccino"]["ingredients"],
    }


# Memanggil harga tiap kopi
def cost():
    return {
        "espresso_cost": menu["espresso"]["cost"],
        "latte_cost": menu["latte"]["cost"],
        "cappuccino_cost": menu["cappuccino"]["cost"],
    }


# Update report setelah program membuat kopi dan melakukan pembayaran
def update_report(water, coffee, milk, money, amount):
    report_resources["water"] -= water * amount
    report_resources["coffee"] -= coffee * amount
    report_resources["milk"] -= milk * amount
    report_resources["money"] += money * amount


# Proses pembayaran
def payment(coffee_type, coffe_type_cost, amount):
    print("Please make payment!")
    user_money = int(input("Your money: "))
    if user_money < coffe_type_cost * amount:
        print(f"Sorry, your money is not enough!\n")
    else:
        update_report(
            menu_resources[coffee_type]["water"],
            menu_resources[coffee_type]["coffee"],
            menu_resources[coffee_type]["milk"],
            coffe_type_cost,
            amount,
        )
        print(f"Your {coffee_type} is being made...")
        time.sleep(2)
        print(f"Here is your change: Rp{user_money-coffe_type_cost*amount}")
        print(f"Your {coffee_type} is ready☕, enjoy!\n")


# Cek bahan baku espresso
def espresso_check(esp_water, esp_coffee, esp_ing_water, esp_ing_coffee, amount):
    if esp_water < esp_ing_water * amount or esp_coffee < esp_ing_coffee * amount:
        if esp_water < esp_ing_water * amount and esp_coffee < esp_ing_coffee * amount:
            print(f"Sorry, there is not enough water and coffee!\n")
        elif esp_water < esp_ing_water * amount:
            print(f"Sorry, there is not enough water!\n")
        elif esp_coffee < esp_ing_coffee * amount:
            print(f"Sorry, there is not enough coffee!\n")
    else:
        print("\n~~~~~~~~YOUR ORDER~~~~~~~~")
        print(f"Espresso cost: Rp{coffee_cost["espresso_cost"]}")
        print(f"{amount} espresso: Rp{coffee_cost["espresso_cost"]*amount}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        payment("espresso", coffee_cost["espresso_cost"], amount)


# Cek bahan baku latte
def latte_check(
    lat_water, lat_coffee, lat_milk, lat_ing_water, lat_ing_coffee, lat_ing_milk, amount
):
    if (
        lat_water < lat_ing_water * amount
        or lat_coffee < lat_ing_coffee * amount
        or lat_milk < lat_ing_milk * amount
    ):
        if (
            lat_water < lat_ing_water * amount
            and lat_coffee < lat_ing_coffee * amount
            and lat_milk < lat_ing_milk * amount
        ):
            print(f"Sorry, there is not enough water, coffee, and milk!\n")
        elif (
            lat_water < lat_ing_water * amount and lat_coffee < lat_ing_coffee * amount
        ):
            print(f"Sorry, there is not enough water and coffee!\n")
        elif lat_water < lat_ing_water * amount and lat_milk < lat_ing_milk * amount:
            print(f"Sorry, there is not enough water and milk!\n")
        elif lat_coffee < lat_ing_coffee * amount and lat_milk < lat_ing_milk * amount:
            print(f"Sorry, there is not enough coffee and milk!\n")
        elif lat_water < lat_ing_water * amount:
            print(f"Sorry, there is not enough water!\n")
        elif lat_coffee < lat_ing_coffee * amount:
            print(f"Sorry, there is not enough coffee!\n")
        else:
            print(f"Sorry, there is not enough mlik!\n")
    else:
        print("\n~~~~~~~~YOUR ORDER~~~~~~~~")
        print(f"Latte cost: Rp{coffee_cost["latte_cost"]}")
        print(f"{amount} latte: Rp{coffee_cost["latte_cost"]*amount}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        payment("latte", coffee_cost["latte_cost"], amount)


# Cek bahan baku cappuccino
def cappuccino_check(
    cap_water, cap_coffee, cap_milk, cap_ing_water, cap_ing_coffee, cap_ing_milk, amount
):
    if (
        cap_water < cap_ing_water * amount
        or cap_coffee < cap_ing_coffee * amount
        or cap_milk < cap_ing_milk * amount
    ):
        if (
            cap_water < cap_ing_water * amount
            and cap_coffee < cap_ing_coffee * amount
            and cap_milk < cap_ing_milk * amount
        ):
            print(f"Sorry, there is not enough water, coffee and milk!\n")
        elif (
            cap_water < cap_ing_water * amount and cap_coffee < cap_ing_coffee * amount
        ):
            print(f"Sorry, there is not enough water and coffee!\n")
        elif cap_water < cap_ing_water * amount and cap_milk < cap_ing_milk * amount:
            print(f"Sorry, there is not enough water and milk!\n")
        elif cap_coffee < cap_ing_coffee * amount and cap_milk < cap_ing_milk * amount:
            print(f"Sorry, there is not enough coffee and milk!\n")
        elif cap_water < cap_ing_water * amount:
            print(f"Sorry, there is not enough water!\n")
        elif cap_coffee < cap_ing_coffee * amount:
            print(f"Sorry, there is not enough coffee!\n")
        else:
            print(f"Sorry, there is not enough mlik!\n")
    else:
        print("\n~~~~~~~~YOUR ORDER~~~~~~~~")
        print(f"Cappuccino cost: Rp{coffee_cost["cappuccino_cost"]}")
        print(f"{amount} cappuccino: Rp{coffee_cost["cappuccino_cost"]*amount}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        payment("cappuccino", coffee_cost["cappuccino_cost"], amount)


# Menyimpan hasil return report
report_resources = report()
coffee_cost = cost()
menu_resources = menu_ingredient()


def coffee_machine_program():
    print("COFFEE MACHINE PROGRAM!")
    run_program = True
    while run_program:
        user_input = input("What would you like? espresso/latte/cappuccino: ").lower()
        if user_input == "report":
            print("---Coffee Machine Report---")
            print(
                f"Ingredrient:\tMoney:\nWater: {report_resources["water"]}\tRp{report_resources["money"]}\nMilk: {report_resources["milk"]}\nCoffee: {report_resources["coffee"]}\n"
            )
        elif user_input == "off":
            print("Cleaning system...")
            time.sleep(2)
            print("Coffee machine turned off. See you next time!")
            run_program = False
        elif user_input == "espresso":
            user_amount = int(input(f"How many {user_input}?: "))
            espresso_check(
                report_resources["water"],
                report_resources["coffee"],
                menu_resources["espresso"]["water"],
                menu_resources["espresso"]["coffee"],
                user_amount,
            )

        elif user_input == "latte":
            user_amount = int(input(f"How many {user_input}?: "))
            latte_check(
                report_resources["water"],
                report_resources["coffee"],
                report_resources["milk"],
                menu_resources["latte"]["water"],
                menu_resources["latte"]["coffee"],
                menu_resources["latte"]["milk"],
                user_amount,
            )
        elif user_input == "cappuccino":
            user_amount = int(input(f"How many {user_input}?: "))
            cappuccino_check(
                report_resources["water"],
                report_resources["coffee"],
                report_resources["milk"],
                menu_resources["cappuccino"]["water"],
                menu_resources["cappuccino"]["coffee"],
                menu_resources["cappuccino"]["milk"],
                user_amount,
            )
        else:
            print("Choose correctly!")


# Running program
coffee_machine_program()
