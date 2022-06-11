"""
Implement breadth-first search on a tree
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_bfs/bfs_challenge.ipynb
"""
from graphs_and_trees.graphs_and_trees_11 import MyBst, Bst, Node
from graphs_and_trees.results import Results


class MyBstBfs(MyBst):
    def bfs(self, visit_func):
        q = [self.root]
        while len(q):
            node = q.pop(0)
            visit_func(node.data)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)


# %load test_bfs.py
import unittest


class TestBfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBfs, self).__init__()
        self.results = Results()

    def test_bfs(self):
        bst = MyBstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        self.assertEqual(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()
