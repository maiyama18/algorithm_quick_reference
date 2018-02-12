import unittest
from binary_tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def test_empty(self):
        bt = BinaryTree()
        self.assertEqual(bt.contains(3), False)

    def test_true(self):
        bt = BinaryTree()
        for x in [4,2,6,8,1,5]:
            bt.add(x)
        self.assertEqual(bt.contains(4), True)
        self.assertEqual(bt.contains(5), True)
        self.assertEqual(bt.contains(6), True)
        self.assertEqual(bt.contains(8), True)

    def test_false(self):
        bt = BinaryTree()
        for x in [4,2,6,8,1,5]:
            bt.add(x)
        self.assertEqual(bt.contains(3), False)
        self.assertEqual(bt.contains(7), False)
        self.assertEqual(bt.contains(9), False)

if __name__ == '__main__':
    unittest.main()