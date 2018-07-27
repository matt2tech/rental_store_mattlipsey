import core

# Inventory file conversion


def inventory_contents():
    with open('inventory.txt', 'r') as file:
        file.readline()
        contents = file.read()
    return contents


def inventory_stock_conversion(contents):
    item = contents.split(',')
    return (item[0]), item[1], item[2], item[3], int(item[4])


def load_inventory():
    contents = inventory_contents()
    inventory = {}
    lines = contents.split('\n')
    for line in lines:
        if line:
            item = inventory_stock_conversion(line)
            inventory[item[0]] = {
                'Item': item[1],
                'Rental Rate': float(item[2]),
                'Replacement Value': float(item[3]),
                'In-Stock': item[4]
            }

    return inventory


def inventory_to_string(inventory):
    strings = []
    for item, info in inventory.items():
        rental_item = info['Item']
        rental_rate = info['Rental Rate']
        replace = info['Replacement Value']
        stock = info['In-Stock']
        string = '{},{},{},{},{}'.format(item, rental_item, rental_rate,
                                         replace, stock)
        strings.append(string)
    strings.sort()
    inventory = '{},{},{},{},{}\n{}'.format('item number', 'item name',
                                            'rental rate', 'replacement cost',
                                            'stock', '\n'.join(strings))
    return inventory


def update_stock(inventory):
    text = inventory_to_string(inventory)
    with open('inventory.txt', 'w') as file:
        file.write(text)


# History file conversion


def transactions_contents():
    with open('history.txt', 'r') as file:
        file.readline()
        contents = file.read()
    return contents


def transactions_stock_conversion(contents):
    item = contents.split(',')
    return item[0], item[1], item[2], int(item[3]), item[4], item[5]


def load_transactions():
    contents = transactions_contents()
    transactions = []
    lines = contents.split('\n')
    for line in lines:
        if line:
            item = transactions_stock_conversion(line)
            transactions.append({
                item[0]: {
                    'Name': item[1],
                    'Item': item[2],
                    'Days Rented': item[3],
                    'Rent Total': float(item[4]),
                    'Replacement Deposit': float(item[5])
                }
            })

    return transactions


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


def transactions_to_string(new_transactions):
    strings = []
    for trans in new_transactions:
        for type_sale, info in trans.items():
            name = info['Name']
            rental_item = info['Item']
            days = info['Days Rented']
            rent_total = info['Rent Total']
            replace = info['Replacement Deposit']
            string = '{},{},{},{},{},{}'.format(type_sale, name, rental_item,
                                                days, round(rent_total, 2),
                                                round(replace, 2))
            strings.append(string)
        strings.sort()
        transaction = '\n'.join(strings)
    return transaction


def update_history(new_transactions):
    text = transactions_to_string(new_transactions)
    with open('history.txt', 'a') as file:
        file.write(text)
