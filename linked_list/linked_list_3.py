"""
Partition a linked list around a given value
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/partition/partition_challenge.ipynb
"""
from linked_list.linked_list_7 import MyLinkedList as PersonalLinkedList, LinkedList, Node


class MyMyLinkedList(PersonalLinkedList):
    def partition(self, data: int):
        if self.__len__() <= 1:
            return
        left = set()
        mid = set()
        right = set()
        node = self.head
        while node is not None:
            if node.data < data:
                left.add(node)
            elif node.data > data:
                right.add(node)
            else:
                mid.add(node)
        lst = left + mid + right
        lst[len(lst) - 1].next = None
        node = lst[0]
        for i in range(1, len(lst) - 1):
            node.next = lst[i]
        self.head = node


class MyLinkedList(LinkedList):
    def partition(self, data):
        if self.__len__() <= 1:
            return
        left = self.__new__()
        right = self.__new__()
        most_left = None
        node = self.node
        while node is not None:
            if node.data < data:
                left.append(node)
                most_left = node
            elif node.data > data:
                right.append(node)
            else:
                right.insert_to_front(node)
            node = node.next

        most_left.next = right.head
        self.head = left.head


# %load test_partition.py
import unittest


class TestPartition(unittest.TestCase):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyMyLinkedList(None)
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyMyLinkedList(Node(5))
        linked_list.partition(0)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyMyLinkedList(Node(5))
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyMyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        self.assertEqual(partitioned_list.get_all_data(),
                         [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')

        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        self.assertEqual(partitioned_list.get_all_data(),
                         [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()
