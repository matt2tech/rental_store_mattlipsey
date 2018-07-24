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
