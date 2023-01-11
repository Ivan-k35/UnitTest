import unittest
from name_function import get_formatted_name


class FormattedNameTest(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """ Do names like 'Robert Downey' work correctly? """
        formatted_name = get_formatted_name('robert', 'downey')
        self.assertEqual(formatted_name, 'Robert Downey')


if __name__ == '__main__':
    unittest.main()
