import unittest

from main import ourprogram


class Testfile(unittest.TestCase):
    def test_ourprogram(self):
        actual = ourprogram('ttext.json')
        expected = "success"
        self.assertEqual(actual,expected)
        actual1 = ourprogram('ttext.json')
        expected1 = "json file is not properly defined"
        self.assertEqual(actual1,expected1)

if __name__ == '__main__':
    unittest.main()

