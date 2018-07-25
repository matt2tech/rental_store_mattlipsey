import core


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


def convert_to_string(inventory):
    strings = []
    for item_number, info in inventory.items():
        item = info['Item']
        rent = info['Rental Rate']
        replace = info['Replacement Value']
        stock = info['In-Stock']
        string = '{},{},{},{},{}'.format(item_number, item, rent, replace,
                                         stock)
        strings.append(string)
    strings.sort()
    inventory = '\n'.join(strings)
    return inventory


def update_stock(inventory):
    text = convert_to_string(inventory)
    with open('inventory.txt', 'w') as file:
        file.write(text)


def transcations_contents():
    with open('history.txt', 'r') as file:
        file.readline()
        contents = file.read()
    return contents


def transcations_stock_conversion(contents):
    item = contents.split(',')
    return item[0], item[1], item[2], int(item[3]), item[4], item[5]


def load_transcations():
    contents = transcations_contents()
    transcations = {}
    lines = contents.split('\n')
    for line in lines:
        if line:
            item = transcations_stock_conversion(line)
            transcations[item[0]] = {
                'Name': item[1],
                'Item': item[2],
                'Days Rented': item[3],
                'Rent Total': float(item[4]),
                'Replacement Fee': float(item[5])
            }

    return transcations
