import unittest
from sequential_search import sequential_search

class TestSequentialSearch(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sequential_search([], 3), False)

    def test_one_true(self):
        self.assertEqual(sequential_search([3], 3), True)

    def test_one_false(self):
        self.assertEqual(sequential_search([4], 3), False)

    def test_many_true(self):
        self.assertEqual(sequential_search([2, 4, 7, 6, 3], 6), True)

    def test_many_false(self):
        self.assertEqual(sequential_search([2, 4, 7, 6, 3], 5), False)

if __name__ == '__main__':
    unittest.main()