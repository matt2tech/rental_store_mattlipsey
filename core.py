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
        total += round(
            (float(info['Rental Rate'])), 2) * float(info['Days Rented'])
    return total


def deposit_return(inv):
    total = 0
    for item, info in inv.items():
        total += float(info['Replacement Deposited'])
    return total


def return_listing(return_item, inventory, days):
    return_dict = {}
    item_name = inventory[return_item]['Item']
    rental_rate = '{0:.2f}'.format(
        inventory[return_item]['Rental Rate'] * 1.07)
    replacement = '{0:.2f}'.format(
        inventory[return_item]['Replacement Value'] * .1)
    return_dict[item_name] = {
        'Days Rented': days,
        'Rental Rate': rental_rate,
        'Replacement Deposited': replacement
    }
    return return_dict
