from shell import *
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

@should_print
def test_total(output):
    inv = [{
        '1': {
            'Item': 'Grill',
            'Rental Rate': 5.00,
            'Replacement Value': 300.00,
            'In-Stock': 5
        }
    }, {
        '2': {
            'Item': 'Boat',
            'Rental Rate': 20.00,
            'Replacement Value': 3000.00,
            'In-Stock': 3
        }
    }, {
        '3': {
            'Item': 'Flat Screen Television',
            'Rental Rate': 7.50,
            'Replacement Value': 500.00,
            'In-Stock': 11
        }
    }]

    cart = ['1', '2']

    total(cart, inv)

    assert output == 'Item: Grill\n\tRental Rate: $5.35\n\tReplacement Fee: $30.00\nItem: Boat\n\tRental Rate: $21.40\n\tReplacement Fee: $300.00\nTotal: $356.75'


@should_print
def test_print_inventory(output):
    inv = [{
        '1': {
            'Item': 'Grill',
            'Rental Rate': 5.00,
            'Replacement Value': 300.00,
            'In-Stock': 5
        }
    }, {
        '2': {
            'Item': 'Boat',
            'Rental Rate': 20.00,
            'Replacement Value': 3000.00,
            'In-Stock': 3
        }
    }]

    print_inventory(inv)

    assert output == '''Item Number: 1\n\tItem: Grill\n\tRental Rate: $5.00\n\tReplacement Value: $300.00\n\tIn-Stock: 5\n\nItem Number: 2\n\tItem: Boat\n\tRental Rate: $20.00\n\tReplacement Value: $3000.00\n\tIn-Stock: 3'''


@should_print
def test_print_transcations(output):
    transcations = [{
        'Rent': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 1,
            'Rent Total': 5.35,
            'Replacement Fee': 30.00
        }
    }, {
        'Return': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Fee': 0.00
        }
    }]

    print_transcations(transcations)

    assert output == 'Type: Rent\nName: Matt\n\tItem: Grill\n\tDays Rented: 1\n\tRent Total: $5.35\n\tReplacement Fee: $30.00\n\nType: Return\nName: Matt\n\tItem: Grill\n\tDays Rented: 2\n\tRent Total: $10.70\n\tReplacement Fee: $0.00\n'


@should_print
def test_revenue_example1(output):
    transcations = [{
        'Rent': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 1,
            'Rent Total': 5.35,
            'Replacement Fee': 30.00
        }
    }, {
        'Return': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Fee': 0.00
        }
    }, {
        'Rent': {
            'Name': 'Bob',
            'Item': 'Grill',
            'Days Rented': 1,
            'Rent Total': 5.35,
            'Replacement Fee': 30.00
        }
    }, {
        'Return': {
            'Name': 'Bob',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Fee': 0.00
        }
    }]

    revenue(transcations)

    assert output == 'Revenue: $21.40'


@should_print
def test_revenue_example2(output):
    transcations = [{
        'Rent': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 1,
            'Rent Total': 5.35,
            'Replacement Fee': 30.00
        }
    }, {
        'Return': {
            'Name': 'Matt',
            'Item': 'Grill',
            'Days Rented': 2,
            'Rent Total': 10.70,
            'Replacement Fee': 0.00
        }
    }, {
        'Rent': {
            'Name': 'Bob',
            'Item': 'Grill',
            'Days Rented': 1,
            'Rent Total': 5.35,
            'Replacement Fee': 30.00
        }
    }]

    revenue(transcations)

    assert output == 'Revenue: $10.70'
