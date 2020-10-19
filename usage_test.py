import unittest
from usage import Usage

a = Usage(89, 90)
b = Usage(21, 102)


class MyTestCase(unittest.TestCase):
    def test_onlyfirst_list(self):
        self.assertEqual(Usage.sum([a, b, b]), Usage(first=131, second=294))

    def test_everything_param(self):
        self.assertEqual(Usage.sum(a, b, b), Usage(first=131, second=294))

    def test_firstlist_1second(self):
        self.assertEqual(Usage.sum([a, b], b), Usage(first=131, second=294))

    def test_using_addition(self):
        self.assertEqual(a + b + b, Usage(first=131, second=294))

    def test_using_multiplication(self):
        self.assertEqual(a * b, Usage(first=1869, second=9180))

    def test_params_with_tuple(self):
        self.assertEqual(Usage.sum((12, 23), [a, b], (12, 3), [a, b]), Usage(first=244, second=410))

    def test_using_add(self):
        self.assertEqual(a.add(b, a), Usage(first=199, second=282))


if __name__ == '__main__':
    unittest.main()
