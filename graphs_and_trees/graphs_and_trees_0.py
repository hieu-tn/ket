"""
Implement depth-first search (pre-, in-, post-order) on a tree
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_dfs/dfs_challenge.ipynb
"""
from graphs_and_trees.graphs_and_trees_11 import MyBst, Bst, Node
from graphs_and_trees.results import Results


class MyBstDfs(MyBst):
    def in_order_traversal(self, node, visit_func):
        # left node right
        if node.left is not None:
            self.in_order_traversal(node.left, visit_func)
        visit_func(node.data)
        if node.right is not None:
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        # node left right
        visit_func(node.data)
        if node.left is not None:
            self.pre_order_traversal(node.left, visit_func)
        if node.right is not None:
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node, visit_func):
        # left right node
        if node.left is not None:
            self.post_order_traversal(node.left, visit_func)
        if node.right is not None:
            self.post_order_traversal(node.right, visit_func)
        visit_func(node.data)


class BstDfs(Bst):
    def in_order_traversal(self, node, visit_func):
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node.data)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        if node is not None:
            visit_func(node.data)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node, visit_func):
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node.data)


# %load test_dfs.py
import unittest


class TestDfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDfs, self).__init__()
        self.results = Results()

    def test_dfs(self):
        # bst = MyBstDfs(Node(5))
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        # bst = MyBstDfs(Node(1))
        bst = BstDfs(Node(1))
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()
