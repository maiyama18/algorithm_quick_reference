import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(binary_search([], 3), False)

    def test_one_true(self):
        self.assertEqual(binary_search([3], 3), True)

    def test_one_false(self):
        self.assertEqual(binary_search([4], 3), False)

    def test_many_true(self):
        self.assertEqual(binary_search([2, 4, 7, 6, 3], 6), True)

    def test_many_false(self):
        self.assertEqual(binary_search([2, 4, 7, 6, 3], 5), False)

if __name__ == '__main__':
    unittest.main()