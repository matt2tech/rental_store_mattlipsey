from disk import *
from core import *


def main():
    inventory = load_inventory()
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
                    returning(return_item, inventory)
                elif option == '2':
                    print_inventory(inventory)
                    rent_item = input('What would you like to rent?\n>>> ')
                    renting(rent_item, inventory)
                elif option == '3':
                    print('receipt')
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
                            print('transcations')
                        elif employee_options == '3':
                            print('revenue')
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
