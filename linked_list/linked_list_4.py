"""
Add two numbers whose digits are stored in a linked list
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/add_reverse/add_reverse_challenge.ipynb
"""
from linked_list.linked_list_7 import MyLinkedList as PersonalLinkedList, LinkedList, Node


class MyMyLinkedList(PersonalLinkedList):
    def add_numbers(self, first_node: Node, second_node: Node, carry: int = 0):
        if first_node is None and second_node is None:
            summary = carry
        elif first_node is None:
            summary = second_node.data + carry
        elif second_node is None:
            summary = first_node.data + carry
        else:
            summary = first_node.data + second_node.data + carry
        return summary % 10, int(summary / 10)

    def add_reverse(self, first_list: PersonalLinkedList, second_list: PersonalLinkedList):
        if first_list is None or second_list is None:
            return
        first_node = first_list.head
        second_node = second_list.head
        carry = 0
        while True:
            if first_node is None and second_node is None and carry == 0:
                break
            summary, carry = self.add_numbers(first_node, second_node, carry)
            self.append(summary)
            if first_node is not None:
                first_node = first_node.next
            if second_node is not None:
                second_node = second_node.next
        return self


class MyLinkedList(LinkedList):
    def _add_reverse(self, first_node: Node, second_node: Node, carry: int = 0):
        if first_node is None and second_node is None and carry == 0:
            return
        value = carry
        value += first_node.data if first_node else 0
        value += second_node.data if second_node else 0
        carry = 1 if value >= 10 else 0
        remainder = value % 10
        node = Node(remainder)
        node.next = self._add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if first_node is not None else None,
            carry)
        return node

    def add_reverse(self, first_list: LinkedList, second_list: LinkedList):
        if first_list is None or second_list is None:
            return
        self.head = self._add_reverse(first_list.head, second_list.head)
        return self


# %load test_add_reverse.py
import unittest


class TestAddReverse(unittest.TestCase):

    def test_add_reverse(self):
        print('Test: Empty list(s)')
        self.assertEqual(MyMyLinkedList().add_reverse(None, None), None)
        self.assertEqual(MyMyLinkedList().add_reverse(Node(5), None), None)
        self.assertEqual(MyMyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = MyMyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyMyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyMyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = MyMyLinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = MyMyLinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = MyMyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')

        print('Test: Empty list(s)')
        self.assertEqual(MyLinkedList().add_reverse(None, None), None)
        self.assertEqual(MyLinkedList().add_reverse(Node(5), None), None)
        self.assertEqual(MyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = MyLinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = MyLinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')


def main():
    test = TestAddReverse()
    test.test_add_reverse()


if __name__ == '__main__':
    main()
