import unittest
from usage import Usage

a = Usage(89, 90)
b = Usage(21, 102)


class MyTestCase(unittest.TestCase):
    def test_first_second_list(self):
        self.assertEqual(Usage.sum([a, b, b]), Usage(first=131, second=294))

    def test_first_second_usage(self):
        self.assertEqual(Usage.sum(a, b, b), Usage(first=131, second=294))

    def test_first_second_add(self):
        self.assertEqual(a + b + b, Usage(first=131, second=294))

    def test_first_second_mul(self):
        self.assertEqual(a * b, Usage(first=1869, second=9180))


if __name__ == '__main__':
    unittest.main()
