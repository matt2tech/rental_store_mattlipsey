from core import *
from bcca.test import should_print


@should_print
def test_renting_out_of_stock(output):
    renting('1', {'1': {'In-Stock': 0}})

    assert output == 'Out of stock.'


def test_renting_in_stock():
    inv = {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 5.00,
            'Replacement Value': 300.00,
            'In-Stock': 5
        }
    }

    renting('1', inv)

    assert inv['1']['In-Stock'] == 4


def test_returning():
    inv = {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 5.00,
            'Replacement Value': 300.00,
            'In-Stock': 5
        }
    }
    returning('1', inv)
    assert inv['1']['In-Stock'] == 6


def test_rental_fee():
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

    total = rental_fee(cart, inv)

    assert total == 26.75


def test_replacement_deposit():
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

    total = replacement_deposit(cart, inv)

    assert total == 330


def test_return_fee():
    inv = {
        'Grill': {
            'Days Rented': 3,
            'Rental Rate': 5.35,
            'Replacement Deposited': 30.00
        }
    }

    total = return_fee(inv)

    assert total == 16.05


def test_deposit_return():
    inv = {
        'Grill': {
            'Days Rented': 3,
            'Rental Rate': 5.35,
            'Replacement Deposited': 30.00
        }
    }

    total = deposit_return(inv)

    assert total == 30.00


def test_return_listing():
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

    dictionary = return_listing('1', inv, 3)

    assert dictionary == {
        'Grill': {
            'Days Rented': 3,
            'Rental Rate': 5.35,
            'Replacement Deposited': 30.00
        }
    }
