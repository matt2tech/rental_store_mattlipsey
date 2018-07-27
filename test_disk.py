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
