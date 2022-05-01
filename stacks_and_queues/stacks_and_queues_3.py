"""
Implement a queue using two stacks
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_from_stacks/queue_from_stacks_challenge.ipynb
"""
from stacks_and_queues.stacks_and_queues_5 import MyStack, Stack


class MyQueueFromStacks(object):
    def __init__(self):
        self.head = None
        self.stack = None

    def shift_stacks(self, source, destination):
        while source.top is not None:
            data = source.pop()
            destination.push(data)

    def enqueue(self, data):
        if self.head is None:
            self.stack = MyStack()
            self.stack.push(data)
            self.head = self.stack.top
        else:
            reversed_stack = MyStack()
            self.shift_stacks(self.stack, reversed_stack)
            reversed_stack.push(data)
            self.shift_stacks(reversed_stack, self.stack)

    def dequeue(self):
        if self.head is None:
            return
        data = self.stack.pop()
        self.head = self.stack.top
        return data


class QueueFromStacks(object):
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def shift_stacks(self, source, destination):
        while source.top is not None:
            data = source.pop()
            destination.push(data)

    def enqueue(self, data):
        if not self.right_stack.is_empty():
            self.shift_stacks(self.right_stack, self.left_stack)
        self.left_stack.push(data)

    def dequeue(self):
        if not self.left_stack.is_empty():
            self.shift_stacks(self.left_stack, self.right_stack)
        return self.right_stack.pop()


# %load test_queue_from_stacks.py
import unittest


class TestQueueFromStacks(unittest.TestCase):

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        num_items = 3
        for i in range(0, num_items):
            queue.enqueue(i)

        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        self.assertEqual(queue.dequeue(), 0)

        print('Test: Multiple dequeue in a row')
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

        print('Test: Enqueue after a dequeue')
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)

        print('Success: test_queue_from_stacks')


def main():
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


if __name__ == '__main__':
    main()
