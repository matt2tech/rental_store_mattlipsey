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


def add_return(name, new_transactions, return_item, inventory, days):
    item_name = inventory[return_item]['Item']
    rent_total = round(inventory[return_item]['Rental Rate'] * 1.07, 2)
    new_transactions.append({
        'Return': {
            'Name': name,
            'Item': item_name,
            'Days Rented': days,
            'Rent Total': (rent_total * days),
            'Replacement Deposit': 0.00
        }
    })


def add_rent(name, new_transactions, rent_item, inventory):
    item_name = inventory[rent_item]['Item']
    rent_total = round(inventory[rent_item]['Rental Rate'] * 1.07, 2)
    replace = round(inventory[rent_item]['Replacement Value'] * .1, 2)
    new_transactions.append({
        'Rent': {
            'Name': name,
            'Item': item_name,
            'Days Rented': 0,
            'Rent Total': rent_total,
            'Replacement Deposit': replace
        }
    })
