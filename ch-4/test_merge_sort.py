import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_one(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted(self):
        self.assertEqual(merge_sort([2, 4, 7]), [2, 4, 7])

    def test_unsorted(self):
        self.assertEqual(merge_sort([8, 4, 5, 1, 6]), [1, 4, 5, 6, 8])

    def test_unsorted_with_duplication(self):
        self.assertEqual(merge_sort([7, 1, 3, 3, 8, 3, 4, 1]), [1, 1, 3, 3, 3, 4, 7, 8])

if __name__ == '__main__':
    unittest.main()