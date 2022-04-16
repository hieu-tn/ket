"""
Find the kth to last element of a linked list
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/kth_to_last_elem/kth_to_last_elem_challenge.ipynb
"""
from linked_list.linked_list_7 import MyLinkedList as PersonalLinkedList, LinkedList, Node


class MyMyLinkedList(PersonalLinkedList):
    def kth_to_last_elem(self, k):
        if self.__len__() == 0 or k >= self.__len__():
            return None
        if k == 0:
            return self.head.data
        index = self.__len__() - k - 1
        node = self.head
        for i in range(index):
            node = node.next
        return node.data


class MyLinkedList(LinkedList):
    def kth_to_last_elem(self, k):
        # [7, 5, 3, 1, 2] => 3
        # if self.__len__() == 0 or k >= self.__len__():
        #     return None
        # if k == 0:
        #     return self.head.data
        # fast = self.head
        # slow = fast
        # while fast is not None:
        #     for i in range(k):
        #         fast = fast.next
        #         if fast is None:
        #             break
        #     if fast is None:
        #         break
        #     slow = slow.next
        # return slow.data
        if self.head is None:
            return None
        fast = self.head
        slow = self.head

        # Give fast a headstart, incrementing it
        # once for k = 1, twice for k = 2, etc
        for _ in range(k):
            fast = fast.next
            # If k >= num elements, return None
            if fast is None:
                return None

        # Increment both pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data


# %load test_kth_to_last_elem.py
import unittest


class Test(unittest.TestCase):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyMyLinkedList(None)
        self.assertEqual(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        self.assertEqual(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyMyLinkedList(head)
        self.assertEqual(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        self.assertEqual(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')

        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        self.assertEqual(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        self.assertEqual(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        self.assertEqual(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()
