
from eve_numbers import eve_numbers
def test_eve_numbers():
    """Test the eve_numbers function."""
    assert eve_numbers() == 6, "The sum should be 6"
    assert eve_numbers() == 4, "The sum should be 4"
    assert eve_numbers() == 2, "The sum should be 2"
    assert eve_numbers() == 0, "The sum should be 0"