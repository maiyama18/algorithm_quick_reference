class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add(value)
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def contains(self, value):
        node = self.root
        while node:
            if node.value == value:
                return True
            elif node.value < value:
                node = node.right
            else:
                node = node.left

        return False