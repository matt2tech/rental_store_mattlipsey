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


def return_fee(inv):
    total = 0
    for item, info in inv.items():
        total += info['Rental Rate'] * info['Days Rented']
    return round(total, 2)


def deposit_return(inv):
    total = 0
    for item, info in inv.items():
        total += info['Replacement Deposited']
    return round(total, 2)


def return_listing(return_item, inventory, days):
    return_dict = {}
    item_name = inventory[return_item]['Item']
    rental_rate = round(inventory[return_item]['Rental Rate'] * 1.07, 2)
    replacement = round(inventory[return_item]['Replacement Value'] * .1, 2)
    return_dict[item_name] = {
        'Days Rented': days,
        'Rental Rate': rental_rate,
        'Replacement Deposited': replacement
    }
    return return_dict
