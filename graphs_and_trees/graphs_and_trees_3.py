"""
Create a binary search tree with minimal height from a sorted array
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_min/bst_min_challenge.ipynb
"""
import math

from graphs_and_trees.graphs_and_trees_11 import MyBst, Bst, Node
from graphs_and_trees.results import Results


class MyMinBst(object):
    def create_min_bst(self, array):
        bst = MyBst()
        for data in array:
            node = bst.insert(data)
            bst.root = self.balance(node)
        return bst.root

    def balance(self, new_node, current_node=None):
        if current_node is None:
            current_node = new_node
        parent = current_node.parent
        if parent is None:
            return current_node

        lheight = height(parent.left)
        rheight = height(parent.right)

        if lheight - rheight >= 2:
            # left case
            if new_node.data <= current_node.data:
                current_node = self._balance(parent, 0)
            else:
                current_node = self._balance(parent, 1)
        elif rheight - lheight >= 2:
            # right case
            if new_node.data > current_node.data:
                current_node = self._balance(parent, 2)
            else:
                current_node = self._balance(parent, 3)
        else:
            current_node = parent

        return self.balance(new_node, current_node)

    def _balance(self, root, algo_type):
        if algo_type == 0:
            new_root = root.left
            new_root.parent = root.parent
            root.left = new_root.right
            if new_root.right is not None:
                new_root.right.parent = root
            new_root.right = root
            if root.parent is not None:
                root.parent.left = new_root
            root.parent = new_root
            return new_root
        elif algo_type == 1:
            old_left = root.left
            new_left = old_left.right
            new_left.parent = old_left.parent
            old_left.right = new_left.left
            old_left.right.parent = new_left
            new_left.left = old_left
            old_left.parent = new_left
            root.left = new_left
            return root
        elif algo_type == 2:
            new_root = root.right
            new_root.parent = root.parent
            root.right = new_root.left
            if new_root.left is not None:
                new_root.left.parent = root
            new_root.left = root
            if root.parent is not None:
                root.parent.right = new_root
            root.parent = new_root
            return new_root
        else:
            old_right = root.right
            new_right = old_right.left
            new_right.parent = old_right.parent
            old_right.left = new_right.right
            old_right.left.parent = new_right
            new_right.right = old_right
            old_right.parent = new_right
            root.right = new_right
            return root


# %load test_bst_min.py
import unittest


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),
                   height(node.right))


class TestBstMin(unittest.TestCase):

    def test_bst_min(self):
        min_bst = MyMinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 3)

        min_bst = MyMinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 4)

        print('Success: test_bst_min')


def main():
    test = TestBstMin()
    test.test_bst_min()


if __name__ == '__main__':
    main()
