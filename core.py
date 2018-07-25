def renting(item_number, inventory):
    if inventory[item_number]['In-Stock'] < 1:
        print('Out of stock.')
    else:
        inventory[item_number]['In-Stock'] -= 1


def returning(item_number, inventory):
    inventory[item_number]['In-Stock'] += 1


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


def total(cart, inventory):
    rent_fee = rental_fee(cart, inventory)
    replacement_cost = replacement_fee(cart, inventory)
    for item in cart:
        item_name = inventory[item]['Item']
        rental_rate = '{0:.2f}'.format(
            float(inventory[item]['Rental Rate']) * 1.07)
        replacement = '{0:.2f}'.format(
            float(inventory[item]['Replacement Value']) * .1)
        print('Item: {}\n\tRental Rate: ${}\n\tReplacement Fee: ${}'.format(
            item_name, rental_rate, replacement))
    print('Total: ${}'.format('{0:.2f}'.format(
        float(rent_fee + replacement_cost))))
