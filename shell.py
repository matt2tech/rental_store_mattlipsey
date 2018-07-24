import disk
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


def main():
    inventory = load_inventory()
    user = ''
    while user != '3':
        user = input(
            'Welcome to Matt\'s Rents.\nAre you a customer or employee?\n1 - Customer\n2 - Employee\n3 - Quit\n>>> '
        )
        if user == '1':
            option = ''
            while option != '3':
                option = input(
                    'Are you returning or renting?\n1 - Return\n2 - Rent\n3 - Quit\n>>> '
                )
                if option == '1':
                    returning = input('What are you returning?\n>>> ')
                elif option == '2':
                    print_inventory(inventory)
                    rent = input('What would you like to rent?\n>>> ')
                    core.renting(rent, inventory)
                elif option == '3':
                    exit()
                elif option == '':
                    break
                else:
                    print('Invalid option!')
        elif user == '2':
            password = ' '
            while password != '':
                password = input('\nInput the store\'s password\n>>> ')
                if password == '1953':
                    print('transcations')
                elif password == '':
                    print('Returning to previous menu...')
                else:
                    print('Invalid Password!')
        else:
            print('Invalid option!')


if __name__ == '__main__':
    main()
