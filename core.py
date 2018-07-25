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
        total += inventory[item]['Rental Rate'] * 1.07
    return round(total, 2)


def replacement_fee(cart, inventory):
    total = 0
    for item in cart:
        total += inventory[item]['Replacement Value'] * .1
    return round(total, 2)
