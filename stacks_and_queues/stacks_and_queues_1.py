"""
Implement a stack that keeps track of its minimum element
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack_min/stack_min_challenge.ipynb
"""
import sys

from stacks_and_queues.stacks_and_queues_5 import MyStack, Stack, Node


class MyStackMin(MyStack):
    def __init__(self, top=None):
        self.top = None
        self.min = None

    def minimum(self):
        if self.top is None:
            return sys.maxsize
        return self.min

    def push(self, data):
        self.top = Node(data, self.top)
        if self.min is None:
            self.min = data
        elif data < self.minimum():
            self.min = data

    def pop(self):
        if self.top is None:
            return
        data = self.top.data
        self.top = self.top.next
        if self.top is None:
            self.min = None
        elif data <= self.minimum():
            node = self.top
            self.min = node.data
            while node is not None:
                if node.data < self.min:
                    self.min = node.data
                node = node.next
        return data


class StackMin(Stack):
    def __init__(self, top=None):
        self.top = None
        self.stack_min = Stack()

    def minimum(self):
        if self.stack_min.top is None:
            return sys.maxsize
        return self.stack_min.top.data

    def push(self, data):
        # node = Node(data, self.top)
        # self.top = node
        # if self.stack_min.top is None:
        #     self.stack_min.top = node
        # elif data < self.stack_min.top.data:
        #     self.stack_min.push(data)
        super().push(data)
        if data < self.minimum():
            self.stack_min.push(data)

    def pop(self):
        # if self.top is None:
        #     return
        # data = self.top.data
        # self.top = self.top.next
        # if data == self.stack_min.top.data:
        #     self.stack_min.pop()
        # return data
        data = super().pop()
        if data == self.minimum():
            self.stack_min.pop()
        return data



# %load test_stack_min.py
import unittest


class TestStackMin(unittest.TestCase):
    def test_stack_min(self):
        print('Test: Push on empty stack, non-empty stack')
        stack = StackMin()
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.minimum(), 5)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.minimum(), 1)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.minimum(), 1)
        stack.push(0)
        self.assertEqual(stack.peek(), 0)
        self.assertEqual(stack.minimum(), 0)

        print('Test: Pop on non-empty stack')
        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.minimum(), 1)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.minimum(), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.minimum(), 5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.minimum(), sys.maxsize)

        print('Test: Pop empty stack')
        self.assertEqual(stack.pop(), None)

        print('Success: test_stack_min')


def main():
    test = TestStackMin()
    test.test_stack_min()


if __name__ == '__main__':
    main()
