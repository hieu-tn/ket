"""
Delete a node in the middle of a linked list
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/delete_mid/delete_mid_challenge.ipynb
"""
from linked_list.linked_list_7 import MyLinkedList as PersonalLinkedList, LinkedList, Node


class MyMyLinkedList(PersonalLinkedList):
    def delete_node(self, node):
        if self.__len__() == 0 or node is None:
            return
        curr = self.head
        prev = None
        while curr is not None:
            if curr.data == node.data:
                if curr.next is None:
                    curr.data = None
                else:
                    prev.next = curr.next
                break
            else:
                prev = curr
            curr = curr.next


class MyLinkedList(LinkedList):
    def delete_node(self, node):
        # if self.__len__() == 0 or node is None:
        #     return
        # curr = self.head
        # while curr is not None:
        #     next = curr.next
        #     if curr.data == node.data:
        #         if next is not None:
        #             curr.data = curr.next.data
        #             curr.next = curr.next.next
        #         else:
        #             curr.data = None
        #     curr = curr.next
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next


# %load test_delete_mid.py
import unittest


class TestDeleteNode(unittest.TestCase):

    def test_delete_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyMyLinkedList(None)
        linked_list.delete_node(None)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyMyLinkedList(head)
        linked_list.delete_node(head)
        self.assertEqual(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyMyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 2])

        print('Test: Multiple nodes, delete last element')
        linked_list = MyMyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 3, None])

        print('Success: test_delete_node')

        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        self.assertEqual(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 2])

        print('Test: Multiple nodes, delete last element')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 3, None])

        print('Success: test_delete_node')


def main():
    test = TestDeleteNode()
    test.test_delete_node()


if __name__ == '__main__':
    main()
