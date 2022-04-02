from collections import defaultdict


class MyPermutations(object):
    def is_permutation(self, str1: str, str2: str):
        # TODO: Implement me
        if str1 is None or str2 is None:
            return False
        elif str1 == '' or str2 == '':
            return False
        if len(str1) != len(str2):
            return False
        for c in str1:
            if c not in str2:
                return False
        return True


class Permutations(object):
    def is_permutation(self, str1: str, str2: str):
        if str1 is None or str2 is None:
            return False
        elif str1 == '' or str2 == '':
            return False
        # str1, str2 = list(str1), list(str2)
        # str1.sort()
        # str2.sort()
        # return str1 == str2
        return sorted(str1) == sorted(str2)


class PermutationsAlt(object):
    def is_permutation(self, str1: str, str2: str):
        if str1 is None or str2 is None:
            return False
        # d = {}
        # for c in str1:
        #     if c not in d:
        #         d.update({c: 1})
        #     else:
        #         d[c] = d[c] + 1
        # for c in str2:
        #     if c not in d:
        #         d.update({c: 1})
        #     else:
        #         d[c] = d[c] - 1
        # for val in d.values():
        #     if val != 0:
        #         return False
        # return True
        if len(str1) != len(str2):
            return False
        unique_counts1 = defaultdict(int)
        unique_counts2 = defaultdict(int)
        for char in str1:
            unique_counts1[char] += 1
        for char in str2:
            unique_counts2[char] += 1
        return unique_counts1 == unique_counts2



# %load test_permutation_solution.py
import unittest


class TestPermutation(unittest.TestCase):

    def test_permutation(self, func):
        self.assertEqual(func(None, 'foo'), False)
        self.assertEqual(func('', 'foo'), False)
        self.assertEqual(func('Nib', 'bin'), False)
        self.assertEqual(func('act', 'cat'), True)
        self.assertEqual(func('a ct', 'ca t'), True)
        self.assertEqual(func('dog', 'doggo'), False)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    my_permutations = MyPermutations()
    test.test_permutation(my_permutations.is_permutation)
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)
    try:
        permutations_alt = PermutationsAlt()
        test.test_permutation(permutations_alt.is_permutation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
