"""
Implement n stacks using a single array
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/n_stacks/n_stacks_challenge.ipynb
"""


class MyStacks(object):
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack = [None for _ in range(stack_size * num_stacks)]

    def abs_index(self, stack_index):
        if stack_index > self.num_stacks:
            raise Exception
        start = self.stack_size * stack_index
        for i in range(self.stack_size):
            if self.stack[start + i] is None:
                return i
        return self.stack_size

    def push(self, stack_index, data):
        if stack_index > self.num_stacks:
            raise Exception
        abs_index = self.abs_index(stack_index)
        if abs_index >= self.stack_size:
            raise Exception
        self.stack[self.stack_size * stack_index + abs_index] = data

    def pop(self, stack_index):
        if stack_index > self.num_stacks:
            raise Exception
        abs_index = self.abs_index(stack_index)
        if abs_index == 0:
            raise Exception
        data = self.stack[self.stack_size * stack_index + abs_index - 1]
        self.stack[self.stack_size * stack_index + abs_index - 1] = None
        return data


class Stacks(object):
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointer = [-1] * self.num_stacks
        self.stack = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return self.stack_size * stack_index + self.stack_pointer[stack_index]

    def push(self, stack_index, data):
        if self.stack_pointer[stack_index] >= self.stack_size - 1:
            raise Exception
        self.stack_pointer[stack_index] += 1
        abs_index = self.abs_index(stack_index)
        self.stack[abs_index] = data

    def pop(self, stack_index):
        if self.stack_pointer[stack_index] < 0:
            raise Exception
        abs_index = self.abs_index(stack_index)
        data = self.stack[abs_index]
        self.stack[abs_index] = None
        self.stack_pointer[stack_index] -= 1
        return data


# %load test_n_stacks.py
import unittest


class TestStacks(unittest.TestCase):

    def test_pop_on_empty(self, num_stacks, stack_size):
        print('Test: Pop on empty stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.pop(0)

    def test_push_on_full(self, num_stacks, stack_size):
        print('Test: Push to full stack')
        stacks = Stacks(num_stacks, stack_size)
        for i in range(0, stack_size):
            stacks.push(2, i)
        stacks.push(2, stack_size)

    def test_stacks(self, num_stacks, stack_size):
        print('Test: Push to non-full stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')
        self.assertEqual(stacks.pop(0), 2)
        self.assertEqual(stacks.pop(0), 1)
        self.assertEqual(stacks.pop(1), 3)
        self.assertEqual(stacks.pop(2), 4)

        print('Success: test_stacks\n')


def main():
    num_stacks = 3
    stack_size = 10
    test = TestStacks()
    test.assertRaises(Exception, test.test_pop_on_empty, num_stacks,
                      stack_size)
    test.assertRaises(Exception, test.test_push_on_full, num_stacks,
                      stack_size)
    test.test_stacks(num_stacks, stack_size)


if __name__ == '__main__':
    main()
