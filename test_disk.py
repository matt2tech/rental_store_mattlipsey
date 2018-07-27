from disk import *
from bcca.test import (
    should_print,
    fake_file,
)


@fake_file({'inventory.txt': '''header line
line
line
line
'''})
def test_inventory_contents():
    assert inventory_contents() == 'line\nline\nline\n'


def test_inventory_stock_conversion():
    contents = '1,Grill,3.0,80.0,5'

    content = inventory_stock_conversion(contents)

    assert content == ('1', 'Grill', '3.0', '80.0', 5)


@fake_file({'inventory.txt': '''header line
1,Grill,3,80,5
'''})
def test_load_inventory_example1():
    inv = load_inventory()

    assert inv == {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 3.0,
            'Replacement Value': 80.0,
            'In-Stock': 5
        }
    }


@fake_file({
    'inventory.txt':
    '''header line
1,Grill,3,80,5
2,Boat,14,1500,3
3,Tent,3.2,100,11
'''
})
def test_load_inventory_example2():
    inv = load_inventory()

    assert inv == {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 3.0,
            'Replacement Value': 80.0,
            'In-Stock': 5
        },
        '2': {
            'Item': 'Boat',
            'Rental Rate': 14.0,
            'Replacement Value': 1500.0,
            'In-Stock': 3
        },
        '3': {
            'Item': 'Tent',
            'Rental Rate': 3.2,
            'Replacement Value': 100.0,
            'In-Stock': 11
        }
    }


@should_print
def test_inventory_to_string_example1(output):
    inv = {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 3.0,
            'Replacement Value': 80.0,
            'In-Stock': 5
        }
    }

    inventory = inventory_to_string(inv)

    assert inventory == 'item number,item name,rental rate,replacement cost,stock\n1,Grill,3.0,80.0,5'


@should_print
def test_inventory_to_string_example2(output):
    inv = {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 3.0,
            'Replacement Value': 80.0,
            'In-Stock': 5
        },
        '2': {
            'Item': 'Boat',
            'Rental Rate': 14.0,
            'Replacement Value': 1500.0,
            'In-Stock': 3
        },
        '3': {
            'Item': 'High-Quality Tent',
            'Rental Rate': 3.2,
            'Replacement Value': 100.0,
            'In-Stock': 11
        }
    }

    inventory = inventory_to_string(inv)

    assert inventory == '''item number,item name,rental rate,replacement cost,stock
1,Grill,3.0,80.0,5
2,Boat,14.0,1500.0,3
3,High-Quality Tent,3.2,100.0,11'''


@fake_file({'inventory.txt': ''})
def test_update_stock():
    inv = {
        '1': {
            'Item': 'Grill',
            'Rental Rate': 3.0,
            'Replacement Value': 80.0,
            'In-Stock': 5
        },
        '2': {
            'Item': 'Boat',
            'Rental Rate': 14.0,
            'Replacement Value': 1500.0,
            'In-Stock': 3
        },
        '3': {
            'Item': 'High-Quality Tent',
            'Rental Rate': 3.2,
            'Replacement Value': 100.0,
            'In-Stock': 11
        }
    }

    update_stock(inv)

    assert open('inventory.txt').read(
    ) == '''item number,item name,rental rate,replacement cost,stock
1,Grill,3.0,80.0,5
2,Boat,14.0,1500.0,3
3,High-Quality Tent,3.2,100.0,11'''


@fake_file({'history.txt': '''header line
line
line
line
'''})
def test_transactions_contents():
    assert transactions_contents() == 'line\nline\nline\n'


def test_transactions_stock_conversion():
    contents = 'Return,Matt,Grill,3,16.05,8'

    content = transactions_stock_conversion(contents)

    assert content == ('Return', 'Matt', 'Grill', 3, '16.05', '8')
