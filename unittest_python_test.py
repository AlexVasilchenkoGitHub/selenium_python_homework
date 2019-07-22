'''
https://stepik.org/lesson/36285/step/12?unit=162401
'''
import unittest

value = 42
neg_value = -value

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(neg_value), value, "{} is not |{}|".format(value, neg_value))
    def test_abs2(self):
        self.assertEqual(abs(neg_value), neg_value, "{} is not |{}|".format(neg_value, neg_value))

if __name__ == "__main__":
    unittest.main()
