MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0

}


def coffee_choice():
    print("\nWhat would you like?\n1. espresso\n2. latte\n3. cappuccino")
    c_choice = input("Please choose from the above options: ").lower()
    if c_choice == '1':
        return 'espresso'
    elif c_choice == '2':
        return 'latte'
    elif c_choice == '3':
        return 'cappuccino'
    elif c_choice == 'off':
        global on_btn
        on_btn = False
        return 'break'
    elif c_choice == 'report':

        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g\nMoney: £{resources['money']}\n")
        select = int(input("1. Back to operation\n2. Turn off the Machine\nWhat would you like to do?: "))
        if select == 2:
            on_btn = False
            return 'break'
        else:
            print('Returned to operation!!')
            return coffee_choice()
    else:
        print("Wrong input, try again!!")
        return coffee_choice()


def availability(w, m, c):
        for res in resources:
            if res == 'water':
                if (resources[res] - w) < 0:
                    return f"no enough {res}"
            elif res == 'milk':
                if (resources[res] - m) < 0:
                    return f"no enough {res}"
            elif res == 'coffee':
                if (resources[res] - c) < 0:
                    return f"no enough {res}"
            else:
                return 'available'


def coin_check():
    print('Please insert coins. Machine not accepting 1,2,5 pennies!!')
    ten_penny = int(input('How many 10p ?: '))
    twenty_penny = int(input('How many 20p ?: '))
    fifty_penny = int(input('How many 50p ?: '))
    pound = int(input('How many £1 ?: '))
    two_pound = int(input('How many £2 ?: '))

    coins = (ten_penny * 0.1) + (twenty_penny * 0.2) + (fifty_penny * 0.5) + pound + (two_pound * 2)
    return coins


def transaction():
    resources['water'] -= water_need
    resources['milk'] -= milk_need
    resources['coffee'] -= coffee_need
    resources['money'] += cost
    if change == 0:
        print(f"\nYour Change is 0.\nHere is your {choice}. Enjoy!")
    else:
        print(f"\nHere is £{change} in change.\nHere is your {choice}. Enjoy!")

# TODO: 1. Print Report of all coffee machine resources


on_btn = True


while on_btn:
    choice = coffee_choice()

    if choice == 'break':
        break
    water_need = MENU[choice]['ingredients']['water']
    milk_need = MENU[choice]['ingredients']['milk']
    coffee_need = MENU[choice]['ingredients']['coffee']
    cost = MENU[choice]['cost']

    stock = availability(water_need, milk_need, coffee_need)

    if stock == 'available':
        inserted = coin_check()

        change = inserted - cost
        if change >= 0:
            transaction()
        else:
            print(f"Sorry that`s not enough money! Refunded £{inserted} .")

    else:
        print(stock)

if not on_btn:
    print('Machine turning off')



