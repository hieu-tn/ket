class MyUniqueChars(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        elif string == '':
            return True
        seen = []
        for c in string:
            if c in seen:
                return False
            else:
                seen.append(c)

        return True


class UniqueChars(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        seen = set()
        for c in string:
            if c not in seen:
                seen.add(c)
            else:
                return False
        return True


class UniqueCharsSet(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        seen = set(string)
        return len(seen) == len(string)


class UniqueCharsInPlace(object):
    def has_unique_chars(self, string: str):
        if string is None:
            return False
        for c in string:
            # count = 0
            # for other_c in string:
            #     if other_c == c:
            #         count += 1
            # if count > 1:
            #     return False
            if string.count(c) > 1:
                return False
        return True


# %load test_unique_chars.py
import unittest


class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self, func):
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    my_unique_chars = MyUniqueChars()
    test.test_unique_chars(my_unique_chars.has_unique_chars)
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        unique_chars_in_place = UniqueCharsInPlace()
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
