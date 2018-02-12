import unittest
from hash_search import hash_search, make_hash

class TestHashSearch(unittest.TestCase):
    def setUp(self):
        self.n = 1000

    def test_empty(self):
        h = make_hash([], self.n)
        self.assertEqual(hash_search(h, 3), False)

    def test_one_true(self):
        h = make_hash([3], self.n)
        self.assertEqual(hash_search(h, 3), True)

    def test_one_false(self):
        h = make_hash([4], self.n)
        self.assertEqual(hash_search(h, 3), False)

    def test_many_true(self):
        h = make_hash([2, 4, 7, 6, 3], self.n)
        self.assertEqual(hash_search(h, 6), True)

    def test_many_false(self):
        h = make_hash([2, 4, 7, 6, 3], self.n)
        self.assertEqual(hash_search(h, 5), False)

if __name__ == '__main__':
    unittest.main()