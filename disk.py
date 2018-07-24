import core


def file_contents():
    with open('inventory.txt', 'r') as file:
        file.readline()
        contents = file.read()
    return contents


def file_stock_conversion(contents):
    item = contents.split(',')
    item_2 = '{0:.2f}'.format(float(item[2]))
    item_3 = '{0:.2f}'.format(float(item[3]))
    return (item[0]), item[1], item_2, item_3, int(item[4])


def load_inventory():
    contents = file_contents()
    inventory = {}
    lines = contents.split('\n')
    for line in lines:
        if line:
            item = file_stock_conversion(line)
            inventory[item[0]] = {
                'Item': item[1],
                'Rent Per Day': item[2],
                'Replacement Value': item[3],
                'In-Stock': item[4]
            }

    return inventory


def print_inventory(inventory):
    for item, info in inventory.items():
        print(
            "Item Number: {}\n\tItem: {}\n\tRent Per Day: {}\n\tReplacement Value: {}\n\tIn-Stock: {}\n".
            format(item, info['Item'], info['Rent Per Day'],
                   info['Replacement Value'], info['In-Stock']))


def convert_to_string(inventory):
    strings = []
    for item_number, info in inventory.items():
        item = info['Item']
        rent = info['Rent Per Day']
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
