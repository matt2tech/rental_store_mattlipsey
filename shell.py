from disk import *
from core import *


def rent_total(rent_cart, inventory):
    rent_fee = rental_fee(rent_cart, inventory)
    replacement_cost = replacement_deposit(rent_cart, inventory)
    print('\nRent')
    for item in rent_cart:
        item_name = inventory[item]['Item']
        rental_rate = '{0:.2f}'.format(inventory[item]['Rental Rate'] * 1.07)
        replacement = '{0:.2f}'.format(
            inventory[item]['Replacement Value'] * .1)
        print(
            'Item: {}\n\tRental Rate: ${}\n\tReplacement Deposit: ${}'.format(
                item_name, rental_rate, replacement))
    print('Total: ${}\n'.format('{0:.2f}'.format(rent_fee + replacement_cost)))


def return_total(return_dict):
    print('Return')
    for inv in return_dict:
        rent_fee = return_fee(inv)
        deposit = deposit_return(inv)
        for item, info in inv.items():
            item_name = item
            days = info['Days Rented']
            rental = '{0:.2f}'.format(info['Rental Rate'])
            replace = '{0:.2f}'.format(info['Replacement Deposited'])
            print(
                'Item: {}\n\tDays Rented: {}\n\tRental Rate: ${}\n\tReplacement Deposited: ${}'.
                format(item_name, days, rental, replace))
        print('Total: ${0:.2f}\nDeposit Return: ${1:.2f}\n'.format(
            round(rent_fee, 2), round(deposit, 2)))


def print_inventory(inventory):
    for item, info in inventory.items():
        print(
            "Item Number: {}\n\tItem: {}\n\tRental Rate: ${}\n\tReplacement Value: ${}\n\tIn-Stock: {}\n".
            format(item, info['Item'], '{0:.2f}'.format(
                float(info['Rental Rate'])), '{0:.2f}'.format(
                    float(info['Replacement Value'])), info['In-Stock']))


def print_transactions(transactions):
    for transaction in transactions:
        for item, info in transaction.items():
            print(
                "Type: {}\nName: {}\n\tItem: {}\n\tDays Rented: {}\n\tRent Total: ${}\n\tReplacement Deposit: ${}\n".
                format(item, info['Name'], info['Item'], info['Days Rented'],
                       '{0:.2f}'.format(info['Rent Total']), '{0:.2f}'.format(
                           info['Replacement Deposit'])))


def revenue(transactions):
    revenue_total = 0
    for transaction in transactions:
        for item, info in transaction.items():
            revenue_total += info['Rent Total']
    print('Revenue: ${0:.2f}'.format(revenue_total))


def main():
    inventory = load_inventory()
    transactions = load_transactions()
    rent_cart = []
    return_dict = []
    new_transactions = []
    user = ''
    while user != '3':
        user = input(
            '\nWelcome to Matt\'s Rents.\nAre you a customer or an employee?\n1 - Customer\n2 - Employee\n3 - Quit\n>>> '
        )
        if user == '1':
            name = input('\nWhat is the name of this order?\n>>> ')
            option = ''
            while option != '4':
                option = input(
                    '\nAre you returning or renting?\n1 - Return\n2 - Rent\n3 - Done\n4 - Quit\n>>> '
                )
                if option == '1':
                    print_inventory(inventory)
                    return_item = input('\nWhat are you returning?\n>>> ')
                    if inventory.get(return_item, False):
                        returning(return_item, inventory)
                        while True:
                            days = input(
                                '\nHow many days have you had this item?\n>>> '
                            )
                            if days.isdigit():
                                days = int(days)
                                return_dict.append(
                                    return_listing(return_item, inventory,
                                                   days))
                                add_return(name, new_transactions, return_item,
                                           inventory, days)
                                break
                            else:
                                print('Provide an appropriate number.')
                    else:
                        print('Sorry, we do not carry that.')
                elif option == '2':
                    print_inventory(inventory)
                    rent_item = input('\nWhat would you like to rent?\n>>> ')
                    if inventory.get(rent_item, False):
                        renting(rent_item, inventory)
                        rent_cart.append(rent_item)
                        add_rent(name, new_transactions, rent_item, inventory)
                    else:
                        print('Sorry, we do not carry that.')
                elif option == '3':
                    if new_transactions == []:
                        print('Leaving Matt\'s Rents...')
                        exit()
                    else:
                        print('\nHere\'s your receipt')
                        print('-----------------------------')
                        print(name)
                        rent_total(rent_cart, inventory)
                        return_total(return_dict)
                        update_stock(inventory)
                        update_history(new_transactions)
                        exit()
                elif option == '4':
                    exit()
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
                            '\nWhat would you like to review?\n1 - Stock\n2 - Transcation History\n3 - Revenue\n4 - Quit\n>>> '
                        )
                        if employee_options == '1':
                            print_inventory(inventory)
                        elif employee_options == '2':
                            print_transactions(transactions)
                        elif employee_options == '3':
                            revenue(transactions)
                        elif employee_options == '4':
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
