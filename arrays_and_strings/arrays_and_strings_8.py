"""
Implement Fizz Buzz
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/fizz_buzz/fizz_buzz_challenge.ipynb
"""


class MySolution(object):
    def fizz_buzz(self, num: int):
        if num is None:
            raise TypeError
        if num < 1:
            raise ValueError
        lst = []
        for i in range(1, num + 1):
            if i % 15 == 0:
                lst.append('FizzBuzz')
            elif i % 5 == 0:
                lst.append('Buzz')
            elif i % 3 == 0:
                lst.append('Fizz')
            else:
                lst.append(str(i))
        return lst


class Solution(object):
    def fizz_buzz(self, num):
        if num is None:
            raise TypeError('num cannot be None')
        if num < 1:
            raise ValueError('num cannot be less than one')
        results = []
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results


# %load test_fizz_buzz.py
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        solution = MySolution()
        self.assertRaises(TypeError, solution.fizz_buzz, None)
        self.assertRaises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')

        solution = Solution()
        self.assertRaises(TypeError, solution.fizz_buzz, None)
        self.assertRaises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()
