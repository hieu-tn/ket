"""
Given two strings, find the single different char
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/str_diff/str_diff_challenge.ipynb
"""
from collections import Counter, defaultdict


class DefaultDictCounter(Counter, defaultdict):
    pass


class MySolution(object):
    def find_diff(self, str1: str, str2: str):
        if str1 is None or str2 is None:
            raise TypeError
        for c in str1:
            if str1.count(c) != str2.count(c):
                return c
        for c in str2:
            if c not in str1:
                return c
        return ''

    def find_diff_xor(self, str1: str, str2: str):
        if str1 is None or str2 is None:
            raise TypeError
        l1 = list(str1)
        l2 = list(str2)
        c1 = DefaultDictCounter(l1)
        c2 = DefaultDictCounter(l2)
        xored = ''
        if len(c1) < len(c2):
            for [k, v] in c1.items():
                if v != c2[k]:
                    xored += '1'
                else:
                    xored += '0'
        else:
            for [k, v] in c2.items():
                if v != c1[k]:
                    xored += '1'
                else:
                    xored += '0'
        for i in range(abs(len(c1) - len(c2))):
            xored += '1'
        index = xored.find('1')
        if len(c1) < len(c2):
            l = list(c2.keys())
            return l[index]
        else:
            l = list(c1.keys())
            return l[index]

        return ''


class Solution(object):
    def find_diff(self, str1: str, str2: str):
        if str1 is None or str2 is None:
            raise TypeError
        seen = defaultdict(int)
        for c in str1:
            seen[c] += 1
        for c in str2:
            if c not in seen:
                return c
            seen[c] -= 1
            if seen[c] < 0:
                return c
        for [k, v] in seen.items():
            if v != 0:
                return k
        return ''

    def find_diff_xor(self, str1: str, str2: str):
        if str1 is None or str2 is None:
            raise TypeError
        result = 0
        for char in str1:
            result ^= ord(char)
        for char in str2:
            result ^= ord(char)
        return chr(result)


# %load test_str_diff.py
import unittest


class TestFindDiff(unittest.TestCase):

    def test_find_diff(self):
        my_solution = MySolution()
        self.assertRaises(TypeError, my_solution.find_diff, None)
        self.assertEqual(my_solution.find_diff('ab', 'aab'), 'a')
        self.assertEqual(my_solution.find_diff('aab', 'ab'), 'a')
        self.assertEqual(my_solution.find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(my_solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        self.assertEqual(my_solution.find_diff_xor('ab', 'aab'), 'a')
        self.assertEqual(my_solution.find_diff_xor('aab', 'ab'), 'a')
        self.assertEqual(my_solution.find_diff_xor('abcd', 'abcde'), 'e')
        self.assertEqual(my_solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')

        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None)
        self.assertEqual(solution.find_diff('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff('aab', 'ab'), 'a')
        self.assertEqual(solution.find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        self.assertEqual(solution.find_diff_xor('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff_xor('aab', 'ab'), 'a')
        self.assertEqual(solution.find_diff_xor('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()
