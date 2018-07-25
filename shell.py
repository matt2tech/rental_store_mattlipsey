from disk import *
from core import *


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


def print_inventory(inventory):
    for item, info in inventory.items():
        print(
            "Item Number: {}\n\tItem: {}\n\tRental Rate: ${}\n\tReplacement Value: ${}\n\tIn-Stock: {}\n".
            format(item, info['Item'], '{0:.2f}'.format(
                float(info['Rental Rate'])), '{0:.2f}'.format(
                    float(info['Replacement Value'])), info['In-Stock']))


def print_transcations(transcations):
    for item, info in transcations.items():
        print(
            "Type: {}\nName: {}\n\tItem: {}\n\tDays Rented: {}\n\tRent Total: ${}\n\tReplacement Fee: ${}".
            format(item, info['Name'], info['Item'], info['Days Rented'],
                   '{0:.2f}'.format(info['Rent Total']), '{0:.2f}'.format(
                       info['Replacement Fee'])))


def revenue(transcations):
    revenue_total = 0
    for item, info in transcations.items():
        if item == 'Return':
            revenue_total += info['Rent Total']
    print('{0:.2f}'.format(revenue_total))


def main():
    inventory = load_inventory()
    transcations = load_transcations()
    cart = []
    user = ''
    while user != '3':
        user = input(
            'Welcome to Matt\'s Rents.\nAre you a customer or an employee?\n1 - Customer\n2 - Employee\n3 - Quit\n>>> '
        )
        if user == '1':
            name = input('What is the name of this order?\n>>> ')
            option = ''
            while option != '4':
                option = input(
                    'Are you returning or renting?\n1 - Return\n2 - Rent\n3 - Done\n4 - Quit\n>>> '
                )
                if option == '1':
                    print_inventory(inventory)
                    return_item = input('What are you returning?\n>>> ')
                    if inventory.get(return_item, False):
                        returning(return_item, inventory)
                    else:
                        print('Sorry, we do not carry that.')
                elif option == '2':
                    print_inventory(inventory)
                    rent_item = input('What would you like to rent?\n>>> ')
                    if inventory.get(rent_item, False):
                        renting(rent_item, inventory)
                        cart.append(rent_item)
                    else:
                        print('Sorry, we do not carry that.')
                elif option == '3':
                    print('Here\'s your receipt')
                    print('-----------------------------')
                    print(name)
                    total(cart, inventory)
                    exit()
                elif option == '4':
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
                    employee_options = ''
                    while employee_options != '4':
                        employee_options = input(
                            'What would you like to review?\n1 - Stock\n2 - Transcation History\n3 - Revenue\n4 - Return to User\'s Menu\n5 - Quit\n>>> '
                        )
                        if employee_options == '1':
                            print_inventory(inventory)
                        elif employee_options == '2':
                            print_transcations(transcations)
                        elif employee_options == '3':
                            revenue(transcations)
                        elif employee_options == '4':
                            print('Returning to previous menu...\n')
                        elif employee_options == '5':
                            print('Leaving Matt\'s Rents...')
                            exit()
                        else:
                            print('Invalid option!')
                elif password == '':
                    print('Returning to previous menu...')
                else:
                    print('Invalid Password!')
        elif user == '3':
            print('Leaving Matt\'s Rents...')
        else:
            print('Invalid option!')


if __name__ == '__main__':
    main()
