import disk
import core


def main():
    inventory = load_inventory()
    user = ''
    while user != '3':
        user = input(
            'Welcome to Matt\'s Rents.\nAre you a customer or employee?\n1 - Customer\n2 - Employee\n3 - Quit\n>>> '
        )
        if user == '1':
            name = input('What is the name of this order?\n>>> ')
            option = ''
            while option != '3':
                option = input(
                    'Are you returning or renting?\n1 - Return\n2 - Rent\n3 - Quit\n>>> '
                )
                if option == '1':
                    print_inventory(inventory)
                    returning = input('What are you returning?\n>>> ')
                    core.returning(returning, inventory)
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
