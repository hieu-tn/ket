"""
Implement a set of stacks class that wraps a list of capacity-bounded stacks
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/set_of_stacks/set_of_stacks_challenge.ipynb
"""
from stacks_and_queues.stacks_and_queues_5 import MyStack, Stack, Node


class MyStackWithCapacity(MyStack):
    def __init__(self, top=None, capacity=10):
        super().__init__(top)
        self.capacity = capacity

    def push(self, data):
        if self.is_full():
            return
        super().push(data)

    def pop(self):
        return super().pop()

    def is_full(self):
        node = self.top
        counter = 0
        while node is not None:
            counter += 1
            node = node.next
        return counter == self.capacity


class MySetOfStacks(object):
    def __init__(self, indiv_stack_capacity):
        self.indiv_stack_capacity = indiv_stack_capacity
        self.stacks = None

    def push(self, data):
        if not self.stacks:
            stack = MyStackWithCapacity(capacity=self.indiv_stack_capacity)
            stack.push(data)
            self.stacks = [stack]
        else:
            if self.stacks[len(self.stacks) - 1].is_full():
                stack = MyStackWithCapacity(capacity=self.indiv_stack_capacity)
                stack.push(data)
                self.stacks.append(stack)
            else:
                self.stacks[len(self.stacks) - 1].push(data)

    def pop(self):
        if not self.stacks:
            return
        data = self.stacks[len(self.stacks) - 1].pop()
        if self.stacks[len(self.stacks) - 1].top is None:
            self.stacks.pop()
        return data


class StackWithCapacity(Stack):
    def __init__(self, top=None, capacity=10):
        super().__init__(top)
        self.capacity = capacity
        self.num_items = 0

    def push(self, data):
        if self.is_full():
            raise Exception
        super().push(data)
        self.num_items += 1

    def pop(self):
        self.num_items -= 1
        return super().pop()

    def is_full(self):
        return self.num_items == self.capacity

    def is_empty(self):
        return self.num_items == 0


class SetOfStacks(object):
    def __init__(self, indiv_stack_capacity):
        self.indiv_stack_capacity = indiv_stack_capacity
        self.stacks = []
        self.last_stack = None

    def push(self, data):
        if not self.last_stack or self.last_stack.is_full():
            stack = StackWithCapacity(capacity=self.indiv_stack_capacity)
            self.last_stack = stack
            self.stacks.append(stack)
        self.last_stack.push(data)

    def pop(self):
        if not self.last_stack:
            return
        data = self.last_stack.pop()
        if self.last_stack.is_empty():
            self.stacks.pop()
            self.last_stack = self.stacks[-1] if self.stacks else None
        return data


# %load test_set_of_stacks.py
import unittest


class TestSetOfStacks(unittest.TestCase):

    def test_set_of_stacks(self):
        print('Test: Push on an empty stack')
        stacks = SetOfStacks(indiv_stack_capacity=2)
        stacks.push(3)

        print('Test: Push on a non-empty stack')
        stacks.push(5)

        print('Test: Push on a capacity stack to create a new one')
        stacks.push('a')

        print('Test: Pop on a stack to destroy it')
        self.assertEqual(stacks.pop(), 'a')

        print('Test: Pop general case')
        self.assertEqual(stacks.pop(), 5)
        self.assertEqual(stacks.pop(), 3)

        print('Test: Pop on no elements')
        self.assertEqual(stacks.pop(), None)

        print('Success: test_set_of_stacks')


def main():
    test = TestSetOfStacks()
    test.test_set_of_stacks()


if __name__ == '__main__':
    main()
