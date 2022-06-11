"""
Determine the height of a tree
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_height/height_challenge.ipynb
"""
from graphs_and_trees.graphs_and_trees_11 import MyBst, Bst, Node
from graphs_and_trees.results import Results


class MyBstHeight(MyBst):
    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1


# %load test_height.py
import unittest


class TestHeight(unittest.TestCase):

    def test_height(self):
        bst = MyBstHeight(Node(5))
        self.assertEqual(bst.height(bst.root), 1)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.height(bst.root), 3)

        print('Success: test_height')


def main():
    test = TestHeight()
    test.test_height()


if __name__ == '__main__':
    main()
