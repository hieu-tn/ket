"""
Sort a stack using another stack as a buffer
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/sort_stack/sort_stack_challenge.ipynb
"""
from stacks_and_queues.stacks_and_queues_5 import MyStack as PersonalStack, Stack


class MyMyStack(PersonalStack):
    def sort(self):
        if self.top is None or self.top.next is None:
            return self
        node = self.top
        prev = None
        while node.next is not None:
            next_node = node.next
            if node.data < next_node.data:
                node.next = next_node.next
                next_node.next = node
                if prev:
                    prev.next = next_node
                    prev = None
                if node == self.top:
                    self.top = next_node
                else:
                    node = self.top
            else:
                prev = node
                node = node.next
        return self


class MyStack(Stack):
    def sort(self):
        buffer = Stack()
        # [6, 3, 2, 7, 9 10 6 3 5]
        # tmp 2
        # buffer 2
        while not self.is_empty():
            tmp = self.pop()
            if buffer.top and buffer.top.data > tmp:
                while not buffer.is_empty():
                    self.push(buffer.pop())
            buffer.push(tmp)
        return buffer


# %load test_sort_stack.py
from random import randint
import unittest


class TestSortStack(unittest.TestCase):

    def get_sorted_stack(self, stack, numbers):
        for x in numbers:
            stack.push(x)
        sorted_stack = stack.sort()
        return sorted_stack

    def test_sort_stack(self, stack):
        print('Test: Empty stack')
        sorted_stack = self.get_sorted_stack(stack, [])
        self.assertEqual(sorted_stack.pop(), None)

        print('Test: One element stack')
        sorted_stack = self.get_sorted_stack(stack, [1])
        self.assertEqual(sorted_stack.pop(), 1)

        print('Test: Two or more element stack (general case)')
        num_items = 10
        numbers = [randint(0, 10) for x in range(num_items)]
        sorted_stack = self.get_sorted_stack(stack, numbers)
        sorted_numbers = []
        for _ in range(num_items):
            sorted_numbers.append(sorted_stack.pop())
        self.assertEqual(sorted_numbers, sorted(numbers, reverse=True))

        print('Success: test_sort_stack')


def main():
    test = TestSortStack()
    test.test_sort_stack(MyStack())
    # try:
    #     test.test_sort_stack(MyStackSimplified())
    # except NameError:
    #     # Alternate solutions are only defined
    #     # in the solutions file
    #     pass


if __name__ == '__main__':
    main()
