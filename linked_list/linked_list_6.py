"""
Determine if a linked list is a palindrome
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/palindrome/palindrome_challenge.ipynb
"""
from linked_list.linked_list_7 import MyLinkedList as PersonalLinkedList, LinkedList, Node


class MyMyLinkedList(PersonalLinkedList):
    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        node = self.head
        seen = list()
        while node is not None:
            seen.append(node.data)
            node = node.next
        for i in range(int(len(seen) / 2)):
            if seen[i] != seen[-i - 1]:
                return False
        return True


class MyLinkedList(LinkedList):
    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        reversed_list = MyLinkedList()
        node = self.head
        for i in range(int(self.__len__() / 2)):
            reversed_list.insert_to_front(node.data)
            node = node.next
        node = node.next if self.__len__() % 2 == 1 else node
        reversed_node = reversed_list.head
        while reversed_node is not None:
            if reversed_node.data != node.data:
                return False
            node = node.next
            reversed_node = reversed_node.next
        return True


# %load test_palindrome.py
import unittest


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        print('Test: Empty list')
        linked_list = MyMyLinkedList()
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyMyLinkedList(head)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyMyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyMyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')

        print('Test: Empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


def main():
    test = TestPalindrome()
    test.test_palindrome()


if __name__ == '__main__':
    main()
