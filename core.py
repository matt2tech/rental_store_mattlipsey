def returning(item_number, inventory):
    inventory[item_number]['In-Stock'] += 1


def renting(item_number, inventory):
    if inventory[item_number]['In-Stock'] < 1:
        print('Out of stock.')
    else:
        inventory[item_number]['In-Stock'] -= 1


def rental_fee(cart, inventory):
    total = 0
    for item in cart:
        total += round(inventory[item]['Rental Rate'] * 1.07, 2)
    return total


def replacement_deposit(cart, inventory):
    total = 0
    for item in cart:
        total += round(inventory[item]['Replacement Value'] * .1, 2)
    return total


def return_fee(cart, inventory, days):
    total = 0
    for item in cart:
        total += round((inventory[item]['Rental Rate'] * 1.07), 2) * days
    return total
