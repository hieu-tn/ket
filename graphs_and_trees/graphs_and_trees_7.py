"""
Find the in-order successor of a given node in a binary search tree
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_successor/bst_successor_challenge.ipynb
"""
from graphs_and_trees.graphs_and_trees_11 import MyBst, Node


class MyBstSuccessor(object):
    def get_next(self, node):
        if node is None:
            return TypeError


# %load test_bst_successor.py
import unittest


class TestBstSuccessor(unittest.TestCase):

    def test_bst_successor_empty(self):
        bst_successor = MyBstSuccessor()
        bst_successor.get_next(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = MyBst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)

        bst_successor = MyBstSuccessor()
        self.assertEqual(bst_successor.get_next(nodes[4]), 5)
        self.assertEqual(bst_successor.get_next(nodes[5]), 6)
        self.assertEqual(bst_successor.get_next(nodes[8]), 9)
        self.assertEqual(bst_successor.get_next(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.assertRaises(TypeError, test.test_bst_successor_empty)


if __name__ == '__main__':
    main()
