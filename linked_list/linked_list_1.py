"""
Remove duplicates from a linked list
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/remove_duplicates/remove_duplicates_challenge.ipynb
"""
from linked_list.linked_list_7 import MyLinkedList as PersonalLinkedList, LinkedList


class MyMyLinkedList(PersonalLinkedList):
    def remove_dupes(self):
        if self.__len__() == 0 or self.__len__() == 1:
            return
        node = self.head
        prev = None
        seen = []
        while node is not None:
            if node.data not in seen:
                seen.append(node.data)
                prev = node
            else:
                prev.next = node.next
            node = node.next


class MyLinkedList(LinkedList):
    def remove_dupes(self):
        if self.__len__() == 0 or self.__len__() == 1:
            return
        node = self.head
        seen = set()
        prev = None
        while node is not None:
            if node.data in seen:
                prev.next = node.next
            else:
                seen.add(node.data)
                prev = node
            node = node.next

    def remove_dupes_single_pointer(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set({node.data})
        while node.next is not None:
            if node.next.data in seen_data:
                node.next = node.next.next
            else:
                seen_data.add(node.next.data)
                node = node.next

    def remove_dupes_in_place(self):
        if self.__len__() == 0 or self.__len__() == 1:
            return
        node = self.head
        while node is not None:
            curr = node.next
            prev = node
            while curr is not None:
                if node.data == curr.data:
                    prev.next = curr.next
                else:
                    prev = curr
                curr = curr.next
            node = node.next


# %load test_remove_duplicates.py
import unittest


class TestRemoveDupes(unittest.TestCase):

    def test_remove_dupes(self, linked_list):
        print('Test: Empty list')
        # linked_list.remove_dupes()
        linked_list.remove_dupes_single_pointer()
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list')
        linked_list.insert_to_front(2)
        # linked_list.remove_dupes()
        linked_list.remove_dupes_single_pointer()
        self.assertEqual(linked_list.get_all_data(), [2])

        print('Test: General case, duplicates')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        # linked_list.remove_dupes()
        linked_list.remove_dupes_single_pointer()
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print('Test: General case, no duplicates')
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print('Success: test_remove_dupes\n')


def main():
    test = TestRemoveDupes()
    # linked_list = MyMyLinkedList(None)
    # test.test_remove_dupes(linked_list)
    linked_list = MyLinkedList(None)
    test.test_remove_dupes(linked_list)


if __name__ == '__main__':
    main()
