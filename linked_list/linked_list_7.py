"""
Implement a linked list
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/linked_list/linked_list_challenge.ipynb
"""


class MyNode(object):
    data = None

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return self.data


class MyLinkedList(object):
    head: MyNode = None

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert_to_front(self, data):
        if data is None:
            return
        self.head = MyNode(data, self.head)

    def append(self, data):
        if data is None:
            return
        node = self.head
        prev = None
        while node is not None:
            prev = node
            node = node.next
        if prev is None:
            self.head = MyNode(data)
            return
        prev.next = MyNode(data)

    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.next

    def delete(self, data):
        node = self.head
        prev = None
        next = None
        is_found = False
        while node is not None:
            if node.data == data:
                next = node.next
                is_found = True
                break
            prev = node
            node = node.next
        if is_found:
            prev.next = next
            del node

    def print_list(self):
        node = self.head
        if node is None:
            return ''
        string = ''
        while node is not None:
            string += node.data
            node = node.next
        return string

    def get_all_data(self):
        node = self.head
        data = []
        while node is not None:
            data.append(node.data)
            node = node.next
        return data


class Node(object):

    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def find(self, data):
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def delete(self, data):
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def delete_alt(self, data):
        if data is None:
            return
        if self.head is None:
            return
        curr_node = self.head
        if curr_node.data == data:
            curr_node = curr_node.next
            return
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data


# %load test_linked_list.py
import unittest


class TestLinkedList(unittest.TestCase):

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = MyLinkedList(None)
        linked_list.insert_to_front(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])

        print('Success: test_insert_to_front\n')

        # print('Test: insert_to_front on an empty list')
        # linked_list = LinkedList(None)
        # linked_list.insert_to_front(10)
        # self.assertEqual(linked_list.get_all_data(), [10])
        #
        # print('Test: insert_to_front on a None')
        # linked_list.insert_to_front(None)
        # self.assertEqual(linked_list.get_all_data(), [10])
        #
        # print('Test: insert_to_front general case')
        # linked_list.insert_to_front('a')
        # linked_list.insert_to_front('bc')
        # self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])
        #
        # print('Success: test_insert_to_front\n')

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = MyLinkedList(None)
        linked_list.append(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        self.assertEqual(linked_list.get_all_data(), [10, 'a', 'bc'])

        print('Success: test_append\n')

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = MyLinkedList(None)
        node = linked_list.find('a')
        self.assertEqual(node, None)

        print('Test: find a None')
        head = MyNode(10)
        linked_list = MyLinkedList(head)
        node = linked_list.find(None)
        self.assertEqual(node, None)

        print('Test: find general case with matches')
        head = MyNode(10)
        linked_list = MyLinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        self.assertEqual(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        self.assertEqual(node, None)

        print('Success: test_find\n')

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = MyLinkedList(None)
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = MyNode(10)
        linked_list = MyLinkedList(head)
        linked_list.delete(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = MyNode(10)
        linked_list = MyLinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = MyLinkedList(None)
        self.assertEqual(len(linked_list), 0)

        print('Test: len general case')
        head = MyNode(10)
        linked_list = MyLinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(len(linked_list), 3)

        print('Success: test_len\n')


def main():
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    test.test_find()
    test.test_delete()
    test.test_len()


if __name__ == '__main__':
    main()
