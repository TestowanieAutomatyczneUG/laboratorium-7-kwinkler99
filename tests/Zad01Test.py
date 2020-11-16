from sample.zad01 import RomanNumerals
import unittest


class RomanNumeralsTest(unittest.TestCase):

    def test_from_file(self):
        fileTest = open("data/zad01.txt")
        tmpRoman = RomanNumerals()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                inp, result = int(data[0]), data[1].strip("\n")
                self.assertEqual(tmpRoman.roman(inp), result)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
