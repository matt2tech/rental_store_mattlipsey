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
