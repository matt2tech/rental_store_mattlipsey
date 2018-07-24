import core


def inventory_contents():
    with open('inventory.txt', 'r') as file:
        file.readline()
        contents = file.read()
    return contents


def inventory_stock_conversion(contents):
    item = contents.split(',')
    item_2 = '{0:.2f}'.format(float(item[2]))
    item_3 = '{0:.2f}'.format(float(item[3]))
    return (item[0]), item[1], item_2, item_3, int(item[4])


def load_inventory():
    contents = inventory_contents()
    inventory = {}
    lines = contents.split('\n')
    for line in lines:
        if line:
            item = inventory_stock_conversion(line)
            inventory[item[0]] = {
                'Item': item[1],
                'Rental Rate': item[2],
                'Replacement Value': item[3],
                'In-Stock': item[4]
            }

    return inventory


def print_inventory(inventory):
    for item, info in inventory.items():
        print(
            "Item Number: {}\n\tItem: {}\n\tRental Rate: ${}\n\tReplacement Value: ${}\n\tIn-Stock: {}\n".
            format(item, info['Item'], info['Rental Rate'],
                   info['Replacement Value'], info['In-Stock']))


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
    item_3 = '{0:.2f}'.format(float(item[3]))
    return item[0], item[1], int(item[2]), item_3


def load_transcations():
    contents = transcations_contents()
    transcations = {}
    lines = contents.split('\n')
    for line in lines:
        if line:
            item = transcations_stock_conversion(line)
            transcations[item[0]] = {
                'Item': item[1],
                'Days Rented': item[2],
                'Total': item[3]
            }

    return transcations


def print_transcations(transcations):
    for item, info in transcations.items():
        print("Name: {}\n\tItem: {}\n\tDays Rented: {}\n\tTotal: ${}".format(
            item, info['Item'], info['Days Rented'], info['Total']))
