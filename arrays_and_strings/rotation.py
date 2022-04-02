from collections import defaultdict


class MyRotation(object):

    def is_substring(self, s1: str, s2: str):
        return s1 in s2

    def is_rotation(self, s1: str, s2: str):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        for c in s1:
            if not self.is_substring(c, s2):
                return False
        return True


class Rotation(object):
    def is_substring(self, s1, s2):
        return s1 in s2

    def is_rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        s3 = s1 + s1
        return self.is_substring(s1, s2 + s2)

# %load test_rotation.py
import unittest


class TestRotation(unittest.TestCase):

    def test_rotation(self):
        my_rotation = MyRotation()
        self.assertEqual(my_rotation.is_rotation('o', 'oo'), False)
        self.assertEqual(my_rotation.is_rotation(None, 'foo'), False)
        self.assertEqual(my_rotation.is_rotation('', 'foo'), False)
        self.assertEqual(my_rotation.is_rotation('', ''), True)
        self.assertEqual(my_rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')

        rotation = Rotation()
        self.assertEqual(rotation.is_rotation('o', 'oo'), False)
        self.assertEqual(rotation.is_rotation(None, 'foo'), False)
        self.assertEqual(rotation.is_rotation('', 'foo'), False)
        self.assertEqual(rotation.is_rotation('', ''), True)
        self.assertEqual(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()
