from shell import *
from bcca.test import should_print


@should_print
def test_rent_total(output):
    inv = {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 5.00,
            'Replacement Value': 300.00,
            'In-Stock': 5
        },
        '2': {
            'Item': 'Boat',
            'Rental Rate': 20.00,
            'Replacement Value': 3000.00,
            'In-Stock': 3
        },
        '3': {
            'Item': 'Flat Screen Television',
            'Rental Rate': 7.50,
            'Replacement Value': 500.00,
            'In-Stock': 11
        }
    }

    cart = ['1', '2']

    rent_total(cart, inv)

    assert output == 'Rent\nItem: Grill\n\tRental Rate: $5.35\n\tReplacement Deposit: $30.00\nItem: Boat\n\tRental Rate: $21.40\n\tReplacement Deposit: $300.00\nTotal: $356.75'


@should_print
def test_return_total(output):
    inv = [{
        'Grill': {
            'Days Rented': 3,
            'Rental Rate': 3.21,
            'Replacement Deposited': 8
        }
    }]

    return_total(inv)

    assert output == 'Return\nItem: Grill\n\tDays Rented: 3\n\tRental Rate: $3.21\n\tReplacement Deposited: $8.00\nTotal: $9.63\nDeposit Return: $8.00\n'


@should_print
def test_print_inventory(output):
    inv = {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 5.00,
            'Replacement Value': 300.00,
            'In-Stock': 5
        },
        '2': {
            'Item': 'Boat',
            'Rental Rate': 20.00,
            'Replacement Value': 3000.00,
            'In-Stock': 3
        }
    }

    print_inventory(inv)

    assert output == '''Item Number: 1\n\tItem: Grill\n\tRental Rate: $5.00\n\tReplacement Value: $300.00\n\tIn-Stock: 5\n\nItem Number: 2\n\tItem: Boat\n\tRental Rate: $20.00\n\tReplacement Value: $3000.00\n\tIn-Stock: 3'''


@should_print
def test_print_transactions(output):
    transactions = [{
        'Rent': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 0,
            'Rent Total': 5.35,
            'Replacement Deposit': 30.00
        }
    }, {
        'Return': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Deposit': 0.00
        }
    }]

    print_transactions(transactions)

    assert output == 'Type: Rent\nName: Matt\n\tItem: Grill\n\tDays Rented: 0\n\tRent Total: $5.35\n\tReplacement Deposit: $30.00\n\nType: Return\nName: Matt\n\tItem: Grill\n\tDays Rented: 2\n\tRent Total: $10.70\n\tReplacement Deposit: $0.00\n'


@should_print
def test_revenue_example1(output):
    transactions = [{
        'Rent': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 0,
            'Rent Total': 5.35,
            'Replacement Deposit': 30.00
        }
    }, {
        'Return': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Deposit': 0.00
        }
    }, {
        'Rent': {
            'Name': 'Bob',
            'Item': 'Grill',
            'Days Rented': 0,
            'Rent Total': 5.35,
            'Replacement Deposit': 30.00
        }
    }, {
        'Return': {
            'Name': 'Bob',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Deposit': 0.00
        }
    }]

    revenue(transactions)

    assert output == 'Revenue: $32.10'


@should_print
def test_revenue_example2(output):
    transactions = [{
        'Rent': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 0,
            'Rent Total': 5.35,
            'Replacement Deposit': 30.00
        }
    }, {
        'Return': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Deposit': 0.00
        }
    }, {
        'Rent': {
            'Name': 'Bob',
            'Item': 'Grill',
            'Days Rented': 0,
            'Rent Total': 5.35,
            'Replacement Deposit': 30.00
        }
    }]

    revenue(transactions)

    assert output == 'Revenue: $21.40'
