#!python

from search import linear_search, binary_search
import unittest


class TestSearch(unittest.TestCase):
    def test_linear_search_with_items_in_list(self):
        # linear search can find items regardless of list order
        names = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
        # linear search should return the index of each item in the list
        self.assertEqual(linear_search(names, 'Winnie'), 0)
        self.assertEqual(linear_search(names, 'Kojin'), 1)
        self.assertEqual(linear_search(names, 'Brian'), 2)
        self.assertEqual(linear_search(names, 'Nabil'), 3)
        self.assertEqual(linear_search(names, 'Julia'), 4)
        self.assertEqual(linear_search(names, 'Alex'), 5)
        self.assertEqual(linear_search(names, 'Nick'), 6)

    def test_linear_search_with_items_not_in_list(self):
        # linear search can find items regardless of list order
        names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
        # linear search should return None for any item not in the list
        self.assertIsNone(linear_search(names, 'Jeremy'))
        self.assertIsNone(linear_search(names, 'nobody'))

    def test_binary_search_with_items_in_list(self):
        # binary search requires list values to be in sorted order
        names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
        # binary search should return the index of each item in the list
        self.assertEqual(binary_search(names, 'Alex'), 0)
        self.assertEqual(binary_search(names, 'Brian'), 1)
        self.assertEqual(binary_search(names, 'Julia'), 2)
        self.assertEqual(binary_search(names, 'Kojin'), 3)
        self.assertEqual(binary_search(names, 'Nabil'), 4)
        self.assertEqual(binary_search(names, 'Nick'), 5)
        self.assertEqual(binary_search(names, 'Winnie'), 6)

    def test_binary_search_with_items_not_in_list(self):
        # binary search requires list values to be in sorted order
        names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
        # binary search should return None for any item not in the list
        self.assertIsNone(binary_search(names, 'Jeremy'))
        self.assertIsNone(binary_search(names, 'nobody'))


if __name__ == '__main__':
    unittest.main()
