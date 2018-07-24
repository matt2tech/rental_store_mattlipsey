def renting(item_number, inventory):
    if inventory.get(item_number, False):
        if inventory[item_number]['In-Stock'] < 1:
            print('Out of stock.')
        else:
            inventory[item_number]['In-Stock'] -= 1
