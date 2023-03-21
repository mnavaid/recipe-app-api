"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test the add number method"""
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_substract_numbers(self):
        """Test the substration method"""
        res= calc.substract(5,11)
        self.assertEqual(res,6)