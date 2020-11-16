from sample.zad02 import hamming
import unittest
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal, assert_raises


@parameterized([
    ("", "", 0),
    ("A", "A", 0),
    ("G", "T", 1),
    ("GGACTGAAATCTG", "GGACTGAAATCTG", 0),
    ("GGACGGATTCTG", "AGGACGGATTCT", 9),
])
def test_hamming_third_option(input_one, input_two, expected):
    fast_check = hamming()
    assert_equal(fast_check.distance(input_one, input_two), expected)


class HammingTest(unittest.TestCase):
    @parameterized.expand([
        ("_empty_strands", "", "", 0),
        ("_single_letter_identical_strands", "A", "A", 0),
        ("_single_letter_different_strands", "G", "T", 1),
        ("_long_identical_strands", "GGACTGAAATCTG", "GGACTGAAATCTG", 0),
        ("_long_different_strands", "GGACGGATTCTG", "AGGACGGATTCT", 9),
    ])
    def test_hamming(self, name, input_one, input_two, expected):
        self.assertEqual(self.temp.distance(input_one, input_two), expected)

    def setUp(self):
        self.temp = hamming()


@parameterized_class(('input_one', 'input_two', 'expected'), [
    ("", "", 0),
    ("A", "A", 0),
    ("G", "T", 1),
    ("GGACTGAAATCTG", "GGACTGAAATCTG", 0),
    ("GGACGGATTCTG", "AGGACGGATTCT", 9),
])
class HammingTest2(unittest.TestCase):
    def test_hamming_parameterized(self):
        self.assertEqual(self.tmp.distance(self.input_one, self.input_two), self.expected)

    def setUp(self):
        self.tmp = hamming()


if __name__ == '__main__':
    unittest.main()
