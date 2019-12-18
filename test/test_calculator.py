"""Test file for the calculator"""

import sys
import unittest
import math
from io import StringIO

from calculator.calculator import Calculator, get_number


class TestCalculator(unittest.TestCase):
    """Test for the Calculator"""

    def setUp(self):
        self.stdout = StringIO()
        sys.stdout = self.stdout
        self.cal = Calculator()

    def test_get_number(self):
        """Test get_number function"""
        self.assertEqual(get_number("10"), 10)
        self.assertEqual(get_number("0b10"), 2)
        self.assertEqual(get_number("0x10"), 16)
        self.assertEqual(get_number("0o10"), 8)
        self.assertEqual(get_number("0.25"), 0.25)
        self.assertEqual(get_number("aaa"), 2730)
        self.assertEqual(get_number("alc"), "alc")

    def test_add(self):
        """Test add method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.add()
        self.assertEqual(self.cal.stack.pop(), 15)

    def test_sub(self):
        """Test sub method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.sub()
        self.assertEqual(self.cal.stack.pop(), -5)

        self.cal.stack.append(25.5)
        self.cal.stack.append(10)
        self.cal.sub()
        self.assertEqual(self.cal.stack.pop(), 15.5)

    def test_mul(self):
        """Test mul method"""
        self.cal.stack.append(5)
        self.cal.stack.append(-10)
        self.cal.mul()
        self.assertEqual(self.cal.stack.pop(), -50)

        self.cal.stack.append(0)
        self.cal.stack.append(-10)
        self.cal.mul()
        self.assertEqual(self.cal.stack.pop(), 0)

    def test_div(self):
        """Test div method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.div()
        self.assertEqual(self.cal.stack.pop(), 0.5)

        # If div by 0, the stack remains the same
        self.cal.stack.append(5)
        self.cal.stack.append(0)
        self.cal.div()
        self.assertEqual(self.stdout.getvalue(), "Impossible to divise by 0\n")
        self.assertEqual(len(self.cal.stack), 2)

    def test_pow(self):
        """Test pow method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.pow()
        self.assertEqual(self.cal.stack.pop(), 5**10)

        self.cal.stack.append(5)
        self.cal.stack.append(0)
        self.cal.pow()
        self.assertEqual(self.cal.stack.pop(), 1)

    def test_and(self):
        """Test _and method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal._and()
        self.assertEqual(self.cal.stack.pop(), 0)

        self.cal.stack.append(7)
        self.cal.stack.append(15)
        self.cal._and()
        self.assertEqual(self.cal.stack.pop(), 7)

    def test_or(self):
        """Test _or method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal._or()
        self.assertEqual(self.cal.stack.pop(), 15)

        self.cal.stack.append(7)
        self.cal.stack.append(15)
        self.cal._or()
        self.assertEqual(self.cal.stack.pop(), 15)

    def test_xor(self):
        """Test xor method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10)
        self.cal.xor()
        self.assertEqual(self.cal.stack.pop(), 15)

        self.cal.stack.append(7)
        self.cal.stack.append(15)
        self.cal.xor()
        self.assertEqual(self.cal.stack.pop(), 8)

    def test_shift_left(self):
        """Test shift_left method"""
        self.cal.stack.append(55)
        self.cal.stack.append(2)
        self.cal.shift_left()
        self.assertEqual(self.cal.stack.pop(), 220)

        self.cal.stack.append(10)
        self.cal.stack.append(5.2)
        self.cal.shift_left()
        self.assertEqual(self.stdout.getvalue(),
                         "This operation requires 2 int\n")
        self.assertEqual(self.cal.stack, [10, 5.2])

    def test_shift_right(self):
        """Test shift_right method"""
        self.cal.stack.append(55)
        self.cal.stack.append(2)
        self.cal.shift_right()
        self.assertEqual(self.cal.stack.pop(), 13)

        self.cal.stack.append(2)
        self.cal.stack.append(5)
        self.cal.shift_right()
        self.assertEqual(self.cal.stack.pop(), 0)

        self.cal.stack.append(10)
        self.cal.stack.append(5.2)
        self.cal.shift_right()
        self.assertEqual(self.stdout.getvalue(),
                         "This operation requires 2 int\n")
        self.assertEqual(self.cal.stack, [10, 5.2])

    def test_absolute_value(self):
        """Test absolute_value method"""
        self.cal.stack.append(5)
        self.cal.absolute_value()
        self.assertEqual(self.cal.stack.pop(), 5)

        self.cal.stack.append(-12.3)
        self.cal.absolute_value()
        self.assertEqual(self.cal.stack.pop(), 12.3)

    def test_inv(self):
        """Test inv method"""
        self.cal.stack.append(4)
        self.cal.inv()
        self.assertEqual(self.cal.stack.pop(), 0.25)

        self.cal.stack.append(-0.1)
        self.cal.inv()
        self.assertEqual(self.cal.stack.pop(), -10)

    def test_sin(self):
        """Test sin method"""
        self.cal.stack.append(0)
        self.cal.sin()
        self.assertEqual(self.cal.stack.pop(), 0.0)

        self.cal.stack.append(math.pi / 2)
        self.cal.sin()
        self.assertEqual(self.cal.stack.pop(), 1.0)

    def test_cos(self):
        """Test cos method"""
        self.cal.stack.append(0)
        self.cal.cos()
        self.assertEqual(self.cal.stack.pop(), 1.0)

        self.cal.stack.append(math.pi / 2)
        self.cal.cos()
        self.assertAlmostEqual(self.cal.stack.pop(), 0.0)

    def test_tan(self):
        """Test tan method"""
        self.cal.stack.append(0)
        self.cal.tan()
        self.assertEqual(self.cal.stack.pop(), 0.0)

        self.cal.stack.append(math.pi / 4)
        self.cal.tan()
        self.assertAlmostEqual(self.cal.stack.pop(), 1.0)

    def test_switch(self):
        """Test switch method"""
        self.cal.stack.append(-25)
        self.cal.stack.append(32.2)
        self.cal.switch()
        self.assertEqual(self.cal.stack, [32.2, -25])

    def test_copy(self):
        """Test copy method"""
        self.cal.copy()
        self.assertEqual(self.cal.stack, [])

        self.cal.stack.append(10)
        self.cal.copy()
        self.assertEqual(self.cal.stack, [10, 10])

    def test_print(self):
        """Test print method"""
        self.cal.stack.append(5)
        self.cal.stack.append(10.2)

        self.cal.print()
        self.cal.print()

        self.assertEqual(self.stdout.getvalue(), "10.2\n5\n")

    def test_print_hex(self):
        """Test print_hex_method"""
        self.cal.stack.append(500)
        self.cal.stack.append(10.0)
        self.cal.stack.append(12.2)

        self.cal.print_hex()
        self.cal.print_hex()
        self.cal.print_hex()

        self.assertEqual(self.stdout.getvalue(),
                         "0x1.8666666666666p+3\n0xA\n0x1F4\n")

    def test_print_bin(self):
        """Test print_bin_method"""
        self.cal.stack.append(500)
        self.cal.stack.append(10.0)
        self.cal.stack.append(2.5)

        self.cal.print_bin()
        self.cal.stack.pop()
        self.cal.print_bin()
        self.cal.print_bin()

        self.assertEqual(self.stdout.getvalue(),
                         "Not possible to print a float in binary\n0b1010\n0b111110100\n")

    def test_print_stack(self):
        """Test print_stack"""
        self.cal.stack.append(500)
        self.cal.stack.append(10.0)
        self.cal.stack.append(123.123)

        self.cal.print_stack()

        self.cal.clear_stack()
        self.cal.print_stack()

        self.assertEqual(self.stdout.getvalue(), "500, 10.0, 123.123\n\n")


if __name__ == "__main__":
    unittest.main()
