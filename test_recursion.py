#!python

from recursion import factorial
import unittest


class TestRecursion(unittest.TestCase):
    def test_factorial_with_small_integers(self):
        # factorial should return the product n*(n-1)*...*2*1 for n >= 0
        self.assertEqual(factorial(0), 1)  # base case
        self.assertEqual(factorial(1), 1)  # base case
        self.assertEqual(factorial(2), 2*1)
        self.assertEqual(factorial(3), 3*2*1)
        self.assertEqual(factorial(4), 4*3*2*1)
        self.assertEqual(factorial(5), 5*4*3*2*1)
        self.assertEqual(factorial(6), 6*5*4*3*2*1)
        self.assertEqual(factorial(7), 7*6*5*4*3*2*1)
        self.assertEqual(factorial(8), 8*7*6*5*4*3*2*1)
        self.assertEqual(factorial(9), 9*8*7*6*5*4*3*2*1)
        self.assertEqual(factorial(10), 10*9*8*7*6*5*4*3*2*1)

    def test_factorial_with_large_integers(self):
        self.assertEqual(factorial(15), 1307674368000)
        self.assertEqual(factorial(20), 2432902008176640000)
        self.assertEqual(factorial(25), 15511210043330985984000000)
        self.assertEqual(factorial(30), 265252859812191058636308480000000)

    def test_factorial_with_negative_integers(self):
        # factorial should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            factorial(-1)
            factorial(-5)

    def test_factorial_with_floating_point_numbers(self):
        # factorial should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            factorial(2.0)
            factorial(3.14159)


if __name__ == '__main__':
    unittest.main()
