"""
Implement a priority queue backed by an array
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/priority_queue/priority_queue_challenge.ipynb
"""


class PriorityQueueNode(object):
    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class MyPriorityQueue(object):
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)

    def extract_min(self):
        min_key = 999
        min_index = -1
        for index, node in enumerate(self.array):
            if min_key > node.key:
                min_key = node.key
                min_index = index
        if min_index > -1:
            node = self.array.pop(min_index)
            return node

    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj == obj:
                node.key = new_key
                break


# %load test_priority_queue.py
import unittest


class TestPriorityQueue(unittest.TestCase):

    def test_priority_queue(self):
        priority_queue = MyPriorityQueue()
        # priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.extract_min(), None)
        priority_queue.insert(PriorityQueueNode('a', 20))
        priority_queue.insert(PriorityQueueNode('b', 5))
        priority_queue.insert(PriorityQueueNode('c', 15))
        priority_queue.insert(PriorityQueueNode('d', 22))
        priority_queue.insert(PriorityQueueNode('e', 40))
        priority_queue.insert(PriorityQueueNode('f', 3))
        priority_queue.decrease_key('f', 2)
        priority_queue.decrease_key('a', 19)
        mins = []
        while priority_queue.array:
            mins.append(priority_queue.extract_min().key)
        self.assertEqual(mins, [2, 5, 15, 19, 22, 40])
        print('Success: test_min_heap')


def main():
    test = TestPriorityQueue()
    test.test_priority_queue()


if __name__ == '__main__':
    main()
