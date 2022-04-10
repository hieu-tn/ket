"""
Find two indices that sum to a specific value
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/two_sum/two_sum_challenge.ipynb
"""


class MySolution(object):
    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError
        if not nums:
            raise ValueError
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == val:
                    return [i, j]
        return []


# %load test_two_sum.py
import unittest


class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        my_solution = MySolution()
        self.assertRaises(TypeError, my_solution.two_sum, None, None)
        self.assertRaises(ValueError, my_solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        self.assertEqual(my_solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


if __name__ == '__main__':
    main()
