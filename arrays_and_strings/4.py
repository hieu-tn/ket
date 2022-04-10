"""
Reverse characters in a string
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/reverse_string/reverse_string_challenge.ipynb
"""


class MyReverseString(object):
    def reverse(self, chars: list):
        if chars is None:
            return None
        tmp = list(chars)
        counter = len(chars)
        for i in range(counter):
            chars.insert(0, tmp[i])
        for i in range(counter):
            chars.pop(counter)
        return chars


class ReverseString(object):
    def reverse(self, chars: list):
        # if chars is None:
        #     return None
        # for i in range(int(len(chars) / 2)):
        #     tmp = chars[i]
        #     chars[i] = chars[len(chars) - 1 - i]
        #     chars[len(chars) - 1 - i] = tmp
        # return chars
        if chars:
            size = len(chars)
            for i in range(size // 2):
                chars[i], chars[size - 1 - i] = chars[size - 1 - i], chars[i]
        return chars


# %load test_reverse_string.py
import unittest


class TestReverse(unittest.TestCase):

    def test_reverse(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(['']), [''])
        self.assertEqual(func(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self, func):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        func(target_list)
        self.assertEqual(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    my_reverse_string = MyReverseString()
    test.test_reverse(my_reverse_string.reverse)
    test.test_reverse_inplace(my_reverse_string.reverse)
    reverse_string = ReverseString()
    test.test_reverse(reverse_string.reverse)
    test.test_reverse_inplace(reverse_string.reverse)


if __name__ == '__main__':
    main()
