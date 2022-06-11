"""
Check if a binary tree is balanced
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/check_balance/check_balance_challenge.ipynb
"""
from graphs_and_trees.graphs_and_trees_11 import MyBst, Node
from graphs_and_trees.graphs_and_trees_3 import height


class MyBstBalance(MyBst):
    def check_balance(self):
        if self.root is None:
            raise TypeError
        is_balance = True
        q = [self.root]
        while len(q):
            node = q.pop()
            is_balance = abs(height(node.left) - height(node.right)) <= 1
            if not is_balance:
                return False
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return is_balance

    def _check_balance(self, node):
        if node is None:
            return True
        return abs(height(node.left) - height(node.right)) <= 1


# %load test_check_balance.py
import unittest


class TestCheckBalance(unittest.TestCase):

    def test_check_balance_empty(self):
        bst = MyBstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = MyBstBalance(Node(5))
        self.assertEqual(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        self.assertEqual(bst.check_balance(), True)

        bst = MyBstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        self.assertEqual(bst.check_balance(), False)

        bst = MyBstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        self.assertEqual(bst.check_balance(), True)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.assertRaises(TypeError, test.test_check_balance_empty)
    test.test_check_balance()


if __name__ == '__main__':
    main()
