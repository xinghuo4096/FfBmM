
import sys
import unittest
import os
s2 = os.path.abspath('.')
s3 = sys.path
s = 1


class test_hellolib2(unittest.TestCase):
    def test_test(self):
        from pffbklibs import helloLib
        s = helloLib.hello("world", "hello2")
        self.assertTrue(s[:5] == "hello")
        self.assertTrue(len(s) > 5)
        self.assertTrue(s == "hello world ! "+"by python hello2")


class tedst_hellolib3(unittest.TestCase):
    def test_test2(self):
        from pffbklibs import helloLib
        s = helloLib.hello("world", "hello2")
        self.assertTrue(s[:5] == "hello")
        self.assertTrue(len(s) > 5)
        self.assertTrue(s == "hello world ! "+"by python hello2")


if __name__ == '__main__':
    unittest.main()