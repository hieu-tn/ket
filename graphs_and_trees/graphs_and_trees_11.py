"""
Implement a binary search tree
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst/bst_challenge.ipynb
"""
from graphs_and_trees.results import Results


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class MyBst(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return new_node
        node = self.root
        while node is not None:
            if node.data > data:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = new_node
                    new_node.parent = node
                    return new_node
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = new_node
                    new_node.parent = node
                    return new_node

    def in_order_traversal(self, node, visit_func):
        # left root right
        if node.left is not None:
            self.in_order_traversal(node.left, visit_func)
        visit_func(node.data)
        if node.right is not None:
            self.in_order_traversal(node.right, visit_func)


class Bst(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, data, node=None):
        if self.root is None:
            self.root = Node(data)
            return self.root
        return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)

    def in_order_traversal(self, node, visit_func):
        # left root right
        if node.left is not None:
            self.in_order_traversal(node.left, visit_func)
        visit_func(node.data)
        if node.right is not None:
            self.in_order_traversal(node.right, visit_func)


# %load test_bst.py
import unittest


class TestTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__()
        self.results = Results()

    def test_tree_one(self):
        # bst = MyBst()
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

    def test_tree_two(self):
        # bst = MyBst()
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()


if __name__ == '__main__':
    main()
