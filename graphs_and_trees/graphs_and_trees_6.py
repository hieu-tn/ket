"""
Determine if a tree is a valid binary search tree
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_validate/bst_validate_challenge.ipynb
"""
from graphs_and_trees.graphs_and_trees_11 import MyBst, Node
from graphs_and_trees.results import Results


class MyBstValidate(MyBst):
    def validate(self):
        if self.root is None:
            raise TypeError
        rs = Results()
        node = self.root
        in_order_traversal(node, rs.add_result)
        return all([rs.results[i] <= rs.results[i + 1] for i in range(0, len(rs.results) - 1)])


def in_order_traversal(node, visit_func):
    # left node right
    if node.left is not None:
        in_order_traversal(node.left, visit_func)
    visit_func(node.data)
    if node.right is not None:
        in_order_traversal(node.right, visit_func)


# %load test_bst_validate.py
import unittest


class TestBstValidate(unittest.TestCase):

    def test_bst_validate_empty(self):
        bst = MyBstValidate(None)
        bst.validate()

    def test_bst_validate(self):
        bst = MyBstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        self.assertEqual(bst.validate(), True)

        bst = MyBstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        self.assertEqual(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.assertRaises(TypeError, test.test_bst_validate_empty)
    test.test_bst_validate()


if __name__ == '__main__':
    main()
