def main():
    user = input(
        'Welcome to "store name".\nAre you a customer or employee?\n1 - Customer\n2 - Employee\n>>> '
    )
    if user == '1':
        print('inventory')
    elif user == '2':
        password = input('Input the store\'s password\n>>> ')


if __name__ == '__main__':
    main()
