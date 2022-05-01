"""
Implement a stack
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack/stack_challenge.ipynb
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyStack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return
        node = self.top
        self.top = self.top.next
        return node.data

    def peek(self):
        if self.top is None:
            return
        return self.top.data

    def is_empty(self):
        return self.top is None


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return
        return self.top.data

    def is_empty(self):
        return False if self.peek() is not None else True


# %load test_stack.py
import unittest


class TestStack(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Empty stack')
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.pop(), None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.is_empty(), True)

        print('Success: test_end_to_end')


def main():
    test = TestStack()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
