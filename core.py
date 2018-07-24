def renting(item_number, inventory):
    if inventory[item_number]['In-Stock'] < 1:
        print('Out of stock.')
    else:
        inventory[item_number]['In-Stock'] -= 1


def returning(item_number, inventory):
    inventory[item_number]['In-Stock'] += 1
