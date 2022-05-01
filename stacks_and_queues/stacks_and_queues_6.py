"""
Implement a queue
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_list/queue_list_challenge.ipynb
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyQueue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        self.first = Node(data, self.first)
        if self.last is None:
            self.last = self.first

    def dequeue(self):
        if self.first is None and self.last is None:
            return
        node = self.first
        if node == self.last:
            self.first = None
            self.last = None
            return node.data
        while node.next != self.last:
            node = node.next
        tmp = self.last
        self.last = node
        return tmp.data


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            tmp = self.tail
            tmp.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None and self.tail is None:
            return
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data


# %load test_queue_list.py
import unittest


class TestQueue(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Dequeue an empty queue')
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        self.assertEqual(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

        print('Success: test_end_to_end')


def main():
    test = TestQueue()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
