"""
Compress a string
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/compress/compress_challenge.ipynb
"""


class MyCompressString(object):
    def compress(self, string: str):
        if string is None:
            return None
        if string == '':
            return ''
        comp = ''
        last_c = ''
        for c in string:
            if last_c == '':
                last_c = c
                continue
            if c == last_c[0]:
                last_c += c
            else:
                comp += last_c[0] + str(len(last_c))
                last_c = c
        comp += last_c[0] + str(len(last_c))
        comp = comp.replace('1', '')
        return comp if len(comp) != len(string) else string


class CompressString(object):
    def compress(self, string: str):
        # if string is None:
        #     return None
        # if string == '':
        #     return ''
        # comp = ''
        # last_c = ''
        # count = 1
        # for c in string:
        #     if last_c == '':
        #         last_c = c
        #         continue
        #     if c == last_c:
        #         count += 1
        #     else:
        #         comp += last_c + str(count)
        #         last_c = c
        #         count = 1
        # comp += last_c + str(count)
        # comp = comp.replace('1', '')
        # return comp if len(comp) < len(string) else string
        if string is None or not string:
            return string
        result = ''
        prev_char = string[0]
        count = 0
        for char in string:
            if char == prev_char:
                count += 1
            else:
                result += self._calc_partial_result(prev_char, count)
                prev_char = char
                count = 1
        result += self._calc_partial_result(prev_char, count)
        return result if len(result) < len(string) else string

    def _calc_partial_result(self, prev_char, count):
        return prev_char + (str(count) if count > 1 else '')


# %load test_compress.py
import unittest


class TestCompress(unittest.TestCase):

    def test_compress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(func('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    my_compress_string = MyCompressString()
    test.test_compress(my_compress_string.compress)
    compress_string = CompressString()
    test.test_compress(compress_string.compress)


if __name__ == '__main__':
    main()
