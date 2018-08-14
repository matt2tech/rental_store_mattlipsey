from disk import *
import core


def rent_total(rent_cart, inventory):
    rent_fee = core.rental_fee(rent_cart, inventory)
    replacement_cost = core.replacement_deposit(rent_cart, inventory)
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
        rent_fee = core.return_fee(inv)
        deposit = core.deposit_return(inv)
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
    print('\nWelcome to Matt\'s Rents.')
    user = ''
    while user != '4':
        user = input(
            '\nAre you a customer or an employee?\n1 - Customer\n2 - Employee\n3 - Help\n4 - Quit\n>>> '
        )
        if user == '1':
            name = input('\nWhat is the name of this order?\n>>> ')
            option = ''
            while option != '5':
                option = input(
                    '\nAre you returning or renting?\n1 - Return\n2 - Rent\n3 - Done\n4 - Help\n5 - Quit\n>>> '
                )
                if option == '1':
                    print_inventory(inventory)
                    return_item = input('\nWhat are you returning?\n>>> ')
                    if inventory.get(return_item, False):
                        core.returning(return_item, inventory)
                        while True:
                            days = input(
                                '\nHow many days have you had this item?\n>>> '
                            )
                            if days.isdigit():
                                days = int(days)
                                return_dict.append(
                                    core.return_listing(
                                        return_item, inventory, days))
                                core.add_return(name, new_transactions,
                                                return_item, inventory, days)
                                break
                            else:
                                print('Provide an appropriate number.')
                    else:
                        print('Sorry, we do not carry that.')
                elif option == '2':
                    print_inventory(inventory)
                    rent_item = input('\nWhat would you like to rent?\n>>> ')
                    if inventory.get(rent_item, False):
                        core.renting(rent_item, inventory)
                        rent_cart.append(rent_item)
                        core.add_rent(name, new_transactions, rent_item,
                                      inventory)
                    else:
                        print(
                            'Sorry, we do not carry that, or we\'re out of stock.'
                        )
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
                    print('''
"Return"
    Customers can return a rented item here.
    Customer will be asked what the item was and
    many days he/she has had said item.  Customer
    will be charged based on days and rental
    rate of item.
"Rent"
    Customers can rent an item here.  Customer
    will be asked what item he/she will be
    renting.  Customer will be charged an
    initial rental rate and will be required
    to put down a replacement deposit of ten
    percent of the item's replacement value.
"Done"
    The order will be confirmed here.  The
    customer will receive a receipt with
    his/her total charge.  Customers will
    receive his/her replacement deposit 
    upon returns here.  If no order was
    placed, customer will close application.
"Quit"
    Quit will close application.''')
                elif option == '5':
                    print('Leaving Matt\'s Rents...')
                    exit()
                else:
                    print('Please input number associated with desired option')
        elif user == '2':
            employee_options = ''
            while employee_options != '5':
                employee_options = input(
                    '\nWhat would you like to review?\n1 - Stock\n2 - Transcation History\n3 - Revenue\n4 - Help\n5 - Quit\n>>> '
                )
                if employee_options == '1':
                    print_inventory(inventory)
                elif employee_options == '2':
                    print_transactions(transactions)
                elif employee_options == '3':
                    revenue(transactions)
                elif employee_options == '4':
                    print('''
"Stock"
    Employee can review information on
    items in stock, such as item\'s
    number, item\'s name, rental rate,
    replacement value, stock quantity.
"Transaction History"
    Employee can review information on
    previous transactions, such as the
    customer's name, item, days, rental
    rate, total rent charge, replacement
    deposit, and if the item was rented
    or returned.
"Revenue"
    Employee can review the total amount
    of money the store has made.
"Quit"
    Quit will close application.''')
                elif employee_options == '5':
                    print('Leaving Matt\'s Rents...')
                    exit()
                else:
                    print('Please input number associated with desired option')
        elif user == '3':
            print('''
"Customer"
    Customer will take the user to the customer
    menu.  The user can build his/her order and
    confirm it here.
"Employee"
    Employee will take the user to the employee
    menu.  The user can review stock, transactions,
    and revenue here.
"Quit"
    Quit will close application.''')
        elif user == '4':
            print('Leaving Matt\'s Rents...')
        else:
            print('Please input number associated with desired option')


if __name__ == '__main__':
    main()
