"""
Find the start of a linked list loop
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/find_loop_start/find_loop_start_challenge.ipynb
"""
from linked_list.linked_list_7 import MyLinkedList as PersonalLinkedList, LinkedList, Node


class MyMyLinkedList(PersonalLinkedList):
    def find_loop_start(self):
        if self.__len__() <= 2:
            return
        seen = set()
        node = self.head
        while node is not None:
            if id(node) not in seen:
                seen.add(id(node))
            else:
                break
            node = node.next
        return node


class MyLinkedList(LinkedList):
    def find_loop_start(self):
        # if self.head is None or self.head.next is None:
        #     return
        # fast = self.head
        # slow = self.head
        # while fast.next is not None:
        #     for i in range(2):
        #         if fast.next is None:
        #             return
        #         else:
        #             fast = fast.next
        #     if fast is None:
        #         return
        #     if slow is fast:
        #         break
        #     slow = slow.next
        # slow = self.head
        # while slow is not fast:
        #     slow = slow.next
        #     fast = fast.next
        #     if fast is None:
        #         return
        # return slow
        if self.head is None or self.head.next is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        return slow


# %load test_find_loop_start.py
import unittest


class TestFindLoopStart(unittest.TestCase):

    def test_find_loop_start(self):
        print('Test: Empty list')
        linked_list = MyMyLinkedList()
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: One element')
        head = Node(1)
        linked_list = MyMyLinkedList(head)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Two elements')
        linked_list.append(2)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Three or more elements')
        linked_list.append(3)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: General case: Circular linked list')
        node10 = Node(10)
        node9 = Node(9, node10)
        node8 = Node(8, node9)
        node7 = Node(7, node8)
        node6 = Node(6, node7)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node0 = Node(0, node1)
        node10.next = node3
        linked_list = MyMyLinkedList(node0)
        self.assertEqual(linked_list.find_loop_start(), node3)

        print('Success: test_find_loop_start')

        print('Test: Empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: One element')
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Two elements')
        linked_list.append(2)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Three or more elements')
        linked_list.append(3)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: General case: Circular linked list')
        node10 = Node(10)
        node9 = Node(9, node10)
        node8 = Node(8, node9)
        node7 = Node(7, node8)
        node6 = Node(6, node7)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node0 = Node(0, node1)
        node10.next = node3
        linked_list = MyLinkedList(node0)
        self.assertEqual(linked_list.find_loop_start(), node3)

        print('Success: test_find_loop_start')


def main():
    test = TestFindLoopStart()
    test.test_find_loop_start()


if __name__ == '__main__':
    main()
