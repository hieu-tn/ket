"""
Implement a hash table
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/hash_map/hash_map_challenge.ipynb
"""


class MyItem(object):
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashTable(object):
    table = None

    def __init__(self, size):
        self.table = list()

    def _hash_function(self, key):
        return key % len(self.table)

    def set(self, key, value):
        is_existed = False
        for item in self.table:
            if item.key == key:
                item.value = value
                is_existed = True
        if not is_existed:
            item = MyItem(key, value)
            self.table.append(item)

    def get(self, key):
        for item in self.table:
            if item.key == key:
                return item.value
        raise KeyError

    def remove(self, key):
        index = -1
        for i in range(len(self.table)):
            if self.table[i].key == key:
                index = i
        if index != -1:
            self.table = self.table[0:index] + self.table[index + 1: -1]
        else:
            raise KeyError


class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError


# %load test_hash_map.py
import unittest


class TestHashMap(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        my_hash_table = MyHashTable(10)

        print("Test: get on an empty hash table index")
        self.assertRaises(KeyError, my_hash_table.get, 0)

        print("Test: set on an empty hash table index")
        my_hash_table.set(0, 'foo')
        self.assertEqual(my_hash_table.get(0), 'foo')
        my_hash_table.set(1, 'bar')
        self.assertEqual(my_hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        my_hash_table.set(10, 'foo2')
        self.assertEqual(my_hash_table.get(0), 'foo')
        self.assertEqual(my_hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        my_hash_table.set(10, 'foo3')
        self.assertEqual(my_hash_table.get(0), 'foo')
        self.assertEqual(my_hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        my_hash_table.remove(10)
        self.assertEqual(my_hash_table.get(0), 'foo')
        self.assertRaises(KeyError, my_hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        self.assertRaises(KeyError, my_hash_table.remove, -1)

        print('Success: test_end_to_end')

        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        self.assertEqual(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        self.assertEqual(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo2')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'foo3')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertRaises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        self.assertRaises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
